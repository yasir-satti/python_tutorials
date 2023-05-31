from chal_project import getUserInput, getCPUInput, getSelection, whoIsWinner

import random

ROCK = 1
PAPER = 2
SCISSORS = 3


def test_user_selects_rock():
    userInput = 1
    userChoice = getSelection(userInput)
    assert userChoice == ROCK