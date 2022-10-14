# g_blackjack.py

'''
title: blackjack
author: kliment lo
date: 10-13-2022
'''

from f_playing_cards import makeDeck, shuffleDeck, drawCards, displayDeck, displayCard

# --- FUNCTIONS --- #

### INPUTS
def chooseAction():
    '''
    player chooses to draw or stay
    :return: (int)
    '''
    print('''
1. Hit me!
2. I'll stay 
''')
    CHOICE = int(input("> "))
    # could use checkInt here as well to prevent crashes when the user enters an invalid input
    if CHOICE < 1 or CHOICE > 2:
        print("Please enter a valid option! ")
        return chooseAction()
    else:
        return CHOICE

#def askContinue():

### PROCESSING
def gameSetup():
    '''
    shuffles the deck and deals starting cards to the players
    :return: (none)
    '''
    global DECK, DEALER_HAND, PLAYER_HAND

    DECK = shuffleDeck(DECK)
    for i in range(2):
        PLAYER_HAND.append(drawCards(DECK))
        DEALER_HAND.append(drawCards(DECK))
    POINT = calculatePoints(PLAYER_HAND)
    return POINT


def calculatePoints(HAND):
    '''
    calculates total points from the hand
    :param PLAYER_HAND: (list)
    :return: (int)
    '''
    POINTS = 0
    ACES = 0
    # aces will be worth either 1 or 11 depending on the current points total
    for i in range(len(HAND)):
        # CARDS [i] [1] is the value of the card
        if HAND[i][1] == 0:
            # if we have an ace, add 11
            POINTS = POINTS + 11
            ACES = ACES + 1
        elif HAND[i][1] > 8:
            # 9 = 10, 10 = jack, 11 = queen, king = 12
            # which are each worth 10 each
            POINTS = POINTS + 10
        else:
            POINTS = POINTS + HAND[i][1] + 1

            # we need to add 1 to HAND [i]][1] because each card's number is 1 less than it's value (because we started at 0)
        # allow ACES to be worth 1 if POINTS > 21
        while POINTS > 21 and ACES > 0:
            POINTS = POINTS - 10
            ACES = ACES - 1
    return POINTS

def determineWinner(PLAYER, DEALER):
    if PLAYER > 21:
        print("You went over 21! You lose!")
    elif DEALER > 21:
        print("Dealer went over 21! You win!")
    else:
        if PLAYER > DEALER:
            print("You had a higher sum than the Dealer. You win!")
        elif DEALER > PLAYER:
            print("Dealer had a higher sum than your deck. You lose!")
        else:
            print("It was a tie!")

### OUTPUTS
def displayCards():
    '''
    displays all cards on the table
    :return: (none)
    '''
    global PLAYER_HAND, DEALER_HAND
    print("DEALER: ")
    displayDeck(DEALER_HAND)
    print("PLAYER: ")
    displayDeck(PLAYER_HAND)
# --- VARIABLES --- #
# first we will create our deck of cards
DECK = makeDeck()
DEALER_HAND = []
PLAYER_HAND = []

DEALER_POINTS = 0
PLAYER_POINTS = 0

DEALER_STAY = False
PLAYER_STAY = False

# --- MAIN PROGRAM CODE --- #
if __name__ == "__main__":
    POINT = gameSetup()
    displayCards()
    print(f"The sum of your cards is currently {POINT} ")
    while not PLAYER_STAY:
        ACTION = chooseAction()
        if ACTION == 1:
            #player draws another card
            PLAYER_HAND.append(drawCards(DECK))
        else:
            PLAYER_STAY = True
        displayDeck(PLAYER_HAND)
        if DEALER_POINTS < 17:
            DEALER_HAND.append(drawCards(DECK))
        DEALER_POINTS = calculatePoints(DEALER_HAND)
        PLAYER_POINTS = calculatePoints(PLAYER_HAND)
        print(PLAYER_POINTS)
        print(DEALER_POINTS)
        WINNER = determineWinner(PLAYER_POINTS, DEALER_POINTS)