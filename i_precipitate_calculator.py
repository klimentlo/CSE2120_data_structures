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
    for j in range(12): #NH = 1, NO = 2, CIO3 = 3, CIO4 = 4, CHC00 = 5
        for i in range(4):
            RowNh.append((j+1, i+1))
        #CLUBS is suit 3

    RowF = [] # F = 6
    for i in range(8):
        RowF.append((13, i+1))
        # DIAMONDS will be suit 0

    RowCl = []    # Cl = 7, Br = 8, I = 9
    for j in range(3):
        for i in range(5):
            RowCl.append((j+14, i+1))

    RowSo = [] #So = 10
    for i in range(7):
        RowSo.append((17, i+1))
        #CLUBS is suit 2
    Soluable = RowNh + RowF + RowCl + RowSo
    print(Soluable)
    Soluable = displayPositibilities(RowNh, RowF, RowCl, RowSo)
    print(Soluable)
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
    return POSSIBILITIES
        #


# librarys to create all the possible things that create a solid
negIons = {
    1 : "h",
    2 : "li",
    3 : "na",
    4 : "k",
    5 : "rb",
    6 : "cs",
    7 : "fr",
    8 : "nh4",
    9 : "no3",
    10 : "cio3",
    11 : "cio4",
    12 : "ch3coo",
    13 : "f",
    14 : "cl",
    15 : "br",
    16 : "i",
    17 : "so4"
}

posIonsNh = {
    1 : "rbcio4",
    2 : "cscio4",
    3 : "agch3coo",
    4 : "hg2(ch3coo)2"
}

posIonsF = {
    1 : "li",
    2 : "mg",
    3 : "ca",
    4 : "sr",
    5 : "ba",
    6 : "fe",
    7 : "hg2",
    8 : "pb"
}

posIonsCl = {
    1 : "cu",
    2 : "ag",
    3 : "hg2",
    4 : "pb",
    5 : "tl"
}

posIonsSo = {
    1 : "ca",
    2 : "sr",
    3 : "ba",
    4 : "ag",
    5 : "hg2",
    6 : "pb",
    7 : "ra4"
}

positiveCharge = {
    "li" : 1,
    "mg" : 2,
    "ca" : 2,
    "sr" : 2,
    "ba" : 2,
    "fe" : 2,
    "hg2" : 2,
    "pb" : 2,
    "cu" : 1,
    "ag" : 1,
    "tl" : 1,
    "ra" : 2,
    "nh4": 1
}

negativeCharge = {
    "no3" : 1,
    "cio3" : 1,
    "cio4" : 1,
    "ch3coo" : 1,
    "f" : 1,
    "cl" : 1,
    "br" : 1,
    "i" : 1,
    "so4" : 2,
    "no3" : 1,
    "cio3" : 1,
    "cio4" : 1,
    "ch3coo" : 1,

}

ionMass = {
    "li" : 6.941, # 0
    "mg" : 24.305, # 1
    "ca" : 40.078, # 2
    "sr" : 87.620, # 3
    "ba" : 137.33, # 4
    "fe" : 55.845, # 5
    "hg2" : 200.59, # 6
    "pb" : 207.20, # 7
    "cu" : 63.546, # 8
    "ag" : 107.87, # 9
    "tl" : 204.38, # 10
    "ra" : 227.00, #11
    "f" : 18.998, # 12
    "cl" : 35.453, # 13
    "br" : 79.904, # 14
    "i" : 126.90, # 15
    "so4" : 96.06, # 16
    "rb" : 000000,
    "cs" : 000000,
    "nh4" : 18.04,
    "no3" : 62.0049,
    "cio3" : 83.45,
    "cio4" : 99.45,
    "ch3coo" : 60.05,
    "rbcio4": 232.35,
    "cscio4": 232.35,
    "agch3coo": 166.9122,
    "hg2(ch3coo)2": 318.678,
    ""
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
   if NUMBER < 0 or NUMBER == 0:
       print("This value can't be negative or zero! ")
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
    ION = input("Please input a positive reacting ion: (no charges) ")
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
   ION = input("Please input a negative reacting ion: (no charges) ")
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
   CONCENTRATION = input("What is the concentration of the solution? (mol/L) ")
   CONCENTRATION = checkFloat(CONCENTRATION)
   CONCENTRATION = checkNeg(CONCENTRATION)
   return CONCENTRATION

def getVolume():
   '''
   requests for the volume of the mixture
   :return: (float)
   '''
   VOLUME = input("What is the volume of the solution? (L) ")
   VOLUME = checkFloat(VOLUME)
   VOLUME = checkNeg(VOLUME)
   return VOLUME

def askContinue():
    answer = input("Would you like to make another calculation? (y/n) ")
    if answer == "Y" or answer == "y" or answer == "":
        return True
    elif answer == "N" or answer == "n":
        exit()
    else:
        print("That was not y or n! ")
        askContinue()

### PROCESSING

def getMass(ION):
   '''
   get the mass depending on the ion they selected
   :param ION:
   :return:
   '''
   MASS = ionMass[ION]
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

def checkPossible(ionN, ionP, possibilities):
    TOGETHER = ionN + ionP
    for i in range(len(possibilities)):
        if TOGETHER == possibilities[i]:
            print("omg its possible")
            return True
    print("not possible :( ")
    return False

def balanceEquation(ionP, ionN):

    global positiveCharge, negativeCharge
    CHARGEP = positiveCharge[ionP]
    CHARGEN = negativeCharge[ionN]
    if CHARGEP > CHARGEN:
        coefficient = ("", 2)
        molarRatio = (1 , 2)
    elif CHARGEN > CHARGEP:
        coefficient = (2,"")
        molarRatio = (2 , 1)
    else:
        coefficient = ("", "")
        molarRatio = (1, 1)
    print(f" {coefficient[0]}{ionP} + {coefficient[1]}{ionN} = {ionP}{coefficient[0]}{ionN}{coefficient[1]}")
    return molarRatio


def limitReactantCal(molesP, molesN, ionN, ionP, coefficient):
    '''
    idk
    :param moles:
    :return:
    '''
    global positiveCharge, negativeCharge
    nN = molesP * (coefficient[1]/coefficient[0])

    IONNN = ionN
    IONNN.capitalize()
    IONPP = ionP
    IONPP.capitalize()

    if nN > molesN:
        print(f"The {IONNN} is the limiting reagent")
        return (molesN, coefficient[1])
    elif molesN > nN:
        print(f"The {IONPP} is the limiting reagent")
        return (molesP, coefficient[0])
    else:
        print("There is no limiting reagent, they are equal!")
        return (molesP, coefficient[1], coefficient[0])

def calMassPrecipitate(ionP, ionN, limitedReactant, coefficient):

    global ionMass
    MASS = limitedReactant[0] * (1 / limitedReactant[1])
    FINAL_MASS = MASS * ((ionMass[ionP] * coefficient[0]) + (ionMass[ionN] * coefficient[1]))
    print(MASS)
    print(FINAL_MASS)


### OUTPUTS
def intro():
    '''
    is the introduction of what this is
    :return: (none)
    '''
    print("""
    Welcome to the chemistry precipitate calculator! Here is the section of the solubility table you can choose from! 
    
    ------------------------------------------------------------------------
    |            | Group 1 Ions  |              |            |             |
    |            |     NH4       |              |            |             |
    |    Ions    |     NO3       |      F       |     Cl     |     SO4     |
    |            |     CIO3      |              |     Br     |             |
    |            |     CIO4      |              |     I      |             |
    |            |    CH3COO     |              |            |             |
    |------------|---------------------------------------------------------|
    |            |               |             |            |              |
    |            |               |             |            |              |
    |   Aqueous  |      most     |     most    |    most    |     most     |
    |            |               |             |            |              |
    |            |               |             |            |              |
    |------------|---------------|-------------|------------|--------------|     
    |            |               |     Li      |            |      Ca      |
    |            |     RbCIO4    |     Mg      |     Cu     |      Sr      |
    |            |     CsCIO4    |     Ca      |     Ag     |      Ba      |
    |   Solid    |    AgCH3COO   |     Sr      |     Hg2    |      Ag      |
    |            |  Hg2(CH3COO)2 |     Ba      |     Pb     |      Hg2     |
    |            |               |     Fe      |     Tl     |      Pb      |
    |            |               |     Hg      |            |      Ra      |
    |            |               |     Pb      |            |              |
    ------------------------------------------------------------------------  
                                       
                                       
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
        possible = checkPossible(ionN, ionP, possibilities)
        if possible == True:
            coefficient = balanceEquation(ionP, ionN)
            ionN.capitalize()
            ionP.capitalize()
            limitedReactant = limitReactantCal(molesP, molesN, ionN, ionP, coefficient)
            massPrecipitate = calMassPrecipitate(ionP, ionN, limitedReactant, coefficient)
        askContinue()


# WHEN YOU PRITN OUT THE ANSWER TO THE USER, MAKE SURE TO CONVERT THE cl or fe or whatever BACK INTO CAPITALIZATION. USING THE FUNCTION .capitalize() (capitalizes the first letter)


# I PLAN THIS TO BE A DISPLAY THING, WHERE IN THE MENU, YOU CAN TYPE "ELEMENTS"
DISPLAY = (("Lithium", 6.9410), ("Magnesium", 24.305), ("Calcium", 40.078), ("Strontium", 87.620), ("Barium", 137.33), ("Iron", 55.845), ("Mercury", 200.59), ("Lead", 207.20) , ("Copper", 63.546), ("Silver", 107.87), ("Thallium", 204.38), ("Fluorine", 18.998), ("Chlorine", 35.453), ("Bromine", 79.904), ("Iodine", 126.90), ("Sulfate", 96.06))
#if askDisplay True:
 #  for i in range(len(DISPLAY)):
  #     for j in range(len(DISPLAY)):
   #        print(f"Name: {DISPLAY[i][j]}")
    #       idk im gonna cry


