#---1---Create a Python script to generate a guessing number game, allowing the user a
# limited number of guesses, using input from user and randint function, and will not work
# on Wednesdays

#-----------------------------------#
# Solutions
#-----------------------------------#

import random
import datetime

GUESSESALLOWED = 7

def Guesses () :
    n = random . randint (1 , 99)
    guesses = 0
    while guesses < GUESSESALLOWED :
        guess = int( input (" Enter an integer 1 to 99: " ))
        if guess < 1 or guess > 99:
            print ( " That ’s an illegal guess . Try again !" )
        elif guess == n:
            print ( " Congratulations ! You took " , \
                        guesses + 1, " guesses ! " )
            return
        elif guess < n:
            print ( " Guess is too low . Try again !" )
        else :
            print ( " Guess is too high . Try again !" )

        guesses += 1

    print ( " Whoops ! You took too many guesses ." , \
            " The answer was " , n )

Today=datetime.date.today()

if Today.strftime("%a")=='Mon':
    Guesses()
else:
    print("The game will not working today")










