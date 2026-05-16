encoded_message = "helloworld5" #4 should be a string #5. no "ed"

if encoded_message[:-1].islower(): 
    message_length = int(encoded_message[-1]) #1. added underscore #5. change 1 to -1
    actual_message = encoded_message[:message_length] #2. same as no.1
    print(actual_message) #Output should be "hello"
else:
    print("The encoded message contains characters otherthan lowercase English letters.") #3. used ' instead of ""


## backup of original code
# encod message = helloworld5
# if encoded message[:-1].islower():
#     message length =int(encoded message[1])
#     actual message = encoded message[:message length]
#     print(actual_message) #Output should be "hello"
# else:
#     print("The encoded message contains characters otherthan lowercase English letters.')