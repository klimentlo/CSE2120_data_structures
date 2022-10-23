# f_playing_cards.py

'''
title: playing cards
author: kliment lo
date-created: 10-12-2022
'''
# --- FUNCTIONS --- #
### INPUTS



### PROCESSING
def makeDeck():
    '''
    creates 52 cards in a 2D array
    :return: (list)
    '''
    CARDS = []
    # make an empty list for all the cards (if we make a new variable and copy the "CARDS" list onto it and change the new variable list, it will also change the original list. But if we make an empty list, then it wont change both.

    # make an empty array for each suit and append cards to each suit, then add them all together to make the full dark

    DIAMONDS = []
    for i in range(13):
        DIAMONDS.append((0, i))
        # DIAMONDS will be suit 0

    CLUBS = []
    for i in range(13):
        CLUBS.append((1, i))
        #CLUBS is suit 1

    HEARTS = []
    for i in range(13):
        HEARTS.append((2, i))
        #CLUBS is suit 2

    SPADES = []
    for i in range(13):
        SPADES.append((3, i))
        #CLUBS is suit 3

    CARDS = DIAMONDS + CLUBS + HEARTS + SPADES
    #print(CARDS[25])
    return CARDS


def shuffleDeck(CARDS):
    '''
    shuffles all the cards in the list   (the list that goes " (0,1), (0,2), etc.")
    :param CARDS: (list)
    :return: (list)
    '''
    SHUFFLE_DECK = []
    for i in range(len(CARDS)): # if i is under the amount of cards in the deck (which is 52), and it still runs 52 times even though we are popping things off the list
        SHUFFLE_DECK.append(CARDS.pop(randrange(len(CARDS)))) # append adds the card to shuffle deck, CARDS.pop will remove that card from CARDS, and it is all randomized.
        #randrange(len(CARDS)) will randomize from a smaller range as cards get popped off from the list
    return SHUFFLE_DECK

def drawCards(CARDS):
    '''
    draws a card from the top of the deck
    :param CARDS: (list)
    :return: (tuple)
    '''
    CARDS = CARDS.pop(0)
    return CARDS

### OUTPUTS

def displayDeck(CARDS):
    '''
    prints out all the cards in a list with values and suits
    :param CARDS: (list)
    :return: (none)
    '''
    global VALUES, SUITS
    DECK_READ = ""
    for i in range(len(CARDS)):
        DECK_READ = DECK_READ + f"{VALUES[CARDS[i][1]]} of {SUITS[CARDS[i][0]]}, "
        #
        print(f"DECKREAD : {DECK_READ}" )

def displayCard(CARD):
    '''
    prints out a card nicely
    :param CARD: (tuple)
    :return: (none)
    '''
    global SUITS, VALUES
    print(f"{VALUES[CARD[1]]} of {SUITS[CARD[0]]}")



# we need a dictionary to translate 0-3 to the correct suit
# we need a dictionary to translate 0-12 to the correct card
# we will call these dictionaries into other functions using global
SUITS = {
    0: "Diamonds",
    1: "Clubs",
    2: "Hearts",
    3: "Spades"
}

VALUES = {
    0: "Ace",
    1: "2",
    2: "3",
    3: "4",
    4: "5",
    5: "6",
    6: "7",
    7: "8",
    8: "9",
    9: "10",
    10: "Jack",
    11: "Queen",
    12: "King",
}
#print(CARDS[25])
#print(f"{VALUES[CARDS[1][1]]} of {SUITS[CARDS[3][0]]}")
# we need to specify which part of CARDS[25] to translate with the SUITS dictionary
# [0] is the suit and [1] is the value of the cards
# 12, 25, 38, and 51 should all be kings
# 6, 19, 32, and 45 should all be 7s

from random import randrange
if __name__ == "__main__":
    CARDS = makeDeck()
    displayDeck(CARDS)
    CARDS = shuffleDeck(CARDS)
    displayDeck(CARDS)
    CARD = drawCards(CARDS)
    displayCard(CARD)
    displayDeck(CARDS)







'''
print(f"Randrange randomly selected {CARD}")
print(CARDS[CARD]) #print out the "x"th part of the list. For example. If CARD = 10 , this command will print out CARDS[10], which would be (0,11)
print(CARDS)
print(f"Your card is the {VALUES[CARDS[CARD][1]]} of {SUITS[CARDS[CARD][0]]}")
'''