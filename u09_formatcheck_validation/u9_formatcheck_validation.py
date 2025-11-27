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

pin = "123141414"
print(len(pin))

while True: 
    otp = input("Enter a 4 digit OTP: ")

    if not otp.isdigit(): 
        print("OTP must be a number!")
    elif len(otp) != 4:
        print("OTP must be 4 digits!")
    else: 
        print("OTP is vallid.")
        break
    