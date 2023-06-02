from chal_py_beginner_rock_paper_scr import getUserInput, getCPUInput, getSelection, whoIsWinner

import random

ROCK = 1
PAPER = 2
SCISSORS = 3


def test_user_selects_rock():
    userInput = 1
    userChoice = getSelection(userInput)
    assert userChoice == ROCK


def test_user_selects_paper():
    userInput = 2
    userChoice = getSelection(userInput)
    assert userChoice == PAPER


def test_user_selects_scissors():
    userInput = 3
    userChoice = getSelection(userInput)
    assert userChoice == SCISSORS


def test_cpu_selects():
    choices = {1: 1, 2: 2, 3: 3}
    cpuInput = getCPUInput()
    cpuChoice = getSelection(cpuInput)
    assert cpuChoice == choices[cpuInput]