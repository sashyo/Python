# Import the random integer function
from random import randint

# Initialise a variable for the user's score
score = 0

# Ask the user to guess several numbers and keep score
for guess in range(5): # how many guesses to allow
    computers_num = randint(0, 9) # choose the computer's random number
    print("I'm thinking of a number between 0 and 9 ... What is it? ", end = "") # prompt the user
    users_response = eval(input()) # read and evaluate the user's response
    if computers_num == users_response: # test if the two numbers are equal
        print("You're right!")
        score = score + 1
    else:
        print("Sorry, but that's not it.")

# Print the final score, being careful to use correct grammar for
# singular versus plural numbers of wins
if score == 1:
    print("Your final score was 1 point.")
else:
    print("Your final score was", score, "points.")
