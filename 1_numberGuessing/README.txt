Number Guessing Game

V1:
Running the numberGuessing.py will run the number guessing game
where the user has to guess a number between 1 and 100, which will be 
randomly generated by the application, in the minimum number of attempts.

----
V2:
Including the feature to store and compare against the highScore which is maintained
in a highScore.txt file in the same directory. This feature currently works only for 
Unix based OS (because of the '/' based file directory structure).

V2.1:
Making the highScore functionality working for Windows based systems as well. 

----
V3:
Adding a function to select the range of the guessing range between:
1. 1 to 100
2. 1 to 200

V3.1:
Making different highScore.txt file based on the range selected:
1. For 1 to 100 -> highScore1To100.txt
2. For 1 to 200 -> highScore1To200.txt

V3.2:
Correcting userInput function to take valid input only
Correcting the guessesReqd counting

V3.3:
Putting the hardcoded fileNames into functions wherever possible.

V3.4:
Using decorators over the functions for file i/o to avoid redundancy

V3.5:
Solving the highScore.txt not over-writing previous highScore bug
----
Ideas to work on:
[.] The current highScore files are not overwriting the previous scores 
    but are appending to the previous entry. Sort it.
[ ] Error Handling
    [ ] While checking user input at each guess
[ ] User generated Range
[ ] UI of some kind if possible
