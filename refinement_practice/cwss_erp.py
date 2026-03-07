
# Task 2 
# In Singapore, electronic road pricing (ERP) is implemented 
# on various expressways to regulate traffic. 
# 
# Lately there has been a change in the ERP rates at 5 gantries across some expressways. 

# The following program calculates the change in rates of these 5 gantries. 

# for i in range(5): 
#     expressway = input("Enter name of gantry:") 
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old 
#     print("Change is",change) 


###########################################################
# 6. Edit the program so that: 
# a)	It works for any number of gantries. 
#       The program must display a suitable input message. [1] 
###########################################################
# Copy + Paste & Write your code here
# num_gan = int(input("Enter number of gantries: "))
# for i in range(num_gan): 
#     expressway = input("Enter name of gantry:") 
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old 
#     print("Change is",change) 



###########################################################
# b)	The name of gantry is accepted if it is made up of only 
#       letters and is of a maximum length of 20. 
#       A suitable error message must be displayed and the program 
#       must loop until the name of the gantry is an input of a maximum of 20 letters. [4] 
###########################################################
# Copy + Paste & Write your code here
# num_gan = int(input("Enter number of gantries: "))
# for i in range(num_gan): 
#     while True:
#         expressway = input("Enter name of gantry:") 
#         if not expressway.isalpha():
#             print("Enter letters only")
#         elif len(expressway) > 20:
#             print("Enter a max of 20 letters")
#         else:
#             break
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old 
#     print("Change is",change) 



###########################################################
# c)	The name of each gantry for which the ERP rate has 
#       been increased is stored in a list and then displayed. [4] 
###########################################################
# Copy + Paste & Write your code here
# num_gan = int(input("Enter number of gantries: "))
# list_incr = []
# for i in range(num_gan): 
#     while True:
#         expressway = input("Enter name of gantry:") 
#         if not expressway.isalpha():
#             print("Enter letters only")
#         elif len(expressway) > 20:
#             print("Enter a max of 20 letters")
#         else:
#             break
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old
#     if change > 0:
#         list_incr.append(expressway)
#     print("Change is",change) 
# if len(list_incr) > 0 :
#     print(list_incr)



###########################################################
# d)	The total number of gantries which saw an increase 
#       in the ERP rate is displayed. [1] 
###########################################################
# Copy + Paste & Write your code here
num_gan = int(input("Enter number of gantries: "))
list_incr = []
for i in range(num_gan): 
    while True:
        expressway = input("Enter name of gantry:") 
        if not expressway.isalpha():
            print("Enter letters only")
        elif len(expressway) > 20:
            print("Enter a max of 20 letters")
        else:
            break
    old = float(input("Enter old rate:")) 
    new = float(input("Enter new rate:")) 
    change = new - old
    if change > 0:
        list_incr.append(expressway)
    print("Change is",change) 
if len(list_incr) > 0 :
    print(list_incr)
print(f"{len(list_incr)} is the total number of gantries which saw an increase")

print(len(list_incr), "is the total number of gantries which saw an increase")

print("{} is the total number of gantries which saw an increase".format(len(list_incr)))

print( str(len(list_incr)) +  "is the total number of gantries which saw an increase")














################### DONE QUESTION BELOW ###################################



# Task 2 
# In Singapore, electronic road pricing (ERP) is implemented 
# on various expressways to regulate traffic. 
# 
# Lately there has been a change in the ERP rates at 5 gantries across some expressways. 

# The following program calculates the change in rates of these 5 gantries. 

# for i in range(5): 
#     expressway = input("Enter name of gantry:") 
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old 
#     print("Change is",change) 


###########################################################
# 6. Edit the program so that: 
# a)	It works for any number of gantries. 
#       The program must display a suitable input message. [1] 
###########################################################
# Copy + Paste & Write your code here
# num_gan = int(input("Enter the number of gantries: "))
# for i in range(num_gan): 
#     expressway = input("Enter name of gantry:") 
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old 
#     print("Change is",change) 



###########################################################
# b)	The name of gantry is accepted if it is made up of only 
#       letters and is of a maximum length of 20. 
#       A suitable error message must be displayed and the program 
#       must loop until the name of the gantry is an input of a maximum of 20 letters. [4] 
###########################################################
# Copy + Paste & Write your code here

# how to detect only letter?
# .isalpha()

# how to know if it is not more than 20 letters?
# len()

# num_gan = int(input("Enter the number of gantries: "))
# for i in range(num_gan): 
#     while True:    
#         expressway = input("Enter name of gantry:") 
#         if not expressway.isalpha():
#             print("Enter only letters")
#         elif len(expressway) > 20:
#             print("Enter a maximum of 20 letters")
#         else:
#             break
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old 
#     print("Change is",change) 



###########################################################
# c)	The name of each gantry for which the ERP rate has 
#       been increased is stored in a list and then displayed. [4] 
###########################################################
# Copy + Paste & Write your code here
# num_gan = int(input("Enter the number of gantries: "))
# list_incr = []
# for i in range(num_gan): 
#     while True:    
#         expressway = input("Enter name of gantry:") 
#         if not expressway.isalpha():
#             print("Enter only letters")
#         elif len(expressway) > 20:
#             print("Enter a maximum of 20 letters")
#         else:
#             break
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old
#     if change > 0:
#         list_incr.append(expressway)
#     print("Change is",change)

# # check if anything is in the list, then print
# if len(list_incr) > 0:   
#     print(list_incr)



###########################################################
# d)	The total number of gantries which saw an increase 
#       in the ERP rate is displayed. [1] 
###########################################################
# Copy + Paste & Write your code here
# num_gan = int(input("Enter the number of gantries: "))
# list_incr = []
# for i in range(num_gan): 
#     while True:    
#         expressway = input("Enter name of gantry:") 
#         if not expressway.isalpha():
#             print("Enter only letters")
#         elif len(expressway) > 20:
#             print("Enter a maximum of 20 letters")
#         else:
#             break
#     old = float(input("Enter old rate:")) 
#     new = float(input("Enter new rate:")) 
#     change = new - old
#     if change > 0:
#         list_incr.append(expressway)
#     print("Change is",change)

# # check if anything is in the list, then print
# if len(list_incr) > 0:   
#     print(list_incr) 

# print(f"{len(list_incr)} gantries increased in price" )