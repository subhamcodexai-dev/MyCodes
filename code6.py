# ---------------Personal Bank Account-------------Using Typecasting-----------


Account_Holder_Name = "Lisa"
Current_Balance = 70000.78
Deposit_This_Month = 10000.10
Minimum_Balance_Required = 1001
Drawings = 2006
Total_Interest_Received = 206


Current_Balance = float(Current_Balance)
Deposit_This_Month = float(Deposit_This_Month)
Minimum_Balance_Required = float(Minimum_Balance_Required)
Drawings = float(Drawings)
Total_Interest_Received = float(Total_Interest_Received)


Final_Balance = Current_Balance + Deposit_This_Month + Total_Interest_Received - Drawings
Account_Active = bool(Final_Balance)
Above_Minimum_Balance = bool(Final_Balance > Minimum_Balance_Required)


print("_____Personal Bank Account Status_____")
print("Holder's Name:" + Account_Holder_Name)
print("Total Balance:" + str(Final_Balance))
print("Is Account Still Active:" + str(Account_Active))
print("Is balance above minimum requirement:" + str(Above_Minimum_Balance))
print("Total Interest Received:" + str(Total_Interest_Received))
print("Total Drawings:" + str(Drawings))
      

