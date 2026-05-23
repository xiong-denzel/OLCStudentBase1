# ============================================================
# Movie Ticket Booking System
# Total: 25 marks
# ============================================================

"""
A cinema is creating a simple ticket booking system for one movie hall.

The movie hall has 5 rows of seats:
A, B, C, D and E

Each row has 20 seats, numbered from 01 to 20.

A valid seat code has exactly 3 characters.

Examples of valid seat codes:
A01
A12
B05
E20

Examples of invalid seat codes:
F01     # invalid row
A00     # invalid seat number
C21     # invalid seat number
A1      # invalid format
AA1     # invalid format
B05X    # invalid length

Each movie ticket costs $12.

The cinema staff will enter bookings for different customers.

For each customer, the program should:
1. Ask for the customer's name.
2. Ask for the number of tickets the customer wants to book.
3. Ask for and validate the seat code for each ticket.
4. Store the customer's booking.
5. Display all current customer bookings.

The program should keep asking for new customer bookings 
until the user choose to stop entering names.

After the user choose to stop, the program should display a daily summary showing:
1. Each customer's name.
2. The amount paid by each customer.
3. The total payment received for the day.

You are not required to use functions for this question.
"""
overall_booked_seats = ["A01","A02","A03"] # list containing all seats booked across all customers
customer_booked_seats = [] # list to store specific customer seats
current_bookings = {"ALI":["A01","A02","A03"]} # dictionary containing all customers and their bookings

# ============================================================
# Task 1: Ask for customer names repeatedly
# [3 marks]
# ============================================================

"""
Write Python code to repeatedly ask the user to enter a customer's name.

- The customer name must not be blank.
- The customer name should be stored in uppercase.

If the user enters a blank name, display a suitable error message and ask
for the customer name again.

After a valid customer name is entered, the program should continue to
Task 2 for that customer.
"""

# Write your code for Task 1 below
# while True:
#     askname = input("Enter customer's name: ")
#     if askname != "":
#         askname = askname.upper()
#         print(askname)
#         break
#     else:
#         print("Error\nEnter customer name again")
#         continue
    


# ============================================================
# Task 2: Ask for the number of tickets
# [3 marks]
# ============================================================

"""
For each customer, ask for the number of tickets the customer wants to book.

- The number of tickets must be a whole number from 1 to 5 inclusive.
- If the input is invalid, display a suitable error message and ask again.
- The program should only continue to Task 3 after a valid number of tickets
  has been entered.
"""
# Copy and paste your code from previous task


# while True:
#     askname = input("Enter customer's name: ")
#     if askname != "":
#         askname = askname.upper()
#         print(askname)
#         break
#     else:
#         print("Error\nEnter customer name again")
#         continue

# Write your code for Task 2 below
# check if between 1 to 5  >>> > 0 and less < 6
# check if its a number >>> .isdigit()

# while True:
#     askticket = input("Enter the amount of ticket you wish to purchase: ")
#     if askticket.isdigit() == False:
#         print("You must enter a number")
#     elif int(askticket) < 1 or int(askticket) > 5:
#         print("You must enter between 1-5 only")
#     else:
#         print(f"You bought {askticket} tickets")
#         break


# ============================================================
# Task 3: Ask for and validate seat codes
# [9 marks]
# ============================================================

"""
For each customer, ask the user to enter one valid seat code for each ticket.

For example, if the customer wants to book 3 tickets, the program should
accept exactly 3 valid seat codes for that customer.

Each seat code entered should be converted to uppercase.

A valid seat code must satisfy all of the following conditions:

1. It has exactly 3 characters.
2. The first character is one of the row letters:
   A, B, C, D or E.
3. The last two characters are digits.
4. The seat number is from 1 to 20 inclusive.
5. The seat has not already been been booked.

If the seat code is invalid, display a suitable error message and ask for
another seat code.

If the seat code is valid, store it as an item in the list customer_booked_seats and overall_booked_seats.
The row must be stored in upper case

The program should only continue to Task 4 after the current customer has
successfully selected all required seats.
"""

# Write your code for Task 3 below

# This variable contains all booked seats across different customers.
# overall_booked_seats = ["A01","A02","A03"] # list containing all seats booked across all customers
# customer_booked_seats = [] # list to store specific customer seats
# current_bookings = {"ALI":["A01","A02","A03"]} # dictionary containing all customers and their bookings

# while True:
#     askname = input("Enter customer's name: ")
#     if askname != "":
#         askname = askname.upper()
#         print(askname)
#         break
#     else:
#         print("Error\nEnter customer name again")
#         continue

# # Write your code for Task 2 below
# # check if between 1 to 5  >>> > 0 and less < 6
# # check if its a number >>> .isdigit()

# while True:
#     askticket = input("Enter the amount of ticket you wish to purchase: ")
#     if askticket.isdigit() == False:
#         print("You must enter a number")
#     elif int(askticket) < 1 or int(askticket) > 5:
#         print("You must enter between 1-5 only")
#     else:
#         print(f"You bought {askticket} tickets")
#         break



# # A20 
# # askseat[-2:] >>> 20
# # is 20 < 1? or 20 > 20?
# # dictionary = {"key":"value", "key2":"value2"}
# for i in range(int(askticket)):
#     while True:
#         askseat = input("Enter your desired seat: ")
#         askseat = askseat.upper()
#         if len(askseat) != 3:
#             print("Error. It has to have exactly 3 characters.")
#         elif askseat[0] not in "A,B,C,D,E": # why didnt this condition stop
#             print("Error - Must start with A,B,C,D,E")
#         elif askseat[-2:].isdigit() == False: # problem here... 
#             print("Error - last 2 must be numbers")
#         elif int(askseat[-2:]) < 1 or int(askseat[-2:]) > 20:
#             print("Error. The seat number is from 1 to 20 inclusive.")
#         elif askseat in overall_booked_seats:
#             print("Error. The seat has already been been booked.")
#         else:
#             customer_booked_seats.append(askseat)
#             overall_booked_seats.append(askseat)
#             break
# print(customer_booked_seats)
# print(overall_booked_seats)



# ============================================================
# Task 4: Store and display all current bookings
# [4 marks]
# ============================================================

"""
After the current customer has selected all required seats, store the customer's
booking in the current_bookings dictionary.
The key is the customer name, and the value is the the customer_booked_seats list

After storing the current customer's booking, display all current customer
bookings.

Example output:

Current Bookings
----------------
ALI : ['A01', 'A02']
MEI : ['B10']
RAVI : ['C05', 'C06', 'C07']

After displaying the current bookings, the program should ask for the next
customer's name.

Ask the user if there are any more customers to process.
"""

# Write your code for Task 4 below

overall_booked_seats = ["A01","A02","A03"] # list containing all seats booked across all customers
customer_booked_seats = [] # list to store specific customer seats
current_bookings = {"ALI":["A01","A02","A03"]} # dictionary containing all customers and their bookings

# while True:

#     while True:
#         askname = input("Enter customer's name: ")
#         if askname != "":
#             askname = askname.upper()
#             print(askname)
#             break
#         else:
#             print("Error\nEnter customer name again")
#             continue

#     # Write your code for Task 2 below
#     # check if between 1 to 5  >>> > 0 and less < 6
#     # check if its a number >>> .isdigit()

#     while True:
#         askticket = input("Enter the amount of ticket you wish to purchase: ")
#         if askticket.isdigit() == False:
#             print("You must enter a number")
#         elif int(askticket) < 1 or int(askticket) > 5:
#             print("You must enter between 1-5 only")
#         else:
#             print(f"You bought {askticket} tickets")
#             break

#     # A20 
#     # askseat[-2:] >>> 20
#     # is 20 < 1? or 20 > 20?
#     # dictionary = {"key":"value", "key2":"value2"}
#     for i in range(int(askticket)):
#         while True:
#             askseat = input("Enter your desired seat: ")
#             askseat = askseat.upper()
#             if len(askseat) != 3:
#                 print("Error. It has to have exactly 3 characters.")
#             elif askseat[0] not in "A,B,C,D,E": # why didnt this condition stop
#                 print("Error - Must start with A,B,C,D,E")
#             elif askseat[-2:].isdigit() == False: # problem here... 
#                 print("Error - last 2 must be numbers")
#             elif int(askseat[-2:]) < 1 or int(askseat[-2:]) > 20:
#                 print("Error. The seat number is from 1 to 20 inclusive.")
#             elif askseat in overall_booked_seats:
#                 print("Error. The seat has already been been booked.")
#             else:
#                 customer_booked_seats.append(askseat)
#                 overall_booked_seats.append(askseat)
#                 break
#     print(customer_booked_seats)
#     print(overall_booked_seats)

#     current_bookings[askname] = customer_booked_seats
#     print(current_bookings)

#     ask = input("is there are any more customers to process?(Y/N): ").upper()
#     if ask != "Y":
#         break






# ============================================================
# Task 5: Display the daily payment summary
# [4 marks]
# ============================================================

"""
After the user choose to stop entering more customer names

The summary should show:

1. Each customer's name.
2. The amount paid by each customer.
3. The total payment received for the day.

The amount paid by each customer is calculated using the number of seats
booked by that customer.

Example output:

Daily Summary
-------------
ALI paid $24
MEI paid $12
RAVI paid $36

Total payment received: $72
"""

# Write your code for Task 5 below

# for i in current_bookings:  
current_bookings = {'ALI': ['A01', 'A02', 'A03'], 'DEN': ['A06', 'A07', 'A08', 'B06', 'B07', 'B08']}
overall_booked_seats = ["A01","A02","A03",'A06', 'A07', 'A08', 'B06', 'B07', 'B08']
for name in current_bookings:
    tickets = current_bookings[name]
    customertotal = len(tickets) * 12
    print(f"{name} paid a total of {customertotal}")
print(f"the total payment received for the day is {len(overall_booked_seats) * 12}")




# ============================================================
# Quality of Program
# [2 marks]
# ============================================================

"""
Award up to 2 marks for:

1. Meaningful variable names.
2. Clear comments where appropriate.
3. Code that is neat, readable and properly indented.
"""


# ============================================================
# End of Question
# ============================================================

