string concatenation/ string formatting

#1 use print()
age = 15
print("I am", age, "years old.")

#2 use the plus +
sentence = "I am " + str(age) + " years old." #age is integer, need to convert to str()
print(sentence1)

#3 use the .format()
sentence2 = "I am {} years old".fromat(age)
print(sentence2)

#4 use the f-string
sentence3 = f"I am {age} years old."
print(sentence3)




########################################## HOW TO USE len()
nums = [2334,576,7,5345,346,546,2345,3464,6765678,32423425536]

#len() # returns how many items are inside
print(len(nums))

# len() works on list, strings, dictionary
# len() on list >> returns count of items inside the list
# len() on string >> returns the count of characters in the string
# len() dictionary >> return the count of key/ value pairs in dictionary






###################################################
#### WHY DO YOU USE len(listnums) ??????
listnums = [10,20,30,40,50,60,70]
print(len(listnums)) # 7

print("-------------------------------")
# hardcoded value
for i in range(7):
    print( listnums[i])

print("-------------------------------")
# better way is to use len(listnums) so that if you change the list, it will still be correct
for i in range(len(listnums)):
    print( listnums[i])

print("-------------------------------")
#### CONTRAST THE ABOVE with the normal way to loop through a list
for num in listnums:
    print(num)