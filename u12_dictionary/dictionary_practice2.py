

# menu ordering system

# ask customer what they want to buy?

# if item exist in your dictionary, say the price

# else, you say sorry i don't sell

# keep asking until customer say "enough"

# bonus 1: calculate the total amount of what customer buy
# bonus 2: you print out the items and price of what the customer buy
# menu = {"hamburger": 6.50, "spaghetti": 12.00, "soup": 7.50, "fries":5.00, "pizza": 25.80}
# count = 0
# while True:
    
#     ask = input("What do you want?: ")
#     if ask != "enough":
#         if ask in menu:
#             print(f"{ask} is ${menu[ask]:.2f}")
#             count += menu[ask]
#         else:
#             print(f"sorry i dont sell {ask}")
#     else:
#         print(count)
#         break





student_scores = {"kevin": 65, "linda":88, "malcolm":67, "joseph":34, "ethan":76}

# retrieve the score for kevin
print(student_scores["kevin"])

# change score of joseph to 88
student_scores["joseph"] = 88
print(student_scores)
# add a new student/ score >> mark : 64
student_scores["D"] = 64
print(student_scores)
# delete kevin from dictionary
del student_scores["kevin"]
print(student_scores)