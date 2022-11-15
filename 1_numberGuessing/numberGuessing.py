#! /usr/bin/env python3

# Idea -> A number guessing python app that generates a random number from 1 to 100 and asks the user to guess the generated number in minimum number of attempts.

# Flow ->   1. Generating a random number.
#           2. Taking inputs from user continually and storing the number of attempts the user is making.
#           3. Once the user guesses the number, print out the number of attempts taken.

# 0. Importing reqd libraries.
import random

def generateRandom():
    """
    Function to generate and return a random integer from 1 to 100
    """
    randNum = random.randInt(1,100)
    return randNum

def getInput():
    """
    Function to take guess int input from user
    """
    guess = int(input("Make a guess between 1 to 100: "))
    return guess
