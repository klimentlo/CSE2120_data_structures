 #e_encryption.py
'''
title: encrypting text
author: kliment lo
date-created: 10-11-2022
'''

'''
this program will use a keyboard cipher to encrypt text
a keyboard cipher uses a keyboard containing no duplicate letters to shift the letters of the alphabet to different positions
'''

# Keyword = stinky

CODE = {
    "a" : "s",
    "b" : "t",
    "c" : "i",
    "d" : "n",
    "e" : "k",
    "f" : "y",
    "g" : " ",
    "h" : "a",
    "i": "b",
    "j": "c",
    "k": "d",
    "l": "e",
    "m": "f",
    "n": "g",
    "o": "h",
    "p": "j",
    # j us used to represent p because i is in our keyword and is already used to represent c
    "q": "l",
    "r": "m",
    "s": "o",
    "t": "p",
    "u": "q",
    "v": "r",
    "w": "u",
    "x": "v",
    "y": "w",
    "z": "x",
    " ": "z",
}

### --- FUNCTIONS --- ###

### INPUTS
# user inputs a message
def getMessage():
    '''
    user inputs a secret message
    :return: (str)
    '''
    MESSAGE = input("Enter message to be encrypted: ")
    return MESSAGE

### PROCESSING
# message will be encrypted
def encryptMessage(TEXT):
    '''
    encrypt message with the code dictionary
    :param TEXT: (str)
    :return: (str)
    '''
    global CODE
    TEXT_LIST = []
    for i in range(len(TEXT)):
        TEXT_LIST.append(TEXT[i])
    print(TEXT_LIST)
    for i in range(len(TEXT_LIST)):
        if TEXT_LIST[i] != " ":
            TEXT_LIST[i] = CODE[TEXT_LIST[i]]
            #transforms input text to encrypted value from our keyboard cipher dictionary
    print(TEXT_LIST)
    ENCRYPTED = "".join(TEXT_LIST)
    # joins all of the things together so its a word or sentence and not ['h', 'e', 'l', etc.]
    print(ENCRYPTED)
    return ENCRYPTED
### OUTPUTS
# outputs the encrypted messages
def displayMessage(TEXT):
    '''
    prints the message
    :param TEXT: (str)
    :return: (none)
    '''
    print(f"The encrypted message is {TEXT}")

# --- MAIN PROGRAM --- #
if __name__ == "__main__":
    SECRET = getMessage()
    ENCRYPTED_SECRET = encryptMessage(SECRET)