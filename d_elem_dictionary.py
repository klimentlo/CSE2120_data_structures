#d_elem_dictionary.py
'''
title: chemical element dictionary
author: kliment
date: 10/6/2022
'''

ELEM_NAMES = {
    "H" : "Hydrogen",
    "He" : "Helium",
    "Na" : "Sodium",
    "Cl" : "Chlorine"
}

ELEM_NUM = {
    "H" : 1,
    "He" : 2,
    "Na" : 11,
    "Cl" : 17
}

ELEM_MASS = {
    "H" : 1.01,
    "He" : 4.00,
    "Na" : 22.99,
    "Cl" : 35.46
}

ATOMIC_NUM = {
    "H" : 1,
    "He" : 2,
    "Na" : 11,
    "Cl" : 17
}

def intro():
    '''
    displays welcome text for the user
    :return:
    '''
    print('''
Welcome to the Periodic Table of Elements!*
Please use the menu below to see my vast wealth of knowledge

*Not all elements are represented 
''')

def menu():
    '''
    User selects the types of information they want to know
    :return: (int)
    '''
    print("""
1. Element Names
2. Element Numbers
3. Element Masses    
4. Element Atomic Number 
""")
    CHOICE = input("Choose the category of information you with to know: ")
    try:
        CHOICE = int(CHOICE)
        if CHOICE > 0 and CHOICE < 5:
            return CHOICE
        else:
            print("Please choose a number from the menu! ")
            return menu()
    except ValueError:
        print("That was not one of the options! ")
        NEW_CHOICE = input(" Please choose a valid number! ")
        return NEW_CHOICE

def askContinue():
    '''
    asks if the user would like to rerun the program
    :return: (bool) # true/false
    '''
    AGAIN = input("Learn more? (y/n) ")
    if AGAIN == "y" or AGAIN == "Y" or AGAIN == "":
        return True
    elif AGAIN == "n" or AGAIN == "N":
        return False
    else:
        print("Please choose y or n ")
        return askContinue()

if __name__ == "__main__":
    """
    print(ELEM_NAMES["Na"])
    print(ELEM_NUM["Na"])
    print(ELEM_MASS["Na"])
    print(f"The ionic compound of {ELEM_NAMES['Na']} and {ELEM_NAMES['Cl']} is NaCl and has a molar mass of {ELEM_MASS['Na'] + ELEM_MASS['Cl']} g/Mol. ")
    SODIUM = "Na"
    print(ELEM_MASS[SODIUM])

    ELEMENTS = ("H", "He", "Na", "Cl")
    print(ELEM_NAMES[ELEMENTS[1]])
    for i in range(len(ELEMENTS)):
        print(ELEM_NAMES[ELEMENTS[i]])
    """
    intro()
    while True:
        CHOICE = menu()
        if CHOICE == 1:
            print(ELEM_NAMES)
        elif CHOICE == 2:
            print(ELEM_NUM)
        elif CHOICE == 3:
            print(ELEM_MASS)
        else:
            print(ATOMIC_NUM)
        if not askContinue():
            exit()