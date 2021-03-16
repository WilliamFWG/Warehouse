drop procedure if exists testdb1.cal_rate_amount;
-- variable Input_Inv_no is for Merchant Invoice Number
create procedure testdb1.cal_rate_amount(in Input_Inv_no varchar(20)) 
begin 
    declare var_TxnRcd varchar(20); 
    declare var_MerID varchar(20);
    declare var_Tktno varchar(13); 
    declare var_AmtInvTax decimal(15,2); 
    declare var_TxnType enum('A','F','K','H','T','O','C'); 
    declare var_TxnRate decimal(5,3); 
    declare var_min decimal(5,2);
    declare var_msf decimal(15,2);
    declare s int default 0;
    -- create csr cursor for mch table
    declare csr cursor for  
        select mch.Txn_Rcd as var_TxnRcd,
            mch.Mer_ID as var_MerID,
            mch.TKT_No as var_Tktno,
            mch.Amt_Inv_Tax as var_AmtInvTax,
            mch.Txn_Type as var_TxnType 
            from mch 
            where mch.Inv_no=Input_Inv_no; 
    -- preset handler s to stop circle loop  
    DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET s=1;
    start transaction; 
    open csr; 
    -- fetch var  from the cursor in first row
    fetch csr into var_TxnRcd,var_MerID,var_Tktno,var_AmtInvTax,var_TxnType;
    -- get the minium charge from Mer_Profile table into var_min 
    select Mer_Profile.Min_Charge from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_min;
    while s<>1 do
    -- conditional statement to define the rate base on Merchant ID and Transaction Type into var_TxnRate
        if var_TxnType="F" then
        -- if F type and start with 784 means CZ transactions
            if substring(var_Tktno,1,3)="784" then
                select Mer_Profile.CZ_Per from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_TxnRate;
            else
                select Mer_Profile.Non_UATP_Per from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_TxnRate;
            end if;
        elseif var_TxnType="A" then
            select Mer_Profile.A_Per from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_TxnRate;
        elseif var_TxnType="K" then
            select Mer_Profile.K_Per from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_TxnRate;
        elseif var_TxnType="T" then
            select Mer_Profile.T_Per from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_TxnRate;
        elseif var_TxnType="O" then
            select Mer_Profile.O_Per from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_TxnRate;  
        elseif var_TxnType="H" then
            select Mer_Profile.H_Per from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_TxnRate; 
        elseif var_TxnType="C" then
            select Mer_Profile.C_Per from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_TxnRate; 
        end if;
        -- verify the merchant service fee base on the txn rate and minium charge
        if var_AmtInvTax<0 then
            -- amount<0  then msf>0
            if abs(var_AmtInvTax*var_TxnRate)>var_min then
                -- select abs(var_AmtInvTax*var_TxnRate) into var_msf;
                set var_msf=abs(var_AmtInvTax*var_TxnRate);
            else
                -- select var_min into var_msf;
                set var_msf= var_min;
            end if;
        else
            -- amount>0 then msf<0
            if var_AmtInvTax*var_TxnRate>var_min then
                set var_msf=-1*var_AmtInvTax*var_TxnRate;
            else
                set var_msf=var_min *(-1);
            end if;
        end if;
        -- insert the value into Fee_Cal table base on calculation result
        insert into Fee_Cal 
        (Inv_no,Txn_Rcd,Mer_ID,TKT_No,Txn_Type,Txn_Rate,Amt,Rate_Amount) 
        values(
        Input_Inv_no,var_TxnRcd,var_MerID,var_Tktno,var_TxnType,var_TxnRate,var_AmtInvTax,
        round(var_msf,3)
        );
        fetch csr into var_TxnRcd,var_MerID,var_Tktno,var_AmtInvTax,var_TxnType;
    end while;
    close csr;
    commit;
end;




    