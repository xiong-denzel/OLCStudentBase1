# menu = {"hamburger": "$2.00", "fries" : "$1.00", "pasta" : "$3.50"}
# priceham = menu["hamburger"]
# print(priceham)

# menu["hamburger"] = "$20.00"
# print(menu)

# menu["pizza"] = "$30.00"
# print(menu)

# del menu["fries"]
# print(menu)

# for food, price in menu.items():
#     print(f"{food} : {price}")
# choice = input("Hello sir, what would you like to eat? ")
# if choice in menu:
#     print(f"{choice} is {menu[choice]}")
# else: 
#     print(f"Sorry i do not sell {choice}")

# newfood = input("Enter name of new food: ")
# newprice = input("Enter name of new price: ")

# menu["newfood"] = "[new price]"
# print("Food has been added to dictionary, Thank you for your suggestion!")


# A student is writing a program to note down 
# the favourite sports of each of his classmates.
# the program will help check how many students like a certain sport.



# Write a program that will 
# -------------------------------------------------
# 1. ask how many students there are in the class

# -------------------------------------------------
# 2. for each student, ask what is their favourite sport
	# 2a. Add the sport into a list

# -------------------------------------------------
# 3. After asking all the student's sport, 
	# Ask the user to enter a sport to check how many students like the sport.

# -------------------------------------------------
# 4. if the sport exist, print out how many people like the sport.
	# e.g. # 3 students like the sport

# -------------------------------------------------
# 5. if the sport does not exist, print out an appropriate message.

# ** Assume that all inputs given are in lower case and valid.
# ** the program will work for any number of students.

ask1 = int(input("How many students are there in the class: ")) # ask will then contain a number
list = []

for i in range(ask1):
    sport = input("what is your favourite sport?: ")
    list.append(sport)
print("Information saved")

counter = 0 
popularity = input("Enter a sport to check the popularity: ")
if popularity in list:
    for sport in list:
        if popularity == sport:
            counter = counter + 1    
    print(f"{popularity} is liked by {counter} student")
else:
    print(f"Nobody likes {popularity}")









































dict1 = {"hamburger": 5, 
         "pasta": 10, 
         "fries": 2}

# add / amend
dict1["hamburger"] = 10

# for key,value in dict1.items():
#     print(key)
#     print(value)

# for key in dict1:
#     print(key) # key
#     print(dict1[key]) # value

def oddoreven(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
