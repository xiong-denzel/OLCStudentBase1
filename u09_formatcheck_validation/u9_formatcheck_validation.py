'''
Question 1 (Length Check):
Write the input entry and validation code for a program that
needs to accept a 4-digit OTP (One-Time Password)
The OTP must be exactly 4 digits long

If the input is invalid, your code should keep trying
by asking for the input to be entered again.

#########################################

Sample output

Enter OTP: 12
Invalid input. The OTP must be exactly 4 digits.

Enter OTP: 12345

Invalid input. The OTP must be exactly 4 digits

Enter OTP: 1234
OTP accepted

'''

# pin = "123141414"
# print(len(pin))

# while True: 
#     otp = input("Enter a 4 digit OTP: ")

#     if not otp.isdigit(): 
#         print("OTP must be a number!")
#     elif len(otp) != 4:
#         print("OTP must be 4 digits!")
#     else: 
#         print("OTP is vallid.")
#         break
    



###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 10: Validating Uppercase Input
# Scenario: You are entering product codes into a system, and 
# all codes must be in uppercase letters (e.g., "ABC123").
# while True:
#     code=input("Enter code: ")
#     if code.isupper():
#         print("valid")
#         break
#     else:
#         print("Try again")




#------------------------------------------------------------
# Exercise 11: Validating Alphanumeric Input
# Scenario: A username field only accepts alphanumeric characters
# (letters and numbers) without special symbols.
# while True:
#     username = input("enter a username: ")
#     if username.isalnum(): #.isalnum
#         print("accepted")
#         break
#     else:
#         print("try again with alphanumeric characters")
        





#------------------------------------------------------------
# Exercise 12: Validating Numeric Input
# Scenario: You are collecting a phone number that must contain 
# only numeric characters.

# isdigit() # isnumeric()
# while True:
#     pn = input("Enter phone number: ")
#     if pn.isdigit():
#         print("OK")
#         break
#     else:
#         print("Not OK")



#------------------------------------------------------------
# Exercise 13: Checking for Substrings
# Scenario: You are searching for the word "Python" in user 
# feedback to categorize responses related to Python programming.

# listwords = ["python","tiger","lion"]
# if python in listwords:

# feedback = input("enter a sentence")
# if "Python" in feedback:
#     print("Exists")
# else:
#     print("Doesnt exist")





#------------------------------------------------------------
# Exercise 14: Replacing Parts of a String
# Scenario: A user entered their old email address, and you 
# need to replace it with a new domain (e.g., from "@old.com" to "@new.com").
# old = input("Enter email address: ")
# print(old.replace("@old.com","@new.com" ))



# isalpha() isdigit() isnumeric() islower() isupper() isspace() isalnum()

#------------------------------------------------------------


# ============================================================
# Exercise 1: Singapore Postal Code
# ============================================================

'''
Ask the user to enter a Singapore postal code.

The postal code must:
- Be exactly 6 digits long
- Contain digits only

Keep asking until a valid input is entered.
'''
#--------------------------------------------------------------------
# Write your code here
# while True:
#     postal = input("enter a sgp postal code: ")
#     if len(postal) != 6:
#         print("Enter 6 digits only")
#     elif not postal.isdigit():
#         print("Enter numbers only")
#     else:
#         print("accepted")
#         break







# ============================================================
# Exercise 6: Singapore Mobile Number
# ============================================================

'''
Ask the user to enter a Singapore mobile number.

The mobile number must:
- Be exactly 8 digits long
- Start with 8 or 9

Keep asking until a valid input is entered.
'''
#--------------------------------------------------------------------
# Write your code here
# while True:
#     mobile = input("enter a sgp mobile number: ")
#     if len(mobile) != 8:
#         print("Retry with 8 digits")
#     elif not mobile[0] == "8" and not mobile[0] == "9":
#         print("Must start with 8 or 9")
#     else:
#         print("accepted")
#         break


# ============================================================
# Exercise 7: Student ID
# ============================================================

'''
Ask the user to enter a student ID.

The student ID must:
- Be exactly 6 characters long
- Start with "S"
- Have 5 digits after "S"

Examples:
S00001
S12345
S99999

Keep asking until a valid input is entered.
'''
#--------------------------------------------------------------------
# Write your code here
# while True:
#     ask = input("enter a student ID: ")
#     if len(ask) != 6:
#         print("must be exactly 6 char long")
#     elif ask[0] != "S":
#         print("must start with S")
#     elif not ask[1:].isdigit():
#         print("must have 5 digit after S")
#     else:
#         print("accepted")
#         break




# ============================================================
# Exercise 8: Product Code
# ============================================================

'''
Ask the user to enter a product code.

The valid product codes are:

valid_codes = ["BK101", "BK102", "PN201", "PN202", "FD301"]

The input must exist in the list.

Keep asking until a valid input is entered.
'''

#--------------------------------------------------------------------
# Write your code here
# valid_codes = ["BK101", "BK102", "PN201", "PN202", "FD301"]
# while True:
#     ask = input("enter a product code")
#     if ask in valid_codes:
#         print("exists")
#         break



# ============================================================
# Exercise 4: Menu Option
# ============================================================

'''
Display this menu:

1. Add Student
2. Remove Student
3. View Student
4. Exit

Ask the user to enter an option.

The option must be a number from 1 to 4.

Keep asking until a valid input is entered.
'''
#--------------------------------------------------------------------
# Write your code here
# menu = '''Display this menu:
# 1. Add Student
# 2. Remove Student
# 3. View Student
# 4. Exit'''

# while True:
#     print(menu)
#     ask = input("enter an option: 1,2,3,4: ")
#     if ask in "1234":
#         print("Ok")
#         break
#     else:
#         print("enter 1,2,3 or 4")


word = "singapore"

# sin
print(word[:3])

#gap
print(word[3:6])
# last 3 characters
print(word[-3:])

# reverse 
print(word[::-2])