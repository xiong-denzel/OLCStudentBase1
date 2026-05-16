# The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is shown below. The pattern repeats from there, with 2012 being another year of the dragon, and 1999 being another year of the hare.
# Write a function called zodiac() that takes in a year as an input argument and returns the animal associated with that year.
# Your program should work correctly for any year greater than or equal to zero, not just the ones listed below.

# Year          Animal
# 2000          dragon
# 2001          snake
# 2002          horse
# 2003          sheep
# 2004          monkey
# 2005          rooster
# 2006          dog
# 2007          boar
# 2008          rat
# 2009          ox
# 2010          tiger
# 2011          hare


def zodiac(years):
    animals = ["dragon", "snake", "horse", "sheep", "monkey", "rooster", "dog", "boar", "rat", "ox", "tiger", "hare"]
    year = (years - 2000) % 12
    return animals[year]



#================================================================
# Task 3
# A program is written for a two-player word-guessing game.
# At the start of the game, the word length is displayed for the players in the form of a string
# i.e. “********”  The number of asterisks will show the length of the secret word.

# In the game, each player takes turn to either
# 1) guess a letter in the secret word OR
# 2) guess the secret word directly

# You can initialise and assign “PARADISE” as the secret word and assume that all user
# inputs will be in uppercase.

# The game will continue indefinitely until one of the player correctly guesses the secret
# word. If any of the player correctly guesses a letter in the secret word, the function is
# required to display the correct letter. A prompt message is required if the character or
# word entered by the player is incorrect.

# Write a program which will prompt the two players to guess a character or the
# secret word each time and provide the feedback to the players when the program
# is run. The program should display a congratulatory message as shown if any
# player guesses the secret word correctly and end immediately.
# Save the file as MYWORDGUESS_<your name>_<class>_<index number>.py


##=======================================================================================
# secret = "PARADISE"
# turn = "1" # Player 1 and Player 2
# display_string = ["*"] * len(secret)

# print("Guess the following word ")
# print("".join(display_string)) # converts the list items into a string

# while True: 
#     print(f"Player {turn} - Enter: ")
#     print("1: guess a character")
#     print("2: guess the word")
#     choice = input("")

#     if choice == "2": # if player guess the whole word
#         player_guess = input("Guess the word: ").upper()
#         if player_guess == secret:
#             print("Congrats! You have gotten it correct!")
#             break
#         else:
#             print("Sorry. Your guess is not correct. Try again.")
#     elif choice == "1": # player guess a single character
#         player_guess = input("Guess a character:: ").upper()
#         # check if the letter exist in the secret
#         if player_guess in secret:

#             for i in range(len(secret)):    # P A R A D I S E
#                 if secret[i] == player_guess:
#                     display_string[i] = player_guess

#             print("".join(display_string))
#             if "*" not in display_string:
#                 print("Congrats! You have gotten it correct!")
#                 break
#         else:
#             print("Sorry. Your character is not in the word")
#     else:
#         print("Only option 1 or 2 only.")

#     if turn == "1":
#         turn = 2
#     else: 
#         turn = 1




# Write a word guessing program like hangman
# assume secret word
# keep guessing until all the letters are found 

# display *, display the character
#  player_guess = input("Guess a character:: ").upper()
#         # check if the letter exist in the secret
#         if player_guess in secret:

#             for i in range(len(secret)):    # P A R A D I S E
#                 if secret[i] == player_guess:
#                     display_string[i] = player_guess

#             print("".join(display_string))
#             if "*" not in display_string:
#                 print("Congrats! You have gotten it correct!")
#                 break
#         else:
#             print("Sorry. Your character is not in the word")

secret_word = "why"
## this part needs to be repeated
while True:
    new_word = ""
    print("Welcome to HANGMAN\nCHOOSE EITHER ONE\n1: GUESS A CHARACTER\n2: GUESS A WORD")
    choose = input()
    if choose == "1":
        cguess = input("Enter character:")
        for i in range(len(secret_word)):
            if secret_word[i] == cguess:
                new_word += cguess
            else:
                new_word += "*"
        print(new_word)


# Write a word guessing program like hangman
# assume secret word
# keep guessing until all the letters are found 




