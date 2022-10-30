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
    creates all the possible precipitates on the soluability table, and storing them in a 2D array
    :return: (list)
    '''
    # make an empty list for all the cards (if we make a new variable and copy the "CARDS" list onto it and change the new variable list, it will also change the original list. But if we make an empty list, then it wont change both.

    # make an empty array for each suit and append cards to each suit, then add them all together to make the full dark
    RowNh = []
    RowNh.append((1, 1)) # works differently from the rest of the groups 1 = clo4, 1 = rb
    RowNh.append((1, 6))  # 1 = clo4, 6 = cs
    RowNh.append((5, 9)) # 5 = ch3coo, 9 = ag
    RowNh.append((5, 10)) # 5 = ch3coo, 10 = hg2

    # sorry for the really random numbers and such. There was a change in plans of how to calculate the first column, so i had to get rid of some stuff and got lazy changing them back to nice numbers as there would be a good chance i mess up the code and have to try to decode it for a few hours :'(
    RowF = [] # F = 13
    for i in range(8):
        RowF.append((13, i+1))  #the negative ion F is identified as 13

    RowCl = []    # Cl = 14 Br = 15, I = 16
    for j in range(3):
        for i in range(5):
            RowCl.append((j+14, i+1)) # i = posIonCl dictionary

    RowSo = [] #So = 17
    for i in range(7):
        RowSo.append((17, i+1))
    Soluable = displayPositibilities(RowNh, RowF, RowCl, RowSo) # prints out the tuples as a string instead of numeros
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
        ROWNH.append(negIons[RowNh[i][0]] + posIonsNh[RowNh[i][1]]) #runs the tuples from that specific group through the dictionary and gets a solid mixture

    ROWF = []
    for i in range(len(RowF)):
        ROWF.append(negIons[RowF[i][0]] + posIonsF[RowF[i][1]]) # same thing as ^^

    ROWCL = []
    for i in range(len(RowCl)):
        ROWCL.append(negIons[RowCl[i][0]] + posIonsCl[RowCl[i][1]])

    ROWSO = []
    for i in range(len(RowSo)):
        ROWSO.append(negIons[RowSo[i][0]] + posIonsSo[RowSo[i][1]])


    POSSIBILITIES = ROWNH + ROWF + ROWCL + ROWSO
    return POSSIBILITIES
        #




# --- FUNCTIONS --- #

### INPUTS

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
   :return: (int)
   '''
   ION = ION.lower()
   CHARGE = negativeCharge[ION]
   return CHARGE

def moleCal(volume, concentration):
   '''
   calculates the amount of moles in the ion
   :param MOLES: (float)
   :return: (float)
   '''
   moles = volume * concentration
   return moles

def checkPossible(ionN, ionP, possibilities):
    '''
    checks if the combination is possible to create a solid
    :param ionN: (str)
    :param ionP: (str)
    :param possibilities: (str)
    :return: (bool)
    '''
    TOGETHER = ionN + ionP
    for i in range(len(possibilities)):
        if TOGETHER == possibilities[i]: #is the combination the user input one of the possible combinations that was created in the list "possibilities"
            return True # if yes, continue calculations
    print("The two ions will not create a precipitate. ")
    return False # if no, return false

def balanceEquation(ionP, ionN):
    '''
    balances the equation
    :param ionP: (str)
    :param ionN: (str)
    :return: (tuple)
    '''
    global positiveCharge, negativeCharge
    CHARGEP = positiveCharge[ionP] # get the charge of the positive ion
    CHARGEN = negativeCharge[ionN] # get charge of the negative ion
    if CHARGEP > CHARGEN: #if chargeP is bigger than chargeN
        coefficient = ("", 2)
        molarRatio = (1 , 2) # ratio is 1 : 2
    elif CHARGEN > CHARGEP: # if chargeN is bigger than chargeP
        coefficient = (2,"")
        molarRatio = (2 , 1) # ratio is 2 : 1
    else:
        coefficient = ("", "")
        molarRatio = (1, 1)

    if ionP == "nh4": # if it's nh4
        IONPP = ionP.upper() #capitalize everything
    else:
        IONPP = ionP.capitalize() # capitalize first letter

    if ionN == "clo3" or ionN == "clo4" or ionN == "ch3coo" or ionN == "so4" or ionN == "no3":
        IONN = ionN.upper() # capitalize entire thing
    else:
        IONN = ionN.capitalize() # capitalize first thing

    print(f" {coefficient[0]}{IONPP} + {coefficient[1]}{IONN} = {IONPP}{coefficient[0]}{IONN}{coefficient[1]}")
    return molarRatio


def limitReactantCal(molesP, molesN, ionN, ionP, coefficient):
    '''
    calculates which is the limiting reagent
    :param molesP: (float)
    :param molesN: (float)
    :param ionN: (str)
    :param ionP: (str)
    :param coefficient:  (tuple)
    :return: (list)
    '''
    global positiveCharge, negativeCharge
    nN = molesP * (coefficient[1]/coefficient[0]) # multiplies the # of molesP by the molar ratio
    noLim = [molesP, coefficient[1], coefficient[0]]

    if ionP == "nh4":
        IONP = ionP.upper()
    else:
        IONP = ionP.capitalize()

    if ionN == "clo3" or ionN == "clo4" or ionN == "ch3coo" or ionN == "so4" or ionN == "no3":
        IONN = ionN.upper()
    else:
        IONN = ionN.capitalize()

    if nN > molesN: # if # of negative moles required is > than the amount of molesN we have, molesN is the limiting reagant
        print(f"The {IONN} is the limiting reagent")
        return [molesN, coefficient[1]] # used in the calMassPrecipitate function
    elif molesN > nN:
        print(f"The {IONP} is the limiting reagent") #
        return [molesP, coefficient[0]]
    else:
        print("There is no limiting reagent, they are equal!")
        noLim.pop()
        return noLim

def calMassPrecipitate(ionP, ionN, limitedReactant, coefficient):
    '''
    calculates the mass of the precipitate
    :param ionP: (str)
    :param ionN: (str)
    :param limitedReactant: (list)
    :param coefficient: (tuple)
    :return: (float)
    '''
    global ionMass
    MASS = limitedReactant[0] * (1 / limitedReactant[1]) #mass of the reactant
    FINAL_MASS = MASS * ((ionMass[ionP] * coefficient[0]) + (ionMass[ionN] * coefficient[1])) # the final mass of the entire mixture
    return FINAL_MASS

### OUTPUTS

# librarys to create all the possible things that create a solid
negIons = {
    1 : "clo4",
    2 : "li",
    3 : "na",
    4 : "k",
    5 : "ch3coo",
    6 : "cs",
    7 : "fr",
    13 : "f",
    14 : "cl",
    15 : "br",
    16 : "i",
    17 : "so4"
}

posIonsNh = {
    1: "rb",
    2: "li",
    3: "na",
    4: "k",
    6: "cs",
    7: "fr",
    8: "nh4",
    9: "ag",
    10: "hg2",
    11: "h"
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
    "nh4": 1,
    "rb": 1,
    "cs": 1,
    "h" :  1,
    "na" : 1,
    "k" : 1,
    "fr" : 1,
}

negativeCharge = {
    "no3" : 1,
    "clo3" : 1,
    "clo4" : 1,
    "ch3coo" : 1,
    "f" : 1,
    "cl" : 1,
    "br" : 1,
    "i" : 1,
    "so4" : 2,
}

ionMass = {
    "li" : 6.941, # 0
    "mg" : 24.305, # 1
    "ca" : 40.078, # 2
    "sr" : 87.620, # 3
    "ba" : 137.33, # 4
    "fe" : 55.845, # 5
    "hg2" : 401.18, # 6
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
    "h": 1.00784,
    "na": 22.989769,
    "k": 39.0983,
    "rb": 85.4678,
    "cs": 132.90545,
    "fr": 223,
    "nh4" : 18.04,
    "no3" : 62.0049,
    "clo3" : 83.45,
    "clo4" : 99.45,
    "ch3coo" : 59.05, #or 60.05 idk
}


def intro():
    '''
    is the introduction of what this is
    :return: (none)
    '''
    print("""
    Welcome to the chemistry precipitate calculator! Here is the section of the solubility table you can choose from!                                        
                                               (diatomic ions not included)                         """)

def menu():
    print("""
    
    
                                 Solubility of Some Common Iconic Compounds in Water at 298.15K
                            ------------------------------------------------------------------------
                            |            | Group 1 Ions  |              |            |             |
                            |            |     NH4       |              |            |             |
                            |    Ions    |     NO3       |      F       |     Cl     |     SO4     |
                            |    (-)     |     CLO3      |              |     Br     |             |
                            |            |     CLO4      |              |     I      |             |    
                            |            |    CH3COO     |              |            |             |
                            |------------|---------------------------------------------------------|
                            |            |               |              |            |             |
                            |   Aqueous  |               |              |            |             |
                            |            |      most     |     most     |    most    |     most    |
                            |   (very)   |               |              |            |             |
                            |  (soluble) |               |              |            |             |
                            |------------|---------------|--------------|------------|-------------|     
                            |            |               |     Li       |            |      Ca     |
                            |            |     RbCLO4    |     Mg       |     Cu     |      Sr     |
                            |            |     CsCLO4    |     Ca       |     Ag     |      Ba     |
                            |   Solid    |    AgCH3COO   |     Sr       |     Hg2    |      Ag     |
                            |    (+)     |  Hg2(CH3COO)2 |     Ba       |     Pb     |      Hg2    |
                            |            |               |     Fe       |     Tl     |      Pb     |
                            |            |               |     Hg       |            |      Ra     |
                            |            |               |     Pb       |            |             |
                            ------------------------------------------------------------------------  
    
""")

def displayMass(ionP, ionN, massPrecipitate):
    '''displays the final mass'''

    if ionP == "nh4":
        IONP = ionP.upper()
    else:
        IONP = ionP.capitalize()

    if ionN == "clo3" or ionN == "clo4" or ionN == "ch3coo" or ionN == "so4" or ionN == "no3":
        IONN = ionN.upper()
    else:
        IONN = ionN.capitalize()

    massPrecipitate = round(massPrecipitate,2)
    print(f"The mass of {IONP + IONN} is {massPrecipitate} grams. ")


# --- MAIN PROGRAM --- #
if __name__ == "__main__":
    intro() #displays info
    possibilities = possibilities() # creates all the possible combinations of mixtures that would create a precipitate (all of the combinations that are on the displayed on the outputted soluability table
    while True:
        menu()
        #get and calculate all things needed about positive ion
        ionP = positiveIon() # user inputs positive ion
        massP = getMass(ionP) # gets the mass of that ion
        chargeP = getChargeP(ionP) # gets the charge of that ion
        volumeP = getVolume() # requests for volume of that ion
        concentrationP = getConcentration() #requests for concentration of that ion
        #get and calculate all things needed about negative ion
        ionN = negativeIon() # user inputs negative ion
        massN = getMass(ionN) # gets the mass of that ion
        chargeN = getChargeN(ionN) # gets the charge of that ion
        volumeN = getVolume() # requests for the volume of that ion
        concentrationN = getConcentration() # requests for concentration of that ion
        #calculates total moles per ion
        molesP = moleCal(volumeP, concentrationP)
        molesN = moleCal(volumeN, concentrationN)
        #checks if the mixture of the two ions creates a precipitate
        possible = checkPossible(ionN, ionP, possibilities)
        if possible == True: # if it can, continue with code
            coefficient = balanceEquation(ionP, ionN) # gets the coefficient of the mixture
            limitedReactant = limitReactantCal(molesP, molesN, ionN, ionP, coefficient) # determintes which ion is the limiting reagent of this reaction
            massPrecipitate = calMassPrecipitate(ionP, ionN, limitedReactant, coefficient) # calculates the mass of the precipitate
            displayMass(ionP, ionN, massPrecipitate) # displays the final mass
        # ask if they want to do the calculation again
        askContinue()