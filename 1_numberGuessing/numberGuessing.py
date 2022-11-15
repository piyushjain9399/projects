#! /usr/bin/env python3

# Idea ->   A number guessing python app that generates a random number from 1 to 100 
#           and asks the user to guess the generated number in minimum number of attempts.
#           After each attempt user is told if the number to be guessed is smaller than or 
#           greater than his/her/their guess.

# Flow ->   1. Generating a random number.
#           2. Taking inputs from user continually, telling user if ans is greater than 
#               or less then their guess and storing the number of attempts the user is making.
#           3. Once the user guesses the number, print out the number of attempts taken.

# 0. Importing reqd libraries.
import random

# 1. Generating random number
def generateRandom():
    """
    Function to generate and return a random integer from 1 to 100
    """
    randNum = random.randint(1,100)
    return randNum

# Taking input from user
def getInput():
    """
    Function to take guess int input from user
    """
    guess = int(input("Make a guess between 1 to 100: "))
    return guess

# Defining the main function and writing the call for it.
def main():
    """
    The driver function.
    """
    guessReqd = 0
    guess = 0
    ans = generateRandom()
    while (guess != ans):
        guess = getInput()
        if guess == ans:
            break
        elif guess < ans:
            print("The correct ans is greater than your guess.")
        else:
            print("The correct ans is smaller than your guess.")
        guessReqd += 1
    print("You've guessed the correct number which is:", ans)
    print(f"You took %{guessReqd} guesses.")

if __name__ == "__main__":
    main()
