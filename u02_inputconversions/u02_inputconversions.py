# name = input("what is your name: ")
# hobby = input('what is your hobby: ')

# sentence = f"{name} likes {hobby}"
 
 
# print(sentence)

# num1 = int(input('enter number 1: '))
# num2 = int(input('enter number 2: '))

# answer = num1 + num2
# print(answer)


# Exercise 8: Area of a Circle with .format()
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result using .format(). Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."

radius = float(input("what is the radius of a circle: "))

answer = 3.14 * radius * radius 

print("The area of the circle with the radius of {} is {}" .format(radius, answer))
