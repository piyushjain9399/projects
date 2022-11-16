#! /usr/bin/env python3

# Idea ->   A number guessing python app that generates a random number from 1 to 100 
#           and asks the user to guess the generated number in minimum number of attempts.
#           After each attempt user is told if the number to be guessed is smaller than or 
#           greater than his/her/their guess.

# Flow ->   1. Generating a random number.
#           2. Taking inputs from user continually, telling user if ans is greater than 
#               or less then their guess and storing the number of attempts the user is making.
#           3. Once the user guesses the number, print out the number of attempts taken.


# V2    ->  Adding the feature to store high scores. (Only for Unix based systems) 
#           i.e. writing the high score to a file stored in the same directory and updating the score
#           if the current score beats the high score.

# V2.1  ->  Adding the highScore functionality to Windows based systems.


# V3    ->  Adding a function to select the range of the guessing range between:
#           1. 1 to 100
#           2. 1 to 200

# V3.1  ->  Making different highScore.txt file based on the range selected:
#           1. For 1 to 100 -> highScore1To100.txt
#           2. For 1 to 200 -> highScore1To200.txt


# V3.2  ->  1. Correcting userInput function to take valid input only.
#           2. Correcting the counting of guesses. 


# 0. Importing reqd libraries.
import random
import os
from sys import platform

# 1. Generating random number
def generateRandom(choice):
    """
    Function to generate and return a random integer from 1-100 and 1-200
    based on the user range input
    """
    if choice==1:
        randNum = random.randint(1,100)
    else:
        randNum = random.randint(1,200)
    return randNum

# Taking input from user
def getInput(choice):
    """
    Function to take guess int input from user based on the range choice
    made by the user
    """
    if choice == 1:
        guess = int(input("Make a guess between 1 to 100: "))
        if (guess>100 or guess<1):
            print("Please make a choice between 1 to 100 only. Try again!")
            guess = getInput(choice)
    else:
        guess = int(input("Make a guess between 1 to 200: "))
        if (guess>200 or guess<1):
            print("Please make a choice between 1 to 200 only. Try again!")
            guess = getInput(choice)
    return guess

# Function to check if highScore.txt file exists
def checkHighScoreFile(choice):
    """
    Checks the pre-existence of highScore.txt file in the same directory
    """
    path = os.getcwd()
    if platform == "win32" or platform == "win64":
        path += "\\highScore"
    else:
        path += "/highScore"
    if choice == 1:
        path += "1To100.txt"
    else:
        path += "1To200.txt"
    isFile = os.path.isfile(path)
    return isFile

# V3 Change: Getting range choice from the user:
def getRange():
    """
    Function to take the range choice between 1-100 and 1-200 from the user
    """
    choice = int(input("Please input 1 if range choice is 1-100 and 2 if range choice is 1-200:"))
    while (choice != 1 and choice != 2):
        print("Please input 1 or 2 only. Try again.")
        choice = getRange()
    return choice

# Defining the main function and writing the call for it.
def main():
    """
    The driver function.
    """
    choice = getRange()
    guessReqd = 0
    guess = 0
    ans = generateRandom(choice)
    while (guess != ans):
        guess = getInput(choice)
        if guess == ans:
            break
        elif guess < ans:
            print("The correct ans is greater than your guess.")
        else:
            print("The correct ans is smaller than your guess.")
        guessReqd += 1
    print("You've guessed the correct number which is:", ans)
    # Increasing the guessReqd to compensate for the last correct guess which is not counted.
    guessReqd += 1
    print(f"You took {guessReqd} guesses.")
    
    highScoreFileExists = checkHighScoreFile(choice)

    if highScoreFileExists:
        # Checking if user score beats current score:
        if choice == 1:
            file1 = open(r"highScore1To100.txt", "r")
        else:
            file1 = open(r"highScore1To200.txt", "r")
        highScore = int(file1.read())
        
        # Updating the highScore.txt with the better highScore.
        if guessReqd < highScore:
            file1.close()
            if choice == 1:
                file1 = open(r"highScore1To100.txt", "w")
            else:
                file1 = open(r"highScore1To200.txt", "w")
            file1.write(str(guessReqd))
            print(f"Congratulations! You have set up a new highScore with {guessReqd} guesses")

        else:
            print("The highscore is:", highScore)
    else:
        # Making the highScore file with correct filename based on the range:
        if choice == 1:
            file1 = open(r"highScore1To100.txt", "w")
        else:
            file1 = open(r"highScore1To200.txt", "w")
        file1.write(str(guessReqd))
        print("Congratulations! You have set up a new highScore!")

if __name__ == "__main__":
    main()
