# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 3/27/19
# Python Version 3.7.3
# Look up Coding Colorado

# Importing pkgs
import os
import random

# Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

########################################################## GLOBAL VARIABLES ##############################################################

# Tracks if the program is still running
Is_Running = True

# Stores the User's input
User_Input = ""

# Tracks if the User has made a decision
User_Confirm = False

# Stores what moves the players can choose from for the vanilla game
Choices = ["Rock", "Paper", "Scissors"]

# Stores what moves the players can choose from for the expanded game
Exp_Choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# Stores what the player decides to play
Player_Choice = 0

# Stores what the Computer decides to play
Computer_Choice = 0

# Tracks the score of each player
Player_Score = 0
Computer_Score = 0

############################################################ PROGRAM LOGIC ###############################################################

### Standard Rock Paper Scissors
def Vanilla_Game():

    # Importing global variables
    global User_Input
    global Choices
    global Player_Choice
    global Computer_Choice
    global Player_Score
    global Computer_Score

    # The player chooses what to play
    while User_Confirm == False:

        # Clearing the screen for readability
        cls()

        User_Input = input("Enter '1' for Rock, '2' for Paper, or '3' for scissors: ")

        if str(User_Input) == "1":
            Player_Choice = Choices[0]
            break
        elif str(User_Input) == "2":
            Player_Choice = Choices[1]
            break
        elif str(User_Input) == "3":
            Player_Choice = Choices[2]
            break
        else:
            print("\nPlease enter a valid selection.")

    # Generating the computer's move
    Computer_Choice = Choices[random.randint(0,2)]

    print("\nPlayer: " + Player_Choice + " <--- ---> " + Computer_Choice + " :Computer")

    # Calculating who won the game
    if Player_Choice.upper() == "ROCK" and Computer_Choice.upper() == "SCISSORS":
        print("\nPlayer's Rock crushes the Computer's Scissors!")
        Player_Score = Player_Score + 1
        print("Player's Score: " + Player_Score + "Computer's Score: " + Computer_Score)
    else:
        print("is this the right way to do this?")

    # DEBUG
    # print(Player_Choice)
    # print(Computer_Choice)

    input("\nPress 'enter' to continue.")

### Rock Paper Scissors Lizard Spock
def Expanded_Game():

    # Importing global variables
    global User_Input
    global Choices
    global Player_Choice
    global Computer_Choice
    global Player_Score
    global Computer_Score

    input("\nPress 'enter' to continue.")

############################################################ PROGRAM FLOW ################################################################

while Is_Running == True:

    while User_Confirm == False:

        # Clearing the screen for readability
        cls()

        print("ROCK! PAPER! SCISSORS!")

        User_Input = input("Enter '1' to play standard Rock Paper Scissors\nor enter '2' to play Rock Paper Scissors Lizard Spock: ")

        if str(User_Input) == "1":
            Vanilla_Game()
        elif str(User_Input) == "2":
            Expanded_Game()
        else:
            print("\nPlease enter a valid selection.")
            input("Press 'enter' to continue.")

        