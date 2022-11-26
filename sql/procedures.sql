drop procedure if exists testdb1.verify_Merchant_rate;
create procedure testdb1.verify_Merchant_rate(
    in Input_MerID varchar(20),
    in Input_TxnType varchar(20),
    in Input_Tktno varchar(13),
    out Output_TxnRate decimal(5,3)
)
begin 
    if Input_TxnType="F" then
    -- if F type and start with 784 means CZ transactions
        if substring(Input_Tktno,1,3)="784" then
            select Mer_Profile.CZ_Per from Mer_Profile where Mer_Profile.Mer_ID=Input_MerID into Output_TxnRate;
        else
            select Mer_Profile.Non_UATP_Per from Mer_Profile where Mer_Profile.Mer_ID=Input_MerID into Output_TxnRate;
        end if;
    elseif Input_TxnType="A" then
        select Mer_Profile.A_Per from Mer_Profile where Mer_Profile.Mer_ID=Input_MerID into Output_TxnRate;
    elseif Input_TxnType="K" then
        select Mer_Profile.K_Per from Mer_Profile where Mer_Profile.Mer_ID=Input_MerID into Output_TxnRate;
    elseif Input_TxnType="T" then
        select Mer_Profile.T_Per from Mer_Profile where Mer_Profile.Mer_ID=Input_MerID into Output_TxnRate;
    elseif Input_TxnType="O" then
        select Mer_Profile.O_Per from Mer_Profile where Mer_Profile.Mer_ID=Input_MerID into Output_TxnRate;  
    elseif Input_TxnType="H" then
        select Mer_Profile.H_Per from Mer_Profile where Mer_Profile.Mer_ID=Input_MerID into Output_TxnRate; 
    elseif Input_TxnType="C" then
        select Mer_Profile.C_Per from Mer_Profile where Mer_Profile.Mer_ID=Input_MerID into Output_TxnRate; 
    end if;
end;

drop procedure if exists testdb1.get_msf;
create procedure testdb1.get_msf(
    in Input_AmtInvTax decimal(15,2), 
    in Input_TxnRate decimal(5,3),
    in Input_min decimal(5,2),
    out Output_msf decimal(15,2)
)
begin
    if Input_AmtInvTax<0 then
        -- amount<0  then msf>0
        if abs(Input_AmtInvTax*Input_TxnRate) then
            -- select abs(Input_AmtInvTax*Input_TxnRate) into Output_msf;
            set Output_msf=abs(Input_AmtInvTax*Input_TxnRate);
        else
            -- selecInput into Output_msf;
            set Output_msf= Input_min;
        end if;
    else
        -- amount>0 then msf<0
        if Input_AmtInvTax*Input_TxnRate then
            set Output_msf=-1*Input_AmtInvTax*Input_TxnRate;
        else
            set Output_msf=Input_min*(-1);
        end if;
    end if;
end;

