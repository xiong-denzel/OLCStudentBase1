# Python List Exercises: Student Names and Scores
#
# Scenario:
# You have 2 separate lists.
# One list stores student names.
# The other list stores the corresponding scores.
#
# The score at each index belongs to the student name at the same index.
#
# Example:
# names[0] matches scores[0]
# names[1] matches scores[1]
#
# Use the sample lists below for the questions.

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

# # retrieve first value from names list
# print(names[0])

# # how to add a new item to the list? "Joseph"
# names.append("Joseph") # adds to the back
# print(names)

# # .insert() # insert at a specific position
# names.insert(2, "new number 3")
# print(names)

# # delete from the list 

# #.remove() # you know the value to delete
# names.remove("Joseph")
# print(names)


# # del # when you know the position / index
# del names[0]
# print(names)

# # check for existence, if "Edward" is in the class
# if "Victor" in names:
#     print("Victor exists")    

# # loop through a list
# for i in names:
#     print(i)




# --------------------------------------------------
# PART 1: Basic list access and membership
# --------------------------------------------------

# Q1
# Print the full names list using a for loop.

# Q2
# Print the full scores list using a for loop.
# for i in scores:
#     print(i)    



# Q3
# Print the first student name in the list.
# print(names[0])

# # Q4
# # Print the last score in the list.
# print(scores[-1])

# # Q5
# # Find out whether "Charlie" exists in the names list.
# # Print True or False.
# if "Charlie" in names:
#     print(True)


# # Q6
# # Ask the user to enter a student name.
# # Check whether that student exists in the names list.
# # Print "Student found" or "Student not found".
# ask = input("Enter name: ")
# if ask in names:
#     print("Student found")
# else:
#     print("Student not found")



# --------------------------------------------------
# PART 2: Finding positions and matching data
# --------------------------------------------------

# Q7
# Find the index position of "Daphne" in the names list.
# Print the index.
# names.index("Daphne")
# print(names.index("Daphne"))

# # Q8
# # Find Charlie's score by first finding Charlie's index in the names list.
# # Then use that same index to get the score from the scores list.
# p = names.index("Charlie")
# print(scores[p])

# print(scores[p],  "is", qs, "score")


# Q9
# Ask the user to enter a student name.
# If the student exists, print that student's score.
# If not, print "Student not found".
# ask = input("Enter your name")
# if ask in names:
#     i = names.index(ask)
#     print(f"{scores[i]} is {ask} score")
# else:
#     print("Student not found")
    
# Q10
# Print every student's name together with their score.
# Example output:
# Aiden : 78
# Bella : 92
# Charlie : 85
# for a in names:
#     i = names.index(a)
#     score = (scores[i])
# for b in scores

# 4 ways of formatting, concatenation

#1 - print way
# age = 15
# print("I am", age,"years old.")





# for i in range(len(names)):
#     current_name = names[i]
#     current_score = scores[i]

#     print(f"{current_name} : {current_score}")

# print(f"{names[0]} : {scores[0]} ")
# print(f"{names[1]} : {scores[1]} ")
# print(f"{names[2]} : {scores[2]} ")
# print(f"{names[3]} : {scores[3]} ")
# print(f"{names[4]} : {scores[4]} ")


# --------------------------------------------------
# PART 3: Working with highest and lowest values
# --------------------------------------------------

# Q11
# Find the highest score in the scores list.
# Print the highest score only.
highest = max(scores)
print(highest)

# Q12
# Find the lowest score in the scores list.
# Print the lowest score only.
lowest = min(scores)
print(lowest)
# Q13
# Find the name of the student who scored the highest mark.
# Assume there is only one highest scorer for now.
n = scores.index(highest)
print(names[n])


# Q14
# Find the name of the student who scored the lowest mark.
# Assume there is only one lowest scorer for now.
a = scores.index(lowest)
print(names[a])
# Q15
# Print a sentence like this:
# "Bella scored the highest mark of 92."
print(f"Bela scored the highest mark of {highest}")

# --------------------------------------------------
# PART 4: Handling ties
# --------------------------------------------------

# Q16
# In the current list, there are 2 students with the highest score.
# Find the highest score first.
# Then print all student names who got that highest score.

maxscore = max(scores)
max_students = []
for i in range(len(names)):
    if scores[i] == maxscore:
        max_students.append(names[i])
print(max_students)
# Q17
# Print the result in this format:
# "Top scorer(s): Lydia, Samuel with 95 marks."

# Q18
# Find all students who got the lowest score.
# Print their names and the score.
min_nums = min(scores)

print(len(scores))

for i in range(len(scores)):
    if scores[i] == min_nums:
        print(names[i])
 # Q19
# Count how many students got the highest score.
# Print the number.
maxscore = max(scores)
max_students = []
for i in range(len(names)):
    if scores[i] == maxscore:
        max_students.append(names[i])
print(f" {len(max_students)} is the number of students who got the highest score" )
# Q20
# Count how many students scored above 80.
maxscore = 80
max_students = []
for i in range(len(names)):
    if scores[i] > maxscore:
        max_students.append(names[i])
print(f" {len(max_students)} is the number of students who got the highest score" )

# --------------------------------------------------
# PART 5: Searching and filtering
# --------------------------------------------------

# Q21
# Create a new list that stores the names of students who scored above 80.
# Print the new list using a for loop.

# Q22
# Create a new list that stores the names of students who failed.
# Assume fail means score below 50.
# Print the new list using a for loop.
failures = []
for i in range(len(names)):
    if scores[i] < 50:
        failures.append(names[i])
print(failures)
# Q23
# Create a new list that stores the scores of students whose names start with the letter "B" or "D".

# Q24
# Ask the user to enter a min_score and a max_score
# Print all student names who are within the range of the min and max score. (inclusive)
mini = int(input("enter minimum score")) ## min() is a function
maxi = int(input("enter maximum score"))
for i in range(len(scores)): # i is the position
    if scores[i] < maxi and scores[i] > mini:
        print(names[i])
# Q25
# Ask the user to enter a student name.
# Print whether the student passed or failed.
# Assume pass mark is 50.


# --------------------------------------------------
# PART 6: Ranking-style questions
# --------------------------------------------------

# Q26
# Find the top 3 highest scores only.
# Print the 3 scores.

# Q27
# Find the names of the top 3 highest scorers together with their scores.
# Example output:
# Lydia : 95
# Samuel : 95
# Yvonne : 94

# Q28
# Print the top 3 highest scorers in ranking format.
# Example:
# 1. Lydia : 95
# 2. Samuel : 95
# 3. Yvonne : 94

# Q29
# Handle ties properly.
# If 2 students share the highest score, both should appear before the next lower score.

# Q30
# Find the 2nd highest score in the list.
# Then print all students who got that 2nd highest score.

# Q31
# Find the 3rd highest unique score in the list.
# Then print all students who got that score.


# --------------------------------------------------
# PART 7: Data changes and updates
# --------------------------------------------------

# Q32
# Add a new student name "Elena" into the names list.
# Add her score 93 into the scores list.
# Then print both updated lists.

# Q33
# Ask the user to enter a new student name and score.
# Add both into the correct lists.

# Q34
# Change Ethan's score to 74.
# Print the updated scores list.

# Q35
# Remove "Grace" from the names list.
# Also remove her matching score from the scores list.

# Q36
# Ask the user for a student name.
# If the student exists, remove that student and the matching score.
# If not, print "Student not found".


# --------------------------------------------------
# PART 8: Slightly more advanced list logic
# --------------------------------------------------

# Q37
# Calculate the average score of all students.
# Print the average.

# Q38
# Find out how many students scored above the average.

# Q39
# Print the names of students who scored above the average.

# Q40
# Find the difference between the highest score and the lowest score.

# Q41
# Sort the scores from highest to lowest.
# Print the sorted scores only.



# --------------------------------------------------
# CHALLENGE QUESTIONS
# --------------------------------------------------

# Q42
# Create a new list of grades based on the scores.
# Use this grading system:
# 75 and above = A
# 65 to 74 = B
# 50 to 64 = C
# below 50 = F
# Print each student's name, score, and grade.

# Q43
# Find all students who got grade A.

# Q44
# Print the class leaderboard from highest to lowest.
# Include ranking number, student name, score, and grade.

# Q45
# If a student name appears more than once in the names list,
# print a warning message saying "Duplicate student name found".
