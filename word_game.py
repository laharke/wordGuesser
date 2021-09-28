import random


LEXICON_FILE = "TestLexicon.txt"    # File to read word list from
INITIAL_GUESSES = 6             # Initial number of guesses player starts with

def underscore(wordLen):
    """this function creates a list of the same length as the parameter given, but the list is filled with underscores,it returns said list"""
    wordlist = []
    for i in range(wordLen):
        wordlist.append("-")
    return wordlist

def splitword(secret_word):
    """this function splits the word given and appends it into a list, it returns said list"""
    splitword = []
    for char in secret_word:
        splitword.append(char)
    return splitword

def checkend(underscorelist):
    """this function checks if the game should end by checking the list that's suopousse to be all letters if the user gussed every single one alredy, it returns false
    if that´s the case to end the while loop that runs the"""
    if '-' in underscorelist:
        return True
    else:
        return False

def printlist(underscorelist):
    for elem in underscorelist:
        print(elem, end = '')
    print()

def play_game(secret_word):
    #WORD PART 
    wordLen = len(secret_word)
    #LIST COMPLETA Y VACIA
    wordlist = splitword(secret_word)
    underscorelist = underscore(wordLen)
    print(f"The word now looks like this: ", end = '')
    printlist(underscorelist)
    guess = guessOneTime()
    counter = 0
    INITIAL_GUESSES = 6
    chances = 6
    #JUST PLAYING THE GAME BEFORE ENTERING THE LOOP UNTIL ITS OVER
    for i in range(len(wordlist)):
        if wordlist[i] == guess:
            underscorelist[i] = wordlist[i]
    if guess not in wordlist:
        print("Letter not in the word")
        counter += 1
        INITIAL_GUESSES -= 1
        chances -= 1
        print(f"You have {INITIAL_GUESSES} chances left")
    else:
        print("That guess is correct")
    print("The word now looks like this: ", end = '')
    printlist(underscorelist)

    #DECLARING THE VARAIBLE TO BE ABLE TO FINISH THE GAME IF THE USER WINS
    
    finishgame = True
    while counter <= INITIAL_GUESSES and finishgame == True:
        guess = guessOneTime()
        for i in range(len(wordlist)):
            if wordlist[i] == guess:
                underscorelist[i] = wordlist[i]
        if guess not in wordlist:
            print("Letter not in the word")
            counter += 1
            chances -= 1
            if chances != 0:
                print(f"You have {chances} chances left")
        else:
            print("That guess is correct")
        print("The word now looks like this: ", end = '')
        printlist(underscorelist)
        finishgame = checkend(underscorelist)
    if counter > INITIAL_GUESSES:
        print(f"Sorry, you lost. The secret word was: {secret_word}")
    if finishgame == False:
        print(f"Congratualtions, the word is: {secret_word}")

    # GUESS PART
def guessOneTime():
    """this function ask the user for input one time and makes sure the input in valid
    it also makes the input uppercase to match the words i alredy have, it returns the input as a normalized word"""
    guess = input("Type a single letter here, then press enter: ")
    while len(guess) != 1 or not guess.isalpha():
        print("Guess should only be a single charcater.")
        guess = input("Type a single letter here, then press enter: ")
    guess = guess.upper()
    return guess

def get_word(LEXICON_FILE):
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    with open(LEXICON_FILE) as f:
        listapalabras = []
        for line in f:
           listapalabras.append(line.strip())
    return random.choice(listapalabras)



def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word(LEXICON_FILE)
    play_game(secret_word)


if __name__ == "__main__":
    main()