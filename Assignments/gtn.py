# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

low = 0
high = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, max_attempts, attempts, low, high
    attempts = 0  
    secret_number = random.randrange(low, high - 1)
    max_attempts = math.ceil(math.log((high - low + 1), 2))
    print ""
    print "Welcome! Let's play the game now."
    print "You have", int(max_attempts), "guesses!"
    print ""


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global high
    high = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global high
    high = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    # incerment attempts to track the number of guesses
    global attempts
    attempts += 1 
    
    input_number = int(guess)
    print "Guess was", input_number
    
    #check if guess is lower of higher tham secret_number
    if secret_number == input_number:
        print "Correct"
        print "Game will be restarted now."
        print ""
        
        new_game()
       
    elif secret_number < input_number:
        print "Higher"
    else:
        print "Lower"
    print "Remaining guesses :", int(max_attempts) - attempts
    print ""
    
    #check if number of guesses crossed maximum attempts allowed
    if attempts >= max_attempts:
        print "You lost! You have crossed maximum number of guesses allowed"
        print "Game will be restarted now."
        new_game()
        
    
    
# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)
frame.add_input('Enter your guess here:', input_guess, 150)
frame.add_button('Range: 0 - 100', range100, 150)
frame.add_button('Range: 0 - 1000', range1000, 150)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
