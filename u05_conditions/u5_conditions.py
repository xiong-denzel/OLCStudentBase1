# num1 = 10
# num2 = 10

# if num1 > num2:
#     print(f"{num1} is more than {num2}")
# elif num1 == num2:
#     print(f"{num1} is equal to {num2}")
# else:
#     print(f"{num1} is not more than {num2}")

# password = "123"

# for j in range(3):
#     inputpassword = input("enter a password: ")

#     if inputpassword == password:
#         print("Access Granted")
#         break # stop this loop
#     else:
#         print("Access Denied")
# else:
#     print("Account locked out")

# import random
# for i in range(30):
#     num1 = random.randint(20, 50)
#     print(num1)


# import random
# marks = 0
# for i in range(10):
#     num1 = random.randint(1,5)
#     num2 = random.randint(1,5)
#     answer = int(input(f"what is {num1} + {num2}? "))

#     if answer == num1 + num2:
#         print("Correct.")
#         marks += 1
#     else:
#         print("Wrong.")
# if marks >= 5 :
#     print(f"You scored {marks} out of 10, well done!")
# else:
#     print("You failed, go and see the princaple")
# Random number guesseing program 
# generate a random number from 1 to 100
# need to loop for 7 times
# input the number
# check if bigger or smaller
# bigger 
# smaller 
# equal

import random

print("*"*50)
print("Guess my number from 1 to 50!")
rannum = random.randint(1,50)
for i in range(50):
    guess = int(input("Guess a number "))
    if guess > rannum:
        print(f"Your {guess} needs to be smaller")
    elif guess == rannum:
        print(f"Your {guess} is correct!")  
        break 
    else: 
        print(f"Your {guess} needs to be bigger")