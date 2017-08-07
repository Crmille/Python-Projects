# -*- coding: utf-8 -*-
"""
GUESS THE NUMBER
"""

import random

def main(intro=True):
    if intro == True:
        print(""" 
        Welcome to Guess the Number!

        Here are the rules:
            1. A number is randomly generated.
            2. You guess the number. 
            3. If your guess is correct, you win!        
        """)

    minVal = 1
    maxVal = 10
    guesses = []
    randomVal = random.randint(minVal,maxVal)
    
    print("The random value has been generated.")
    print("The number is between:",minVal,"and",maxVal)
    
    while True:
        try:
            guess = int(input("Please input your guess."))
        except ValueError:
            continue
        else:
            if guess in guesses:
                print("I'm sorry, this guess has alreayd been used. Try agian.")
                continue
            elif guess < randomVal:
                print("I'm sorry, your guess is too low.")
                guesses.append(guess)
            elif guess > randomVal:
                print("I'm sorry, your guess is too high.")
                guesses.append(guess)
            elif guess > maxVal or guess < minVal:
                print("I'm sorry, your guess is out of bounds. Try again." )
        



if __name__== "__main__":
    main()
