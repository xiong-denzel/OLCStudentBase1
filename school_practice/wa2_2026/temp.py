# Task 1.1
usrNme_inData = "eddiep"
pin_inData = "1234"
bal_inData = 1000.00

print("Hello, welcome to Bank’s ATM.")
username = input("Please enter your username: ")
pin = input("Please enter your pin: ")
if username == usrNme_inData and pin == pin_inData:
    print(f"Hello, {usrNme_inData}, welcome to Bank's ATM.")
else:
    print("Invalid username or PIN")

# seems like a more basic version

#Task 1.2
usrNme_inData = "eddiep"
pin_inData = "1234"
bal_inData = 1000.00
print("Hello, welcome to Bank’s ATM.")
username = input("Please enter your username: ")
pin = input("Please enter your pin: ")
if username == usrNme_inData and pin == pin_inData:
    print("Hello, welcome to Bank's ATM.")
else:
    print("Invalid username or PIN")
# 1.1: 3/4
# inputs                     1m
# credentials chk            1m
# upper                      0m name and upper() mssing
# outputs                    1m

# 1.2: 4/6
# while loop                 1m
# process for opt 1          1m
# process for opt 2          1m
# process for opt 3  
#     [rng chk]              0m
#     [resulting conditions] 0m
# process for opt 4          1m
# TASK 1: 7/10
menu = "Bank ATM Menu:\n(1) check balance\n(2) deposit money\n(3) withdraw money\n(4) exit"
while True:
    print(menu)
    option = input("Please enter your option (1 to 4):")
    if option == "1":
        print(bal_inData)
    elif option == "2":
        depamt = int(input("Enter amount: "))
        bal_inData += depamt
    elif option == "3":
        witamt = int(input("Enter amount: ")) # why int? # float()

        # check if you have enough money to withdraw
        if bal_inData < witamt:
            print("Insufficient funds.")
        else:
            bal_inData +- witamt


    for i in range(len(bal_inData)): # whats the point of a loop here?
        if bal_inData[i] < witamt: # syntax error
                print("Insufficient funds.")
        else:
                bal_inData +- witamt
        print(bal_inData)
    else:
        break