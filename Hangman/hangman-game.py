import random

fail = 0
guess = " "
gameOver = 6
max_turn = 12
i = 0

library = ["soccer", "football", "rugby" ]
word = random.choice(library)
#print(word)

def gameProgress(fails):
    if fail == 0:
        print("   __________ ")
        print("  | /         ")
        print("  |/          ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("__|__________ \n")

     


        

    elif fail == 1:
        print("   __________ ")
        print("  | /    |    ")
        print("  |/          ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("__|__________ \n")

    elif fail == 2:
        print("   __________ ")
        print("  | /    |    ")
        print("  |/     O   ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("__|__________ \n")

    elif fail == 3:
        print("   __________ ")
        print("  | /    |    ")
        print("  |/     O    ")
        print("  |      |    ")
        print("  |           ")
        print("  |           ")
        print("  |           ")
        print("__|__________ ")

    elif fail == 4:
        print("   __________ ")
        print("  | /    |    ")
        print("  |/     O    ")
        print("  |      |    ")
        print("  |      |    ")
        print("  |           ")
        print("  |           ")
        print("__|__________ \n")

    elif fail == 5:
        print("   __________ ")
        print("  | /    |    ")
        print("  |/     O    ")
        print("  |      |\   ")
        print("  |      |    ")
        print("  |           ")
        print("  |           ")
        print("__|__________ \n")

    elif fail == 5:
        print("   __________ ")
        print("  | /    |    ")
        print("  |/     O    ")
        print("  |     /|\   ")
        print("  |      |    ")
        print("  |           ")
        print("  |           ")
        print("__|__________ \n")

    elif fail == 6:
        print("   __________ ")
        print("  | /    |    ")
        print("  |/     O    ")
        print("  |     /|\   ")
        print("  |      |    ")
        print("  |     /     ")
        print("  |           ")
        print("__|__________ \n")

    elif fail == 6:
        print("   __________ ")
        print("  | /    |    ")
        print("  |/     O    ")
        print("  |     /|\   ")
        print("  |      |    ")
        print("  |     / \   ")
        print("  |           ")
        print("__|__________ ")
        print("    GAME OVER \n")

def checkWord(guess):
    global fail
    guess = input("\n\nGuess a letter of this word: ")
    while fail < gameOver:
        for i in word:
            if i in guess:
                print(guess, end= ' ')
            else:
                print('_', end =' ')
        guess = input("\n\nGuess a letter of this word: ")
    
            
        if guess not in word:
            print("The word does not contain " + guess)
            print("Try again")
            fail+=1
            
                
            
            

def hangman():
    print("You are now playing Hangman")
    gameProgress(fail)
    for i in word:
        print("_", end=' ')
    checkWord(guess)

    
      
    

hangman()
    
    
    
