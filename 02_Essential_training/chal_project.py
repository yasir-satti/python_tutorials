# Rock paper scissors is a hand game for two or more players. Participants say “rock, paper, scissors” and then simultaneously form their hands into the shape of a rock, a piece of paper, or a pair of scissors. The rules are straightforward:

# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.

# We’d like you to replicate this game using Python! Requirements:

# Allow user to choose Rock, Paper or Scissors
# Allow the computer to randomly generate a response
# Determine who wins the game

# This can be done in any way that is comfortable with you but we would like to see you demonstrate the various concepts learnt through the courses already.

# Bonus points:
# Extend the playability by allowing the user to play several games in a row (user input for how many games to play in a row)
# Improve the readability of the code using Enums and functions
# Add additional features to increase the overall experience of the game.

import random

ROCK = 1
PAPER = 2
SCISSORS = 3


def getUserInput():
     choices = """
     Please select one of the following by typing a number:

     1. Rock
     2. Paper
     3. Scissors
     """
     print(choices)
     userInput = int(input())
     print('user choice ', userInput)
     return userInput


def getSelection(input):
    if input == 1:
        choice = ROCK
    elif input == 2:
        choice = PAPER
    else:
         choice = SCISSORS
    return choice


def getCPUInput():
     cpuChoice = random.randint(1, 3)
     print('cpu choice ', cpuChoice)
     return cpuChoice


def whoIsWinner(userChoice, cpuChoice):
    # Rock smashes scissors.
    # Paper covers rock.
    # Scissors cut paper.
    winner = 'no winner'
    if (userChoice == ROCK) and (cpuChoice == SCISSORS):
         winner = 'user is the winner !'
    elif (userChoice == PAPER) and (cpuChoice == ROCK):
         winner = 'user is the winner !'
    elif (userChoice == SCISSORS) and (cpuChoice == PAPER):
         winner == 'user is the winner !'
    if (cpuChoice == ROCK) and (userChoice == SCISSORS):
         winner = 'cpu is the winner !'
    elif (cpuChoice == PAPER) and (userChoice == ROCK):
         winner = 'cpu is the winner !'
    elif (cpuChoice == SCISSORS) and (userChoice == PAPER):
         winner == 'cpu is the winner !'
    return winner


def playGame():

    userInput = getUserInput()
    usercChoice = getSelection(userInput)
    cpuInput = getCPUInput()
    cpuChoice = getSelection(cpuInput)
    winner = whoIsWinner(usercChoice, cpuChoice)
    print(winner)


playGame()