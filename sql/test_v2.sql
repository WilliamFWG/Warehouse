drop procedure if exists testdb1.cal_rate_amount;
-- variable Input_Inv_no is for Merchant Invoice Number
create procedure testdb1.cal_rate_amount(in Input_Inv_no varchar(20)) 
begin 
    declare var_TxnRcd varchar(20); 
    declare var_MerID varchar(20);
    declare var_Tktno varchar(13); 
    declare var_AmtInvTax decimal(15,2); 
    declare var_TxnType enum('A','F','K','H','T','O','C');
    declare var_Act_No varchar(19); 
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
            mch.Txn_Type as var_TxnType,
            mch.Act_No as var_Act_No 
            from mch 
            where mch.Inv_no=Input_Inv_no; 
    -- preset handler s to stop circle loop  
    DECLARE CONTINUE HANDLER FOR SQLSTATE '02000' SET s=1;
    start transaction; 
    open csr; 
    -- fetch var  from the cursor in first row
    fetch csr into var_TxnRcd,var_MerID,var_Tktno,var_AmtInvTax,var_TxnType,var_Act_No;
    -- get the minium charge from Mer_Profile table into var_min 
    select Mer_Profile.Min_Charge from Mer_Profile where Mer_Profile.Mer_ID=var_MerID into var_min;
    while s<>1 do
    -- Conditional statement to define the rate base on Merchant ID and Transaction Type into var_TxnRate
    -- Type Rate is not exist in CA_List  
        if not exists (
            select CA_List.Type_Rate
            from CA_List 
            where CA_List.CA_No = var_Act_No and CA_List.Txn_Type=var_TxnType) then

                call verify_Merchant_rate(var_MerID,var_TxnType,var_Tktno,var_TxnRate);
        else   
        -- Type rate exists in CA_List
            select CA_List.Type_Rate into var_TxnRate 
            from CA_List
            where CA_List.CA_No = var_Act_No and CA_List.Txn_Type=var_TxnType;

        end if;

        -- verify the merchant service fee base on the txn rate and minium charge
        call testdb1.get_msf(var_AmtInvTax,var_TxnRate,var_min,var_msf);

        -- insert the value into Fee_Cal table base on calculation result
        insert into Fee_Cal 
        (Inv_no,Txn_Rcd,Mer_ID,TKT_No,Txn_Type,Txn_Rate,Amt,Rate_Amount) 
        values(
        Input_Inv_no,var_TxnRcd,var_MerID,var_Tktno,var_TxnType,var_TxnRate,var_AmtInvTax,
        round(var_msf,3)
        );
        fetch csr into var_TxnRcd,var_MerID,var_Tktno,var_AmtInvTax,var_TxnType,var_Act_No;
    end while;
    close csr;
    commit;
end;




    