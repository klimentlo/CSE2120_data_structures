# i_precipitate_calculator.py

'''
title: precipitate calculator
author: kliment lo
date: 10/18/2022
'''
import math

# --- DICTIONARIES/TUPLE/ARRAY SETUP --- #
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
}

negativeCharge = {
    "f" : 1,
    "cl" : 1,
    "br" : 1,
    "i" : 1,
    "so2" : 2,
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
    "f" : 18.998, # 11
    "cl" : 35.453, # 12
    "br" : 79.904, # 13
    "i" : 126.90, # 14
    "so" : 96.06, # 15
}
# --- FUNCTIONS --- #

### INPUTS

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
    return ION

def getConcentration():
    '''
    requests for the concentration of the mixture
    :return: (float)
    '''
    CONCENTRATION = input("Please input how concentrated the fluid is: ")
    return CONCENTRATION

def getVolume():
    '''
    requests for the volume of the mixture
    :return: (float)
    '''
    VOLUME = input("Please input how many liters of fluid there is: ")
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
    while True:
       ion = positiveIon()
       positiveVolume = getVolume()
       positiveConcentration = getConcentration()
       mass = getMass(ion)

#NEW CONTENT
       molesP = moleCal(volumeP, concentrationP)
       molesN = moleCal(volumeN, concentrationN)
       limitedReactant = limitReactantCal(ionP, ionN, molesN, molesP)

def moleCal(volume, concentration):
    '''
    calculates the amount of moles in the ion
    :param MOLES:
    :return:
    '''
    moles = volume * concentration
    return moles

def limitReactantCal(ionP, ionN, molesN, molesP):
    '''
    idk
    :param moles:
    :return:
    '''
    global positiveCharge, negativeCharge
    NEGREACTANT = molesP * (negativeCharge[ionN]/positiveCharge[ionP])
    if NEGREACTANT < molesN:
        coefficient[1] = coefficient[1] + 1
coefficient = []
coefficient = [1, 1, 1]

# I PLAN THIS TO BE A DISPLAY THING, WHERE IN THE MENU, YOU CAN TYPE "ELEMENTS"
DISPLAY = (("Lithium", 6.9410), ("Magnesium", 24.305), ("Calcium", 40.078), ("Strontium", 87.620), ("Barium", 137.33), ("Iron", 55.845), ("Mercury", 200.59), ("Lead", 207.20) , ("Copper", 63.546), ("Silver", 107.87), ("Thallium", 204.38), ("Fluorine", 18.998), ("Chlorine", 35.453), ("Bromine", 79.904), ("Iodine", 126.90), ("Sulfate", 96.06))
if askDisplay True:
    for i in range(len(DISPLAY)):
        for j in range(len(DISPLAY)):
            print(f"Name: {DISPLAY[i][j]}")
            idk im gonna cry

