# count = 0 
# while count < 10:
#     print(count)
#     count += 1

# use the while loop and print out numbers from 0 to 5

# use the while loop and print out numbers from 1 to 5

# use the while loop and print out multiples of 5 from 5 to 50

# use the while loop and print out numbers from 10 to 1

# count = 0
# while count < 6 :
#     print(count)
#     count += 1

# count = 1
# while count < 6 :
#     print(count)
#     count += 1

# count = 5
# while count < 51 :
#     print(count)
#     count += 5

# count = 10
# while count > 0 :
#     print(count)
#     count -= 1

# while True: 
#     age = input("enter your age: ")
#     if age .isdigit():
#         age = int(age)
#         if age > 16: 
#             print("You go to JC.")
#         elif age > 12:
#             print("You go to Secondary")
#         elif age > 6:
#             print("You go to Primary")
#         else:
#             print("You are too young")
#         break
#     else: 
#         print("this is not a number")

while True:
    age = input("enter your age: ")
    if age .isdigit():
        age = int(age)
        if age < 7:
            print("Your bus fare is free")
        elif age <13:
            print("Your bus fare is $2.00")
        elif age < 22:
            print("Your bus fare is $4.00")
        elif age < 61:
            print("Your bus fare is $10.00")
        else:
            print("Your bus fare is $1.00")
        break
    else: 
        print("this is not a number")




# Recap and Warm up - DO THIS

# write a program to help categorise how much bus fare to pay

# ask user to input an age

# check if age is a valid number # <str>.isdigit()

# use if, elif and else
# age < 7, free
# between 7 to 12, $2.00
# between 13 to 21, $4.00
# between 22 to 60, $10.00
# 61 and above, $1.00

# Print out the correct fare according to the age.