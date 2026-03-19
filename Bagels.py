"""Bagels, a deductive logic game by Al Sweigart.

A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Yoru Own
Computer Games with Python" htpps://nostarch.com/inventwithpython
Tages: short, game, puzzle"""

import random
# Brings in built-in random module 

NUM_DIGITS = 3 
MAX_GUESSES = 10

def getSecretNum():
    """Returns a string made up of num_digits unique random digits."""

    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order

    # Get the first num_digits digits in the list for the secret number:
    secretNum  = ''
    for i in range(NUM_DIGITS):
        secret += str(numbers[i])

    return secretNum
    
def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number paint."""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0: # There ar eno correct digits at all.
        return 'Bagel' 
    else:
        # Sort the clues into alphabetical order so their original order
        # Doesn't give information away
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)
        
def main():
    """define main function"""

    print('''Bagels, a deductive logic game by Al Sweigart.
    By Al Sweigart al@inventwithpython.com
          
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
        When I say:     That means:
        Pico           One digit is correct but in the wrong position.
        Fermi          One digit is correct and in the right position.
        Bagels         No digit is correct.
          
    For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico'''.format(NUM_DIGITS))
   
   # Intiate main game loop 
    while True: 
        # Store the secret number the player needs to guess
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looing until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(num_guesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            num_guesses += 1

            if guess == secretNum:
                break # PLayer has guessed the correct number, break out of loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

if __name__ == '__main__':
    main()