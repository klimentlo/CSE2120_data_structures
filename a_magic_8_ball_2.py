#a_magic_8_ball_2.py

'''
title: magic 8 ball with lists
author: kliment lo
date-crated: october 3, 2022
'''

from random import randrange

# --- SUBROUTINES --- #
def displayIntro():
    print("""
Welcome to Magic 8 Ball!
It's all-knowing.......................
    """)

### INPUTS
def shakeBall():
    '''
    Determines whether to shake the ball
    :return: (bool)
    '''
    RESULT = input("Shake ball? (Y/n) ")
    RESULT = RESULT.upper()
    # upper() is a function that transforms a string into UPPERCASE
    if RESULT == "N" or RESULT == "NO":
        return False
    else:
        return True

### PROCESSING
def getNumber():
    '''
    Selects a random index number
    :return: (int)
    '''
    global ANSWERS
    # ANSWERS will be our static array of magic 8 ball answers
    CHOICE = randrange(len(ANSWERS))
    return CHOICE
### OUTPUTS
def displayAnswer(TEXT):
    '''
    displays the 8 ball answer
    :param TEXT: (str)
    :return: (none)
    '''
    print(TEXT)

### VARIABLES
ANSWERS = ("it is certain :D",
           "No, you idiot",
           "ask me again later",
           "hell nah",
           "don't count on it",
           "you're stupid",
           "don't kys, that's bad. But yea, it's not a good idea"
)
### --- MAIN PROGRAM --- ###
if __name__ == "__main__":

    for i in range (len(ANSWERS)):
        print(ANSWERS[1])

    displayIntro()
    while True:
        if shakeBall():
            CHOICE = getNumber()
            displayAnswer(ANSWERS[CHOICE])
            # displayAnswer(ANSWERS[CHOICE]) will use index item CHOICE from the tuple ANSWERS as the argument for the function displayAnswer()
        else:
            exit()