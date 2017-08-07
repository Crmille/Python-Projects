import requests
import random

#GLOBALS


def hangman_getDifficulty():
    print("Choose the Difficulty. 1-Easy, 2-Normal, 3-Hard.")
    difficulty = input("Enter 1, 2, or 3.")

    if int(difficulty) is not 1 or 2 or 3:
        print("Invalid input.")
        difficulty = hangman_getDifficulty()
    else: pass
        
    return difficulty

def hangman_getRandomword():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()    
    word = random.choice(WORDS)
       
    return word
    
    
    
def hangman_getLetter(guessedCharacters):
    while True:
        guess = input("Please input a single character:")
        guess = guess.lower()
        
        if len(guess) is not 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Invalid input. Try again.")
        elif guess in guessedCharacters:
            print("You have already guessed this character:", guess)
        else: return guess
        
        
        

def main(intro=True):
    if intro == True:
        print(""" 
            Welcome to Hangman!
            
            The rules are the game are as follows:
                1. Choose characters that may be in the word.
                2. Reveal all the characters before the counter reaches zero.
                3. The characters in the secret word are always lowercase.
        """)
    else: pass
    
    total_rounds = 6
    current_round = 0
    secretWord = hangman_getRandomword()
    secretWord = secretWord.lower()
    
    guessedCharacters = []
    correctCharacters = []
    print("The length of the Secret Word is:", len(secretWord))
    
    gameState = False
    
    while current_round < total_rounds:
     
        print("Missed characters:", guessedCharacters)
        
        hiddenWord = '_' * len(secretWord)
        
        for character in secretWord:
            if secretWord[character] in correctCharacters:
                hiddenWord = hiddenWord[:character] + secretWord[character] + hiddenWord[character+1:]
                
        for char in hiddenWord:
            print(char, end=' ')
        
        playerGuess = hangman_getLetter()
        
        if playerGuess in secretWord:
            correctCharacters = correctCharacters + playerGuess
            
            wordCheck = True
            for char in secretWord:
                if secretWord[char] not in correctCharacters:
                    wordCheck = False
                    break
                
            if wordCheck == True:
                print("Congrats! The word is:",secretWord)
                print("You have won!")
                gameState = True
            
        else: 
            guessedCharacters = guessedCharacters + playerGuess
            
            incorrectGuess = len(guessedCharacters) - len(correctCharacters)
            
            if int(incorrectGuess) > total_rounds:
                print("You have run out of guesses!")
                print("The word is:", secretWord)
                gameState = True
        
        if gameState == True:
            game_continue = input("New game? y/n?")
            game_continue = game_continue.lower()
            
            if game_continue == 'y':
                guessedCharacters = []
                correctCharacters = []
                current_round = 0
                gameState = False
                secretWord = hangman_getRandomword()
                secretWord = secretWord.lower()
                print("The Length of the Secret Word is:", len(secretWord))
            else: break
 


if __name__== "__main__":
    main()