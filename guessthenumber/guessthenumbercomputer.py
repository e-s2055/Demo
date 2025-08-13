import random #imports "random" library - has random.randint, random number generator

def guess(x): #passes x to get a random number
    random_number = random.randint(1, x) #returns a random number to guess
    guess = 0 # Never want user input will never be the same as default
    while guess is not random_number: # while (expression): <--- you want to stop it when X is fulfilled
        guess = int(input(f'Guess a number between 1 and {x}')) #int() to specify an int for input
        if guess < random_number:
            print("Sorry, try again. Too low.")
        elif guess > random_number:
            print("Sorry, try again. Too high.")
    print(f"Correct! You've correct the guessed the number {random_number} correctly.")

guess(10)