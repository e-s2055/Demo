import random #imports "random" library - has random.randint, random number generator

def guess(x): 
    '''passes x to get a random number'''
    '''returns a random number to guess'''
    random_number = random.randint(1, x) 
    '''Never want user input will never be the same as default'''
    guess = 0 
    '''while (expression): <--- you want to stop it when X is fulfilled'''
    while guess is not random_number: 
        '''int() to specify an int for input'''
        guess = int(input(f'Guess a number between 1 and {x}')) 
        if guess < random_number:
            print("Sorry, try again. Too low.")
        elif guess > random_number:
            print("Sorry, try again. Too high.")
    print(f"Correct! You've correct the guessed the number {random_number} correctly.")

def computer_guess(x):
    '''goal is to choose a number and NOT tell the computer
    #range below'''
    low, high = 1, x
    '''next tell comp if it's too high, too low, or correct: feedback var'''
    feedback = ""
    while feedback != "c":
        if low != high: 
            '''Make low/high your bounds to shrink the range according to user'''
            guess = random.randint(low, high)
        else:
            guess = low
        ''' Asks for user feedback on {guess}, and automatically lowers the feedback'''
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The computer guessed your number {guess} correctly!")

computer_guess(10)
