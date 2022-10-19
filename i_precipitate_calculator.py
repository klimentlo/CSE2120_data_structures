# i_precipitate_calculator.py

'''
title: precipitate calculator
author: kliment lo
date: 10/18/2022
'''
import math

# --- DICTIONARIES --- #
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
    "li" : 6.9410,
    "mg" : 24.305,
    "ca" : 40.078,
    "sr" : 87.620,
    "ba" : 137.33,
    "fe" : 55.845,
    "hg" : 200.59,
    "pb" : 207.20,
    "cu" : 63.546,
    "ag" : 107.87,
    "tl" : 204.38,
    "f" : 18.998,
    "cl" : 35.453,
    "br" : 79.904,
    "i" : 126.90,
    "so2" : 64.066,
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
