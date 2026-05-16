# # Write a function called contain_three() that will take in four 2-digit integers as input arguments.

# # The function should return the number of times "3" appears in the input arguments.


# # Answer
# # Type your function below #
# def contain_three(a, b, c, d):
#     str_input = str(a) + str(b) + str(c) + str(d)
#     count_three = 0
#     for letter in str_input:
#         if letter == "3":
#             count_three += 1

#     return count_three

# for i in range(2, 32, 2): # 2 - 29 # start, stop, step
#     print(i)

# word = "SINGAPORE"

# print(word[3:6])


# Repeat Task 3 WITHOUT using any If-elif-else statements.

# Insert one line of code that will meet the problem

# ----------------------------------------------------------------------------------------------------------------------------------------

# Task 4 
# Write a function called odd_integer() that will take in 5 integers as input arguments.

# The function should return the number of odd integers.

# ----------------------------------------------------------------------------------------------------------------------------------------

# Copy and continue using the following template:

# def odd_integer(a, b, c, d, e):

# Task 3
# Write a function called odd_integer() that will take in 5 integers as input arguments.

# The function should return the number of odd integers.

def odd_integer(a,b,c,d,e):
    num_list = [a, b, c, d, e]
    counter = 0
    for num in num_list:
        if num % 2 != 0:
            counter += 1
    return counter

# # Type in your answer for the code following #
# def odd_integer(a,b,c,d,e):
#     num_list = [a, b, c, d, e]
#     counter = 0
#     for num in num_list:
#         if num % 2 != 0:
#             counter += 1
#     return counter
# Write a function called odd_integer() that will take in 5 integers as input arguments.

# The function should return the number of odd integers.

# Write a function named number_chain() that will take in 2 integers as inputs. 
# The function should return one whole string of all numbers (inclusive of upper and lower limit) 
# in the range specified by the inputs.

# For example, number_chain(11,15) will return "1112131415".

def number_chain(num1, num2):
    numstr = ""
    for i in range(num1, num2 + 1):
        numstr = numstr + str(i)
    return numstr

print(number_chain(11,15))

# range(11, 15) # >>> 11, 12, 13, 14

# "SINGAPOREMALAYSIATHAILAND"[11:15]  # slicing

# Write a function dna_rna(arg) which transcribes a given DNA strand 
# into corresponding mRNA - a type of RNA, that will be formed from it after transcription. 
# DNA has the bases A, T, G and C, while RNA converts to U, A, C and G respectively.

# dna_rna("ATGC") ➞ "UACG"
# dna_rna("ATTAGCGCGATATACGCGTAC") ➞ "UAAUCGCGCUAUAUGCGCAUG"

# in the function, you need to loop through all characters
    # if the character is A > U
    # if the character is T > A
    # if the character is G > C
    # if the character is C > G

# use a list, with UACG >> 

# dna_rna("ATTAGCGCGATATACGCGTAC") # ➞ "UAAUCGCGCUAUAUGCGCAUG"

### 

# dna = ["A", "T", "G", "C"]

# pos = dna.index("A") # returns 0

def dna_rna(dna_string):
    output = ""
    placeholder = ""
    for i in dna_string:
        if i == "A":
            placeholder = "U"
        elif i == "T":
            placeholder = "A"
        elif i == "G":
            placeholder = "C"
        elif i == "C":
            placeholder = "G"
        output += placeholder
    return output



print(dna_rna("ATTAGCGCGATATACGCGTAC"))

# Create a function longest(h,m,s) that takes three values: 
# hour, minutes and seconds. Return the value that is the longest duration. 
# (Each duration input will be distinct)

# longest(1, 59, 3598) ➞ 1

def longest(h,m,s):
    h = h * 60 * 60
    m = m * 60
    if h > m and h > s:
        return int(h / (60*60))
    elif m > h and m > s:
        return int(m / 60)
    else:
        return s
    # if h1 > m1 and h1 > s1, then h1 is biggest

    # elif m1 > h1 and m1 > s1, then m1 is biggest

    # else
print(longest(1, 61, 87000))
# 1.0 

# Write a function seq() which accepts a string and 
# returns True if the string is sequential, else, False. 

# Consider case sensitivity. 
# the string argument will always have at least 2 characters.
# seq("abcd") #➞ True
# seq("abcD") #➞ False
# seq("1234") #➞ True
# seq("1245") #➞ False

# s = "abcd"
# i = 2
# s[i] # c
# s[i+1] # d

def seq(letter_string):

    # loop through every single letter, using index
    for i in range(len(letter_string)):

        #a b c d
        # checks if it is the end of string, i break
        if i == len(letter_string)-1:
            break

        # 
        if ord(letter_string[i+1]) - ord(letter_string[i]) != 1:
            return False
    # after looping through everything successfully, it must be true
    return True



######################### 
def odd_integer(a,b,c,d,e):
    num_list = [a, b, c, d, e]
    counter = 0

    for num in num_list:
        counter += num % 2 == 1
        # if num % 2 != 0:
        #     counter += 1
    return counter

print(odd_integer(1,2,3,4,5))

# A bowling game consists of 10 frames. Each frame has 10 pins to hit and the player has up to 2 throws to hit and fell all 10 pins. The score for each frame is based on the number of pins fell for that frame, except for spares or strikes. 

# Spares "/" occurs when the player fells all remaining pins in the second throw. The score of this frame will add scores from the next one frame. 

# Strikes "><" occur when the player fells all 10 pins in the first throw. The score of this frame will add scores from the next two frames.

# Should a spare or strike occur at the 10th frame, an additional one or two frames will be added respectively after it, so that scores for the 10th frame can be determined. 

# Write a function score() which takes in a string parameter and returns the total scores of the bowling game. 

# Sample execution: 

# score("-/-/9/1/7/3/4/5/6/5/-") >>> 140
# score("><2/158/1023><><5/7/-") >>> 126
# score("18181818181818181818") >>> 90
# score("--------------------") >>> 0
# score("><><><><><><><><><><><><") >>> 300
# All digits in the score represent the number of pins fell. A dash "-" indicates that the bowling ball went into the gutter at the sides of the lane. "-" indicates that 0 pins fell and should represent a 0 score. 






# one of the first known examples of encryption was used by Julius Caesar. 
# Caesar needed to provide written instructions to his generals but he didn’t 
# want his enemies to learn his plans if the message slipped into their hands. 
# As a result, he developed what later became known as the Caesar Cipher.

# The idea behind this cipher is simple (and as a result, it provides no protection 
# against modern code breaking techniques).

# 1) Each letter in the original message is shifted by 3 places. As a result,
# A becomes D, B becomes E, C becomes F, D becomes G, etc.

# 2) The last three letters in the alphabet are wrapped around to the beginning.
#  X becomes A. Y becomes B and Z becomes C.

# 3) Non-letter characters are not modified by the cipher.

# 4) Your function only needs to handle lowercase letters, so convert 
# the text to lowercase at the start of your function.

# Write a function named encode_caesar() that implements a Caesar Cipher. 
# Your function should take in the message in the form of a string input and return the encrypted message. 


alphabets = "abcdefghijklmnopqrstuvwxyz"
shift = 3
def encode_caesar(message):
    message = message.lower()
        output_string = ""

            #loop through every single character in the message
                for c in message:
                        if c in alphabets:
                                    # find the current position e.g. a = 0, b = 1
                                                c_pos = alphabets.find(c)
                                                            # the position + shift
                                                                        shifted_pos = (c_pos + shift) % 26
                                                                                    #find the letter in the new shifted position 
                                                                                                encrypted_letter = alphabets[shifted_pos]
                                                                                                            # add to the output string
                                                                                                                        output_string += encrypted_letter
                                                                                                                                else:
                                                                                                                                            output_string += c # if not lowercase alphabet
                                                                                                                                                return output_string
print(encode_caesar("xxxx"))

# Expression	Expected	
# encode_caesar("Time to attack!")

# "wlph wr dwwdfn!"

# encode_caesar("RED ALERT!! Strengthen defence!")

# "uhg dohuw!! vwuhqjwkhq ghihqfh!"
