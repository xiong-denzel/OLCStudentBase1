# How to define a dictionary
# menu = {"hamburger": 6.50, "spaghetti": 12.00, "soup": 7.50}

# # retrieve a value from dictionary
# ham_price = menu["hamburger"]
# print(ham_price)
# print(menu)

# # change the value of a key
# menu["spaghetti"] = 20.9
# print(menu)

# ### add a new item to dictionary
# menu["lasagne"] = 30.8
# print(menu)

# ## delete an item from dictionary
# del menu["soup"]
# print(menu)

# # loop through dictionary
# for food_name in menu: #food_name == key
#     print(food_name)
#     print(f"{food_name}: ${food_price}")
# ### to ask customer what they want to eat?


# need to check if i sell the item


### ask for a key and value and add it to dictionary


# add to dictionary???

names = [
    "Aiden", "Bella", "Charlie", "Daphne", "Ethan", "Fiona", "Grace", "Henry",
    "Isaac", "Jasmine", "Kai", "Lydia", "Mason", "Nora", "Owen", "Priya",
    "Quentin", "Rachel", "Samuel", "Tina", "Uma", "Victor", "Wendy", "Xavier",
    "Yvonne", "Zach", "Aaron", "Bianca", "Caleb", "Denise"
]

scores = [
    78, 92, 45, 92, 67, 88, 58, 81,
    90, 73, 84, 95, 69, 87, 58, 91,
    76, 83, 95, 32, 72, 89, 77, 68,
    94, 80, 58, 86, 24, 79
]

##### find the maximum score in the list


##### find who scored the maximum

new = {}
for i in range(len(scores)):
    ss = names[i]
    sc = scores[i]
    new[ss] = sc
# print(new) 
     
    

# # add a new record, "LeeLing" 95
# new["LeeLing"] = 95
# print(new) 
# new["Uma"] = 88
# print(new) 


# --------------------------------------------------
# PART 3: Working with highest and lowest values
# --------------------------------------------------

# Q11
# Find the highest score in the the dictionary
# Print the highest score only.
# maxi = max(scores) # int 99

# i = scores.index(maxi)
# print(names[i])
# highest = 0

# for name,score in new.items():
#     if score > highest:
#         highest = score

# print(highest)


# for key,value in new.items():
#     if value > highest:


# Q12
# Find the lowest score in the scores dictionary
# Print the lowest score only.
# lowest = 100
# for name,score in new.items():
#     if score < lowest:
#         lowest = score
# print(lowest)
# Q13
# Find the name of the student who scored the highest mark.
# Assume there is only one highest scorer for now.
print(new)
highest = 0
highestname = ""
for name,score in new.items():
    if score > highest:
        # print(score)
        highest = score
        highestname = name
# print(highestname,highest)
# Q14
# Find the name of the student who scored the lowest mark.
# Assume there is only one lowest scorer for now.
lowest = 1000
lowestname = ""
for name,score in new.items():
    if score < lowest:
        lowest = score
        lowestname = name
# print(lowest,lowestname)


#### print out the list of name and students who fail. < 50
for name,score in new.items():
    if score < 50:
        print(f" {name} scored a {score} and failed")

# Given a list of numbers, write a function find all its elements that are 
# greater than their left neighbor. Return the result as a String. 

# Note: examine the test cases in this question very carefully to know what is required in the output. 


#your code here
def greater(a):
    nums = ""
    # start, stop, step 
    for i in range(len(a)-1, -1, -1):
        print(i)
        if i != 0: # need to stop left most number
            if a[i] > a[i-1]: # check whether bigger than left number
                nums = nums + str(a[i]) # concatenate
    # print(nums)
    # return None
    return nums
#DO NOT delete test cases:    
a = [1,5,2,4,3]
b = [1,3,5,7,9]
c = [-1, -2, -3, -4, -5]

print(greater(a))
print(greater(b))
print(greater(c))
