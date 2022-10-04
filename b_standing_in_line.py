#b_standing_in_line.py
'''
title: line up system
author: kliment lo
date-created: 10-4-2022
'''

# --- SUBROUTINE --- #

# --- INPUTS
def menu():
    '''
    User selects a function of teh program
    :return: (int)
    '''
    print('''
1. Stand in line
2. Serve a customer
3. Cut in Line
4. Exit
''')
    CHOICE = input("> ")
    return int(CHOICE)
    # make sure to use a function like checkInt() when writing your program for an summative project!

def askName():
    '''
    asks for teh customer's name
    :return: (str)
    '''
    return input("Please enter your name: ")

# --- PROCESSING
def addToLine(NAME, LINE):
    '''
    Adds the name fot the customer to the line
    :param NAME: (str)
    :param LINE: (list) List of customers in the line
    :return:  (list) updated list of customers
    '''
    LINE.append(NAME)
    # .append() adds an item to the end of the list
    return LINE

def serveNextCustomer(LINE):
    '''
    return the next customer in line
    :param LINE: (list) List of customers
    :return: (str) the next customer in the line
    '''
    CUSTOMER = LINE.pop(0) # gets the name of the first customer in line
    return CUSTOMER

def cutInLine(NAME, LINE):
    '''
    Places their name at the front of the line
    :param NAME: (str)
    :param LINE: (line)
    :return: (line)
    '''
    LINE.insert(0, NAME)
    return LINE
# --- OUTPUTS
def displayLineLength(LINE):
    '''
    display to customer where they are in line
    :param LINE: (list) List of customers in line
    :return: (none)
    '''
    print(f"{LINE[-1]}, you are the {len(LINE)} person in line. ")
    # LINE [-1 is the last name in the list]
    # len(LINE) is used to get the number of nodes in a data structure

def displayNextCustomer(CUSTOMER):
    '''
    displays text to indicate the next customer
    :param CUSTOMER: (str)
    :return: (none)
    '''
    print(f"The next customer to be served is {CUSTOMER}. ")

# --- MAIN PROGRAM --- #
if __name__ == "__main__":

    # --- VARIABLES --- #
    CUSTOMERS = []
    # CUSTOMERS is the list where new names will be added and served customers will removed (.popped)

    while True:
        ### INPUTS
        CHOICE = menu()

        ### PROCESSING
        if CHOICE == 1:
            NAME = askName()
            CUSTOMERS = addToLine(NAME, CUSTOMERS)
            displayLineLength(CUSTOMERS)
            print(CUSTOMERS)
        elif CHOICE == 2:
            if len(CUSTOMERS) > 0:
                NOW_SERVING = serveNextCustomer(CUSTOMERS)
                # serveNextCustomer .pops the first name off the list and returns it
                displayNextCustomer(NOW_SERVING)
                print(CUSTOMERS)
            else:
                print("There is no one in line! ")
        elif CHOICE == 3:
            NAME = askName()
            CUSTOMERS = cutInLine(NAME, CUSTOMERS)
            displayLineLength(CUSTOMERS)
            print(CUSTOMERS)
        else:
            exit()

        # a limitation of storing data in variables in your program and not in files external to program (we'll do this in our next module) is that all data is lost when you end/re-run the program.
