# Task 3
# In cryptography, one of the methods to hide the intended message is to remove all vowels 
# from the message. 

# Open the file CENSORSHIP.py

# 4 Write a function censor(sentence) which replaces all vowels in that sentence 
# with * and returns the censored sentence and vowels that were taken out.

# Sample executions: 
# >>>censor(“Long Live the Queen”)
# “L*ng L*v* th* Q***n”, “oieeuee”

# >>>censor(“It’s a GOOD day!”)
# “*t’s * G**D d*y!”, “IaOOa”
#================================================================
# Long Live the Queen == ["a", "e", "i", "o", "u"]
# L == ["a", "e", "i", "o", "u"]
# newlist = list(sentence)

def censor(sentence):
    introlist = list(sentence)
    vowellist = []
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(sentence)): # L, o, n... 0, 1, 2 ,3
        if introlist[i].lower() in vowels:
            # introlist[i] += "*"
            # then u know this introlist[i] is a vowel
            vowellist.append(introlist[i])
            
            introlist[i] = "*" # i must be a number

    
    return "".join(introlist), "".join(vowellist)       


print(censor("Long Live The Queen"))
print(censor('It’s a GOOD day!'))





# 5 Write a function uncensor(c,v) which takes in a censored sentence and its 
# vowels; and returns the original sentence.

# Sample executions: 
# >>>uncensor(“L*ng L*v* th* Q***n”, “oieeuee”)
# “Long Live the Queen”
# >>>uncensor(“*t’s * G**D d*y!”, “IaOOa”)
# “It’s a GOOD day!”

# You do not need to call the functions. 
# Save the file as MYCENSORSHIP_<your name>_<class>_<index number>.py 

#================================================================
# [11]
# L*ng L*v* th* Q***n


def uncensor(sentence,vowel):
    count = 0
    newlist = list(sentence)
    for i in range(len(sentence)):
        if newlist[i] == "*":
            newlist[i] = vowel[count]
            count += 1
    print(newlist)
    return "".join(newlist)

print(uncensor("L*ng L*v* th* Q***n", "oieeuee"))
print(uncensor('*t’s * G**D d*y!', 'IaOOa'))