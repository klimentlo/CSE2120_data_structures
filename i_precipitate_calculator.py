# i_precipitate_calculator.py

'''
title: precipitate calculator
author: kliment lo
date: 10/18/2022
'''
import math

# --- DICTIONARIES/TUPLE/ARRAY SETUP --- #
def possibilities():
    '''
    creates 52 cards in a 2D array
    :return: (list)
    '''
    CARDS = []
    # make an empty list for all the cards (if we make a new variable and copy the "CARDS" list onto it and change the new variable list, it will also change the original list. But if we make an empty list, then it wont change both.

    # make an empty array for each suit and append cards to each suit, then add them all together to make the full dark
    RowNh = []
    for j in range(5): #NH = 1, NO = 2, CIO3 = 3, CIO4 = 4, CHC00 = 5
        for i in range(4):
            RowNh.append((j+1, i+1))
        #CLUBS is suit 3

    RowF = [] # F = 6
    for i in range(8):
        RowF.append((6, i+1))
        # DIAMONDS will be suit 0

    RowCl = []    # Cl = 7, Br = 8, I = 9
    for j in range(3):
        for i in range(5):
            RowCl.append((j+7, i+1))

    RowSo = [] #So = 10
    for i in range(7):
        RowSo.append((10, i+1))
        #CLUBS is suit 2
    Soluable = displayPositibilities(RowNh, RowF, RowCl, RowSo)
    return Soluable

def displayPositibilities(RowNh, RowF, RowCl, RowSo):
    '''
    prints out a card nicely
    :param CARD: (tuple)
    :return: (none)
    '''
    global negIons, posIonsNh, posIonsF, posIonsCl, posIonsSo
    ROWNH = []
    for i in range(len(RowNh)):
        ROWNH.append(negIons[RowNh[i][0]] + posIonsNh[RowNh[i][1]])


    ROWF = []
    for i in range(len(RowF)):
        ROWF.append(negIons[RowF[i][0]] + posIonsF[RowF[i][1]])


    ROWCL = []
    for i in range(len(RowCl)):
        ROWCL.append(negIons[RowCl[i][0]] + posIonsCl[RowCl[i][1]])


    ROWSO = []
    for i in range(len(RowSo)):
        ROWSO.append(negIons[RowSo[i][0]] + posIonsSo[RowSo[i][1]])


    POSSIBILITIES = ROWNH + ROWF + ROWCL + ROWSO
    print(POSSIBILITIES)
    return POSSIBILITIES
        #


# librarys to create all the possible things that create a solid
negIons = {
    1 : "nh",
    2 : "no",
    3 : "cio3",
    4 : "cio4",
    5 : "chcoo",
    6 : "f",
    7 : "cl",
    8 : "br",
    9 : "i",
    10 : "so"
}

posIonsNh = {
    1 : "rbcio",
    2 : "cscio",
    3 : "agchcoo",
    4 : "hg(chcoo)"
}

posIonsF = {
    1 : "li",
    2 : "mg",
    3 : "ca",
    4 : "sr",
    5 : "ba",
    6 : "fe",
    7 : "hg",
    8 : "pb",
}

posIonsCl = {
    1 : "cu",
    2 : "ag",
    3 : "hg",
    4 : "pb",
    5 : "tl",
}

posIonsSo = {
    1 : "ca",
    2 : "sr",
    3 : "ba",
    4 : "ag",
    5 : "hg",
    6 : "pb",
    7 : "ra",
}

positiveCharge = {
    "li" : 1,
    "mg" : 2,
    "ca" : 2,
    "sr" : 2,
    "ba" : 2,
    "fe" : 2,
    "hg" : 2,
    "pb" : 2,
    "cu" : 1,
    "ag" : 1,
    "tl" : 1,
    "ra" : 2
}

negativeCharge = {
    "f" : 1,
    "cl" : 1,
    "br" : 1,
    "i" : 1,
    "so" : 2,
}

ionMass = {
    "li" : 6.9410, # 0
    "mg" : 24.305, # 1
    "ca" : 40.078, # 2
    "sr" : 87.620, # 3
    "ba" : 137.33, # 4
    "fe" : 55.845, # 5
    "hg" : 200.59, # 6
    "pb" : 207.20, # 7
    "cu" : 63.546, # 8
    "ag" : 107.87, # 9
    "tl" : 204.38, # 10
    "ra" : 227.00, #11
    "f" : 18.998, # 12
    "cl" : 35.453, # 13
    "br" : 79.904, # 14
    "i" : 126.90, # 15
    "so" : 96.06, # 16
}


# --- FUNCTIONS --- #

### INPUTS

## Check functions
def checkFloat(NUMBER):
   '''
   checks if the input is a float
   :param NUMBER:
   :return:
   '''
   try:
       NUMBER = float(NUMBER)
       return NUMBER
   except:
       print("That is not a number! ")
       NEW_NUM = input("Please input a number.")
       return checkFloat(NEW_NUM)

def checkNeg(NUMBER):
   '''
   checks if the number is a negative
   :param NUMBER:
   :return:
   '''
   NUMBER = checkFloat(NUMBER)
   if NUMBER < 0:
       print("This value can't be a negative! ")
       NEW_NUM = input("Please input a new number.")
       return checkNeg(NEW_NUM)
   else:
       return NUMBER

# OTHER

def positiveIon():
    '''
    requests for the positive ion
    :return:(str)
    '''
    ION = input("Please input the positive reacting ion: (no charges) ")
    print(ION)
    ION = ION.lower()
    try:
        positiveCharge[ION] # try to put the user's input into the list of positive charges, if it exists then it returns the ion they chose.
        return ION # we dont do anything with this charge as this is solely to detext this
    except:
        print("That is not one of the options. Please choose again")
        return positiveIon()

def negativeIon():
   '''
   requests for the negative ion
   :return: (str)
   '''
   ION = input("Please input the negative reacting ion: (no charges) ")
   print(ION)
   ION = ION.lower()
   try:
       negativeCharge[ION]  # try to put the user's input into the list of negative charges, if it exists then it returns the ion they chose.
       return ION  # we dont do anything with this charge as this is solely to detext this
   except:
       print("That is not one of the options. Please choose again")
       return negativeIon()

def getConcentration():
   '''
   requests for the concentration of the mixture
   :return: (float)
   '''
   CONCENTRATION = input("Please input how concentrated the fluid is: ")
   CONCENTRATION = checkFloat(CONCENTRATION)
   CONCENTRATION = checkNeg(CONCENTRATION)
   return CONCENTRATION

def getVolume():
   '''
   requests for the volume of the mixture
   :return: (float)
   '''
   VOLUME = input("Please input how many liters of fluid there is: ")
   VOLUME = checkFloat(VOLUME)
   VOLUME = checkNeg(VOLUME)
   return VOLUME


### PROCESSING

def getMass(ION):
   '''
   get the mass depending on the ion they selected
   :param ION:
   :return:
   '''
   MASS = ionMass[ION]
   print(MASS)
   return MASS

def getChargeP(ION):
   '''
   get the charge of the positive ion depending on the ion they selected
   :param ION: (int)
   :return:
   '''
   ION = ION.lower()
   CHARGE = positiveCharge[ION]
   return CHARGE

def getChargeN(ION):
   '''
   get the charge of the negative ion depending on the ion they selected
   :param ION: (int)
   :return:
   '''
   ION = ION.lower()
   CHARGE = negativeCharge[ION]
   return CHARGE

def moleCal(volume, concentration):
   '''
   calculates the amount of moles in the ion
   :param MOLES:
   :return:
   '''
   moles = volume * concentration
   return moles

def checkPossible(IonN, IonP, possibilities):
    together = IonN + IonP
    for i in range(len(possibilities)):
        print(i)
        if together == possibilities[i]:
            print("omg its possible")
            return True
    print("not possible :( ")
def limitReactantCal(ionP, ionN, molesN, molesP):
   '''
   idk
   :param moles:
   :return:
   '''
   global positiveCharge, negativeCharge
   NEGREACTANT = molesP * (negativeCharge[ionN]/positiveCharge[ionP])
   if NEGREACTANT < molesN:
       print("balls")
   return NEGREACTANT


### OUTPUTS
def intro():
   '''
   is the introduction of what this is
   :return: (none)
   '''
   print("""
Welcome to the chemistry precipitate calculator!   
""")
### dont forget to fulfull all the requirements, ALL OF THEM



# --- MAIN PROGRAM --- #
if __name__ == "__main__":
   intro()
   possibilities = possibilities()
   while True:
      #get and calculate all things needed about positive ion
      ionP = positiveIon()
      massP = getMass(ionP)
      chargeP = getChargeP(ionP)
      volumeP = getVolume()
      concentrationP = getConcentration()
      #get and calculate all things needed about negative ion
      ionN = negativeIon()
      massN = getMass(ionN)
      chargeN = getChargeN(ionN)
      volumeN = getVolume()
      concentrationN = getConcentration()
      molesP = moleCal(volumeP, concentrationP)
      molesN = moleCal(volumeN, concentrationN)
      checkPossible(ionN, ionP, possibilities)
      limitedReactant = limitReactantCal(ionP, ionN, molesN, molesP)

# WHEN YOU PRITN OUT THE ANSWER TO THE USER, MAKE SURE TO CONVERT THE cl or fe or whatever BACK INTO CAPITALIZATION. USING THE FUNCTION .capitalize() (capitalizes the first letter)

coefficient = []
coefficient = [1, 1, 1]

# I PLAN THIS TO BE A DISPLAY THING, WHERE IN THE MENU, YOU CAN TYPE "ELEMENTS"
DISPLAY = (("Lithium", 6.9410), ("Magnesium", 24.305), ("Calcium", 40.078), ("Strontium", 87.620), ("Barium", 137.33), ("Iron", 55.845), ("Mercury", 200.59), ("Lead", 207.20) , ("Copper", 63.546), ("Silver", 107.87), ("Thallium", 204.38), ("Fluorine", 18.998), ("Chlorine", 35.453), ("Bromine", 79.904), ("Iodine", 126.90), ("Sulfate", 96.06))
#if askDisplay True:
 #  for i in range(len(DISPLAY)):
  #     for j in range(len(DISPLAY)):
   #        print(f"Name: {DISPLAY[i][j]}")
    #       idk im gonna cry


