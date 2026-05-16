###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# number of elements.
numbers = [10, 20, 30, 40, 50, 60, 70]





#------------------------------------------------------------

# Exercise 8: Checking Palindrome in a String
# Scenario: Determine if a string is a palindrome (reads the same 
# backward as forward).
# word = 
word = "singapore"
if word == word[::-1]:
    print("it is a palindrome")
else:
    print("no")
# how to reverse a string
# [start: stop: step]
# [::-1]


# if a string, is the same as the string (reverse) then its a palindrome



# hannah, racecar, level 




#------------------------------------------------------------

# Exercise 9: Reversing Words in a Sentence
# Scenario: Reverse the words in a sentence manually.
# sentence = "Python is fun to learn."
# sentence = "a a a a a a a a a"

# learn to fun is Python

# splits a string using the separator, and stores into a list
  # reversing the list
# listword = sentence.split(" ")
# print(listword[::-1])
# print(listword)

# pull out each whole word into a list
# flip the list




'''
# Question 9: Extract the first three characters from a string
# Test case 1: example input: hello, example output: hel
# Test case 2: example input: Python, example output: Pyt
'''
## Write and test your code here
strings = "hello"
print(strings[0:3])

    

'''
# Question 10: Extract the last three characters from a string
# Test case 1: example input: hello, example output: llo
# Test case 2: example input: Python, example output: hon
'''
## Write and test your code here
strings2 = "hello"
print(strings2[-3:])



'''
# Challenge 4:
Write a function `is_valid_postal_code(postal_code: str) returns bool` 
to validate a Singaporean postal code. A valid postal code consists 
of exactly 6 digits where the first digit must be between 1 and 7.

Normal Test: Input: "123456", Output: True
Error Test: Input: "823456", Output: False
Boundary Test: Input: "12345", Output: False
'''
#------------------------------------------------------
def is_valid_postal_code(postal_code):
    
    # if len(postal_code) == 6:   
    #     if int(postal_code[0]) >= 1 and int(postal_code[0]) <= 7:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False

    if len(postal_code) != 6:
        return False   
    elif not( int(postal_code[0]) >= 1 and int(postal_code[0]) <= 7):
        return False
    else:
        return True

print(is_valid_postal_code("123456")) # True
print(is_valid_postal_code("123")) # False
print(is_valid_postal_code("823456")) # False
print(is_valid_postal_code("723456")) # True
print(is_valid_postal_code("12345678")) # False