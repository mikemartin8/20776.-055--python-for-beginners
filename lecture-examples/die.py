'''
lab_10_exercises_num_1.py - Module that contains a function called RollDie() that will
roll a six-sided die.
'''

import random

def RollDie():
    '''Updates the die with a random roll.'''
    value = 1 + random.randrange(6)
    return value

def Run():
    '''Function that will run if module run from commandline.
This function will test the module by rolling the die twice.
'''
    
    for n in range(1):
         print 'Number rolled on first die is',RollDie()
         print 'Number rolled on second die is',RollDie()

if __name__=='__main__':
    Run()
