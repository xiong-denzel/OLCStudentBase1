# print("")

# import random
# random.randint(1,100)


# int()
# float()
# append()

# input()

# def hello():
#     print("Hello, how are you?")

# hello()

# def greet(yourname, myname):
#     print(f"Hello {yourname}, how are you? ")
#     print(f"My name is {myname}")
# greet("Denzel" , "Den")

def area_rectangle(length,breadth):
    area = length * breadth 
    return area 
rect1 = area_rectangle(65, 89)
rect2 = area_rectangle(75, 12)
rect3 = area_rectangle(4, 75)
rect4 = area_rectangle(78, 36)
rect5 = area_rectangle(14, 89)
total = rect1 + rect2 + rect3 + rect4 + rect5
print(total)


# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.


# Test the function with multiple operations.
# print(calculator(10, 5, "+"))
# print(calculator(10, 5, "-"))
# print(calculator(10, 5, "*"))
# print(calculator(10, 5, "/"))

def calculator(number1, number2, op):
    if op == "+":
        output = num1 + num2
    elif op == "-":
        output = num1 - num2 
    elif op == "*":
        output = num1 * num2
    elif op == "/":
        output = num1 / num2
    
    # minus = num1 - num2
    # return minus
    # multiply = num1 * num2
    # return multiply
    # divide = num1 / num2 
    # return divide

    return output

num1 = int(input("input first number: "))
num2 = int(input("input second number: "))
operation = input("Enter operation (+, -, *, /): ")
answer = calculator(num1, num2, operation)
print(f"{num1} {operation} {num2} = {answer}")








