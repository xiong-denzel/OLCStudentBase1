# planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]

# print(planets[2])

# planets[3] = "Denzelland"
# print(planets)

# del planets[6]
# print(planets)

# planets.remove("mercury")
# print(planets)

# planets.append("jiajieland")
# print(planets)

# count = len(planets)
# print(count)

# for i in planets:
#     print(f"Someday i would like to visit {i}")

# names = []
# for i in range(5):
#     ask = input("WHAT IS YOUR NAME?: ")
#     names.append(ask)

# for i in names:
#     print(f"Hello, {i}")
# for every item in this list




###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 9: Summing Numbers in a List
# Write a program to calculate the sum of numbers in a list.
# list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
#          5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
#          1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
#          756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
#          2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
#          6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
#          6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
#          4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
#          5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
#          4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# maxnum = list1[0]

# for i in list1:
#    if i > maxnum:
#         maxnum = i
# print (maxnum)

# minnum = list1[0]
# for i in list1:
#     if i < minnum:
#         minnum = i 
# print (minnum)
##### find the average of this list of numbers

#### find the biggest number in this list

#### find the smallest number in this list


#### find the total of all the numbers
# total = sum(list1) #

# total = 0
# # list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040]
# for i in list1:

#     total = total + i
#     # numbers = len(list1)
#     # print(numbers)   
#     # print(f"{i}*{numbers}")

# print(total)






'''
Question 12: Write a function that takes a list of numbers and 
returns a new list with the square of each number.
example input:
[1, 2, 3, 4, 5]
expected output:
[1, 4, 9, 16, 25]
'''
# Write your code here
# list1 = [1, 2, 3, 4, 5]
# list2 = []
# for num in list1:
#     print(num)
#     sq2 = num ** 2
#     list2.append(sq2)
# print(list2)





'''
Question 13: Given a list of words, create a new list of words 
that are longer than 3 characters.
example input:
['tree', 'car', 'house', 'sun', 'computer']
expected output:
['tree', 'house', 'computer']
'''
# Write your code here
words = ['tree', 'car', 'house', 'sun', 'computer']
words2 = []
for char in words:
    print(char)
    if len(char) > 3:
        words2.append(char)
print(words2) 

# for loop
# check how long is the word len()
# append() to new list


'''
Question 14: Write a function that takes a list of numbers and 
returns the sum of the even numbers in the list.
example input:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expected output:
30
'''
# Write your code here
def sumeven(listnum):
    total = 0
    for num in listnum:
        if num % 2 == 0:
            total = total + num # the variable total is equals to the value of total + X
            # total += num
    return total
print(sumeven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

            



########################################################
'''
# Exercise 15: Create a List
# Add the following numbers into a list using a for loop
# Example output: [1, 2, 3, 4, 5, 6, 7, 8]
'''
# Write your code here


'''
# Exercise 16: Access List Elements
# Print the first and last element of a given list.
# Example input: numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected output: 1 8
'''
# Write your code here
numbers = [100, 200, 300, 400, 500, 600, 700, 800]
var1 = numbers[-3:] #[start:stop:increment]
print(var1)

#slicing works on strings and list
firstname = "johnathon"
lastname = "tang"

# create a user name. use first 3 characters from firstname and last 3 characters from last name
username = firstname[:3] + lastname[-3:]

# 30 Tampines Street 32

# replace 32 with 31
streetname = "30 Tampines Street 32"


# replace 32 with 31
streetname = "30 Tampines Street 32"

#option 1
newstreet = streetname.replace("32", "31") # searching for a value, replace with something else 
# print(newstreet)

# option 2
pos_new = streetname.find("32") # find() the position of 32 in the string
new_streetname = streetname[:19]+"31"
print(new_streetname)

# John created a variable john_address to store his address. 
# But instead of storing the correct address of "1 Tampines St 32", 
# he wrongly assigned the string "1 Tampines St 30". 
# He tried using the following code to correct it but keeps getting an error message.

# john_address = "1 Tampines St 30"
# john_address[-1] = '2'

# # construct the string from the start, and omit the last character
# new_address = john_address[:-2]

# # >>> john_address = "1 Tampines St 30"
# # >>> john_address[-1] = '2'
# # Traceback (most recent call last):
# #   File "<pyshell#4>", line 1, in <module>
# #     john_address[-1] = '2'
# # TypeError: 'str' object does not support item assignment


# Edit the program so that the username is created using the
#  first three letters of the first name, along with the last name.

# firstname = input("Please enter your first name: ")
# lastname = input("Please enter your last name: ")
# username = firstname[:3] + lastname
# print("Your username is " + username)
# password = input("Please enter a password: ")


'''
# Exercise 17: List Length
# Find and print the length of a given list.
# Example input: numbers = [1, 2, 3, 4, 5]
# Expected output: 5
'''
# Write your code here

'''
# Exercise 18: Combine Two Lists
# Combine two lists into one and print the result.
# Example input: list1 = [1, 2, 3], list2 = [4, 5, 6]
# Expected output: [1, 2, 3, 4, 5, 6]
'''
# Write your code here

'''
# Exercise 19: Check if an Element is in a List
# Check if the number 3 is in the given list and print the result.
# Example input: numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected output: True
'''
# Write your code here


'''
# Exercise 20: Minimum and Maximum in a List
# Find and print the minimum and maximum value in a given list.
# Example input: numbers = [2, 3, 1, 4, 5]
# Expected output: 1 5
'''
# Write your code here


'''
# Exercise 21: Sum of List Elements
# Calculate and print the sum of all elements in a given list.
# Example input: numbers = [1, 2, 3, 4, 5]
# Expected output: 15
'''
# Write your code here
numbers = [1, 2, 3, 4, 5]
print("before XXXXXX")
print(sum(numbers))

total = 0 #sum()
for num in numbers:
    total += num
print(total)

print("after XXXXXX")
print(sum(numbers))    #15(numbers)

# sum, int float list str
# if got questions: david.lee@computhink.com.sg
# cannot hear you, you are breaking up 

'''
# Exercise 22: Average of List Elements
# Calculate and print the average of all elements in a given list.
# Example input: numbers = [1, 2, 3, 4, 5]
# Expected output: 3.0
'''
# Write your code here


'''
# Exercise 23: List Slicing
# Print the first three elements of a given list.
# Example input: numbers = [1, 2, 3, 4, 5]
# Expected output: [1, 2, 3]
'''
# Write your code here


'''
# Exercise 24: List Indexing
# Print the index of the element 10 in a given list.
# Example input: numbers = [1, 23, 90, 54, 34, 10, 23, 43]
# Expected output: 5
'''
# Write your code here


'''
# Exercise 25: List of Strings
# Create a list of strings and print each element on a 
# new line using a for loop
# Example input: fruits = ['apple', 'banana', 'cherry', 'orange']
# Expected output:
# apple
# banana
# cherry
# orange
'''
# Write your code here


















# string variable
# integer, float
# boolean >> True False
# List
###################################################
# Part 1: Learning Exercises

# Exercise 1: Accessing List Elements by Index
# Write a program to access and print the first, second, and last 
# elements of a list using indexing.

# fruits = ["apple", "orange", "banana","durian"] # my list
# print(fruits[2]) # retrieve a specific value from the list



# #------------------------------------------------------------
# # Exercise 2: Adding Elements to a List
# # Write a program to add an element to the end of a list using 
# # append(), and add another element at a specific index using 
# # insert().


# fruits.append("durian") # add a new item to the list, adds at the back

# fruits.insert(1, "grapes") # add at specific position





# #------------------------------------------------------------
# # Exercise 3: Using del() to Remove an Element by Index
# # Write a program to delete an element at a specific index.
# # Example: Remove the second color.

# del(fruits[1]) # deleting by the index



# #------------------------------------------------------------
# # Exercise 4: Using remove() to Remove an Element by Value
# # Write a program to remove a specific element by its value.
# # Example: Remove "green" from the list.
# # colors = ["red", "green", "blue", "yellow"]
# # colors.remove("green")  # Remove by value
# # print("Colors after removal: {}".format(colors))

# # fruits.remove("durian")

# # while True:
# #     if "durian" in fruits:
# #         fruits.remove("durian")
# #     else:
# #         break



# #------------------------------------------------------------
# # Exercise 5: Using pop() to Remove and Retrieve an Element
# # Write a program to remove the last element of a list using pop().
# # Example: Remove and print the last color.
# # colors = ["red", "green", "blue", "yellow"]
# # removed_color = colors.pop()  # Remove the last element
# # print("Removed color: {}".format(removed_color))
# # print("Colors after pop: {}".format(colors))

# lastfruit = fruits.pop() # removes last one and assign to variable
# print(fruits)




# #------------------------------------------------------------
# # Exercise 6: Modifying Elements in a List
# # Write a program to change the second element in a list to "pink."
# # colors = ["red", "green", "blue"]
# # colors[1] = "pink"  # Modify value at index 1
# # print("Modified colors: {}".format(colors))
# print(lastfruit)
# fruits[3] = "spikyfruit" # change the value
# print(fruits)

# #------------------------------------------------------------
# # Exercise 7: Membership Check
# # Write a program to check if "blue" is in the list.
# # colors = ["red", "green", "blue"]
# # if "blue" in colors:
# #     print("Blue is in the list.")
# # else:
# #     print("Blue is not in the list.")

# # validation check - existence check
# checkfruit = input("Enter a fruit name: ")
# if checkfruit in fruits:
#     print(f"{checkfruit} is in the list")
# else:
#     print(f"{checkfruit} is not in the list")

# #------------------------------------------------------------

# ##### to loop through every single item
# for i in fruits:
#     print(i)

# for i in range(5): 
