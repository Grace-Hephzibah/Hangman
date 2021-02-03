import random as rd

import Words as W
import Hangman as hg


def getRandomWord(wordlist):
    wordIndex = rd.randint(0, len(W.words) - 1 )

    return W.words[wordIndex]

def displayBoard (missedLetters, correctLetters, secretWord):

    print (hg.Hangman[len(missedLetters)])
    print()

    print('Missed Letters : ', end = " " )

    for letter in missedLetters:
        print(letter, end = " ")
    print()

    blanks = '_' * len(secretWord)

    for i in range (len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end= " ")
    print()

def getGuess (alreadyGuessed):

    while (True):
        print('Guess a letter.')
        guess = input()

        guess = guess.lower()

        if len(guess) != 1:
            print('Please enter a single letter. ')

        elif guess in alreadyGuessed:
            print('You have already guessed that letter.')

        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a Letter. ')

        else:
            return guess

def playAgain():

    print('Do you want to play again ? (yes or no) ' )

    return input().lower().startswith('y')




    
