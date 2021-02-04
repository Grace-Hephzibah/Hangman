import Hangman as hg
import Hangman_Functions as hf
import Words as w

print("H A N G M A N")

# Missed Letters -----> ml
# Correct Letters ----> cl
# Secret Word --------> sw
# Found All Letters --> fal

sw = hf.getRandomWord(w.words)

ml = ''
cl = ''

GameIsDone = False

while True:

    hf.displayBoard(ml, cl, sw)

    guess = hf.getGuess(ml+cl)

    if guess in sw:
        cl += guess

        fal = True

        for i in range(len(sw)):
            if sw[i] not in cl:
                fal = False
                break;

        if fal == True:
            print('You have won. The secret word is ', sw)

            GameIsDone = True

    else:
        ml += guess;

        if len(ml) == len(hg.Hangman)-1:
            hf.displayBoard(ml, cl, sw)
            print('You have run out of guess! The word is ', sw)

            GameIsDone = True


    if GameIsDone == True:
        if hf.playAgain():
            ml = ''
            cl = ''
            GameIsDone = False
            sw = hf.getRandomWord(w.words)

        else:
            break;

            
            



















            
        
