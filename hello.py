# Write a function called contain_three() that will take in four 2-digit integers as input arguments.

# The function should return the number of times "3" appears in the input arguments.


# Answer
# Type your function below #
def contain_three(a, b, c, d):
    str_input = str(a) + str(b) + str(c) + str(d)
    count_three = 0
    for letter in str_input:
        if letter == "3":
            count_three += 1

    return count_three

for i in range(2, 32, 2): # 2 - 29 # start, stop, step
    print(i)

word = "SINGAPORE"

print(word[3:6])