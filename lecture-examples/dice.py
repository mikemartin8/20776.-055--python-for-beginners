'''
dice.py - Python Class that has one method that will use the function from
die.py to roll the die.
'''

import die

class Dice:

    def RollDie(self):
        return die.RollDie()

def Run():
    '''Function that will run if Class run from commandline.
This function will test the class by rolling the die 4 times.
'''
    the_die = Dice()
    for roll in range(4):
        print the_die.RollDie()
        
if __name__=='__main__':
    Run()
    
    
