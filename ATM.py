#Name of programmer: Aditya D Malode
#git: https://github.com/Ady-6720
#LinkedIN: https://www.linkedin.com/in/aditya-malode-749585158

#Problem Statement:
#problem code: HS08TEST
#Pooja would like to withdraw X $US from an ATM. 
# The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges).
# For each successful withdrawal the bank charges 0.50 $US. 
# Calculate Pooja's account balance after an attempted transaction

import time as t
bal=2000
print("Hello Pooja Welcome to Bank Of Gotham !")
print("Your account balance is : 2000.USD")
t.sleep(3)

data_valid = False
while data_valid == False:
    withdraw =input("Please Enter ammount to withdraw correctly.")
    try:
        withdraw = float(withdraw)
    except:
        print("Enter a valid Ammount avoid alphabetical characters !")
        continue
    if withdraw>2000:
        print("The ammount you want to withdraw can not be proceed due to insuffcient funds.")
        continue
    else:
        data_valid = True

    
if(withdraw%5==0):
    final_bal=float(bal-(withdraw+0.50))
    print("Transaction Successfull!")
    t.sleep(1.5)
    print("Updated account balance: ",round(float(final_bal),2),".USD.")
else:
    print("The ammount you entered can not be withdrawned !")
    t.sleep(2)
    print("Bal= 2000.USD")
