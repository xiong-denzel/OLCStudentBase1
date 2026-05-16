
###################################################
# Part 1: Learning Exercises

# Exercise 1: Using .find()
# Write a program to find the position of the first occurrence 
# of "Python" in a string using .find().
text = "I love Python programming."
position = text.find("Python")  # Find the position
# print("The position of 'Python' is: {}".format(position))




#------------------------------------------------------------
# Exercise 2: Using .index()
# Write a program to find the position of the first occurrence 
# of "Python" in a string using .index().
text = "I love Python programming."
position = text.index("Python")  # Find the position
# print("The position of 'Python' is: {}".format(position))




#------------------------------------------------------------
# Exercise 3: Finding Substring Without .find() or .index()
# Write a program to find the position of "Python" manually 
# without using .find() or .index().
text = "I love Python programming."
substring = "Python"
position = -1  # Default value for "not found"

# Iterate through the string, checking each substring of 
# the same length as "Python".
for i in range(len(text) - len(substring) + 1):
    # Extract a slice of the text with the same length as the 
    # substring
    current_slice = text[i:i + len(substring)]
    # Compare the slice with the substring
    if current_slice == substring:
        position = i  # Record the position
        break  # Exit the loop once found
# print("The position of 'Python' is: {}".format(position))



# Exercise 4: Splitting a String Using .split()
# Write a program to split a sentence into words using .split().
sentence = "Python is fun to learn."
words = sentence.split()  # Split by whitespace
# print("Words in the sentence: {}".format(words))




#------------------------------------------------------------
# Exercise 5: Splitting a String Without .split()
# Write a program to manually split a sentence into words 
# without using .split().
sentence = "Python is fun to learn."
words = []  # Initialize an empty list to store words
word = ""   # Temporary variable to build words
for char in sentence:
    if char == " ":  # Space indicates the end of a word
        words.append(word)  # Add the word to the list
        word = ""  # Reset for the next word
    else:
        word += char  # Build the word character by character
if word:  # Add the last word if it exists
    words.append(word)
# print("Words in the sentence: {}".format(words))






#------------------------------------------------------------
# Exercise 6: Finding Position in a List Using .index()
# Write a program to find the position of an element in a list 
# using .index().
numbers = [10, 20, 30, 40, 50]
position = numbers.index(30)  # Find the position of 30
# print("The position of 30 is: {}".format(position))






#------------------------------------------------------------
# Exercise 7: Finding Position in a List Without .index()
# Write a program to find the position of an element in a list 
# manually without using .index().
numbers = [10, 20, 30, 40, 50]
target = 30
position = -1  # Default value for "not found"

# Iterate through the list to find the target
for i in range(len(numbers)):
    if numbers[i] == target:
        position = i  # Record the position
        break  # Exit the loop once found
# print("The position of 30 is: {}".format(position))





#------------------------------------------------------------






###########################################################
# Part 2. IN-CLASS Practice Exercises
# Exercise 8: Case-Insensitive Substring Search
# Scenario: Searching for "python" in a string, ignoring case.
text = "I love PYTHON programming."

# print(text.lower().index("jython"))   # returns error if cannot find

# print(text.lower().find("python"))   # returns -1






#------------------------------------------------------------
# Exercise 9: Multiple Occurrences of Substring
# Scenario: Count how many times "Python" appears in a string.
text = "Python is great. Python is easy to learn. Python is fun!"

# for i in 50:
textlist = text.split(" ")  
count = 0
for i in textlist:   # got problem
    if i == "Python":
        count += 1
print(count)





#------------------------------------------------------------
# Exercise 10: Manual List Splitting
# Scenario: A list of comma-separated numbers is given, and you 
# need to split it into individual elements without using .split().
# data = "10,20,30,40,50"
countries = "malaysia,singapore,thailand,indonesia,myanmar"
country_list = []
tempword = ""
for i in countries:
    if i != ",":
        tempword += i
    else:
        country_list.append(tempword)
        tempword = ""
country_list.append(tempword)
print(country_list)

# loop through each character
# build the word

# once detect ",", add word to list, clear word

#=========================================================
# Scenario 2: Extracting URLs from a Web Log
# You are a web analyst at a large company handling 
# log files from multiple servers. Your task is to extract URLs 
# from a comma-separated web traffic log into a list for further analysis.

# expected output
# ['https://shopnow.com', 'https://newsdaily.com', 'https://techinsider.org', ... ]
weblogs = "https://shopnow.com,https://newsdaily.com,https://techinsider.org,https://myblog.net,https://travelhub.io,https://educonnect.edu,https://cryptoexchange.com,https://gamingworld.gg,https://sportsupdates.tv,https://moviemagic.net,https://musicstream.fm,https://fitnessclub.org,https://foodiesdelight.com,https://financeguru.biz,https://shoppinghub.co,https://bookreviews.xyz,https://jobportal.jobs,https://weatherwatcher.gov,https://luxuryhomes.realestate,https://carenthusiast.auto"


# write your code here

weblogslist = []
tempstr = ""
for i in weblogs:
    if i != ",":
        tempstr += i
    else:
        weblogslist.append(tempstr)
        tempstr = ""
weblogslist.append(tempstr)
print(weblogslist)





########################################################

# Scenario 4: Extracting Stock Prices for Market Analysis
# You are working for a stock exchange where hourly stock prices 
# for nVidia are recorded in a colon-separated string. 
# Your task is to extract all hourly stock prices 
# into a list of floats for further calculations.

# expected output
# [154.2, 158.7, 160.1, 163.4]

stockprice = "154.2:158.7:162.9:160.1:163.4:165.8:159.5:161.2:167.3:162.0:169.4:172.5:171.8:168.2:166.0:175.4:177.9:180.2:178.6:182.1:185.3:190.5:188.2:191.0:193.5:195.8:199.1:200.7:202.3:198.9"

# write your code here
stockpricelist = []
tempstr = ""
for i in stockprice:
    if i != ":":
        tempstr += i
    else:
        stockpricelist.append(tempstr)
        tempstr = ""
stockpricelist.append(tempstr)
print(stockpricelist)