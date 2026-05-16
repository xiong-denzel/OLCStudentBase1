# create a new list, containing a proper name 
# names = ["kevin", "lionel","mary","benny"]   

name = "lionel"
# using string slicing, output Kevin (capitalised)
newname = name[0].upper() + name[1:]
print(newname)

firstname = "kevin"
lastname = "obama"

# generate a user name
# take first 3 characters of firstname, and last 3 characters of lastname + random 3 digit number

import random
r = random.randint(100,999)
username = firstname[0:4] + lastname[-3:] + str(r)
print(username)









'''
# Challenge 1:
Write a function `validate_nric(nric: str) -> bool` to 
validate if a given input is a valid Singapore NRIC number. 
A valid NRIC must start with 'S', 'T', 'F', or 'G', followed by 7 digits, 
and ends with an uppercase letter.

* In this case, assume that as long as the last character 
is an uppercase letter it is valid.

Normal Test: Input: "S1234567D", Output: True
Error Test: Input: "A1234567D", Output: False
Boundary Test: Input: "S123456", Output: False
'''

# if X not true
# elif Y not true
# elif Z not true
# else, True

# T1234567H

def validate_nric(nric):
    start = ["S","T","F","G"]    
    if nric[0] not in start:
        return False
    elif not nric[1:8].isdigit():
        return False
    elif not nric[-1].isalpha():
        return False
    else:
        return True



print(validate_nric("A1234567L"))
print(validate_nric("S1234567L"))
print(validate_nric("11234567L"))
print(validate_nric("S1567L"))