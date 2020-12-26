'''
    GlobalAIHub - Homework 3
    Huseyin SAHIN
    huseyinsahn@gmail.com
'''
import random 

name = input("Please enter your name before started the game: ")
print('Welcome {}'.format(name))

def getWords():
    words = ["turkey", "huseyin", "globalaihub", "galatasaray","messi","antalya","covid","lenovo"]
    return random.choice(words)

def playHangman():
    searched_word = getWords()
    retries = 6
    letters = []
    word_length = len(searched_word)
    guess = list('_'* word_length)

    print(' '.join(guess),end = '\n')

    while retries > 0:
    
        guessed_letter = input("Please guess a letter: ")
        if guessed_letter in letters:
            print("Please do not guess the letters you guessed earlier!!")
            continue
            
        elif len(guessed_letter) > 1:
            print("Please enter only one letter!!")
            continue

        elif guessed_letter not in searched_word:
            retries -= 1
            print(f'Wrong guess!! You have {retries} guesses left.')
            
        else:
            for i in range(len(searched_word)):
                if guessed_letter == searched_word[i]:
                    print("Right guess!!")
                    guess[i] = guessed_letter
                    letters.append(guessed_letter)

            print(' '.join(guess), end='\n')

        answer = input("Do you want to guess the full word?.Enter 'y' if yes, and 'n' if no: ")

        if answer == "y":
            guessed_word = input("Please enter the full word: ")
            if guessed_word == searched_word:
                print("Congratulations!!")
                break
            else:
                retries -= 1
                print(f'Wrong guess!! You have {retries} guesses left.')

        if retries == 0:
            print("Your right to guess is over.You lost the game.")
            break

playHangman()
