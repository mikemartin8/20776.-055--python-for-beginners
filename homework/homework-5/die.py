# die.py

import random
def RollDie():
    die_num = random.randint(1,6)
    return die_num
    print die_num

if __name__ == '__main__':
    die = RollDie()   
    print die
