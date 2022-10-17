#h_array_list_exercises.py

'''
title: array list practice
author: kliment lo
date: 10/17/2022
'''
from random import randrange
print('''
-------------------------------------------------------------------------------------------------------------
Exercise 1:''')
def exercise1():
    A_LIST = [100, 200, 300, 400, 500]
    NEW_LIST = []
    for i in range(len(A_LIST)-1, -1, -1):
        NEW_LIST.append(A_LIST[i])
    print(NEW_LIST)
exercise1()
print('''-------------------------------------------------------------------------------------------------------------
Exercise 2:''')
def exercise2():
    LIST1 = ["M", "na", "i", "Klim"]
    LIST2 = ["y ", "me ", "s ", "ent "]
    LIST3 = []
    for i in range(len(LIST1)):
        LIST3.append(LIST1[i] + LIST2[i])
    print(LIST3)
exercise2()

print('''-------------------------------------------------------------------------------------------------------------
Exercise 3:''')
def exercise3():
    A_LIST = [1, 2, 3, 4, 5, 6, 7]
    NEW_LIST = []
    for i in range(len(A_LIST)):
        NEW_LIST.append(A_LIST[i] ** 2)
    print(NEW_LIST)
exercise3()
print('''-------------------------------------------------------------------------------------------------------------
Exercise 4:''')
def exercise4():
    LIST1 = ["Hello ", "take "]
    LIST2 = ["Dear", "Sir"]
    LIST3 = []
    for i in range(len(LIST1)):
        LIST3.append(LIST1[i] + LIST2[i])
        LIST3.append(LIST1[i] + LIST2[i])
    print(LIST3)
exercise4()
