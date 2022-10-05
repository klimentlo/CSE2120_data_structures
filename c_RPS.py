#c_RPS.py

'''
title: rock paper scissors
author: kliment lo
date: 10/5/2022
'''

from random import randrange

def checkInt(NUMBER):
    '''
    verifies if the number is an integer
    :param NUMBER: (str)
    :return: (int)
    '''
    if NUMBER.isnumeric():
        return int(NUMBER)
    else:
        print("That is not a number!")
        NEW_NUM = input("Please enter a valid number! ")
        return checkInt(NEW_NUM)

def chooseWeapon():
    """
    Prints a selection of weapons for the user to select
    :return: (int) chosen weapon
    """
    print("""
1. Rock
2. Lizard
3. Spock    
4. Scissors
5. Paper
""")
    WEAPON = input("> ")
    WEAPON = checkInt(WEAPON)
    if WEAPON > 0 and WEAPON < 6:
        return WEAPON
    else:
        print("Please choose a valid option from the list! ")
        return chooseWeapon()

def computerWeapon():
    '''
    computer randomly chooses a weapon
    :return:
    '''
    return randrange(5)

def getWinner(PLAYER, COMPUTER, WEAPONS):
    '''
    determines who the winner is
    :param PLAYER: (int) player weapon
    :param COMPUTER: (int) computer weapon
    :return: (int) Winner (0= tie, 1 = player, 2 = computer)
    '''
    WEAPONS = ("Rock", "Lizard", "Spock", "Scissors", "Paper")
    if PLAYER == COMPUTER:
        return 0
    elif WEAPONS[COMPUTER] == WEAPONS[PLAYER - 1] or WEAPONS[COMPUTER] == WEAPONS[COMPUTER - 3]:
        return 2
    else:
        return 1

def displayWinner(WINNER):
    '''
    Displays the winner of the round
    :param WINNER:  (int) winner
    :return: (none)
    '''
    if WINNER == 0:
        print("You and the computer tied! ")
    elif WINNER == 1:
        print("You win! ")
    else:
        print ("You lose... ")

if __name__ == "__main__":
    WEAPONS = ("Rock", "Lizard", "Spock", "Scissors", "Paper")
    USER = chooseWeapon()
    COMP = computerWeapon()
    WINNER = getWinner(USER, COMP, WEAPONS)
    displayWinner(WINNER)
    print(USER)
    print(COMP)
