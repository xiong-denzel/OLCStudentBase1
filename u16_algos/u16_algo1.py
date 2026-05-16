# check for palindrome algorithm
word = "hannah"
reversed = word[::-1] # how to reverse a word
print(reversed)
# if word = word[::-1]:
if word == reversed:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")