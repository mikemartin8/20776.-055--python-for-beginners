## Michael Martin
## 1/31/2017
## Homework #2

## Create the function "AskForLetter():" such that the function repeatedly
## asks the user for a single letter until the user types "quit" to exit the
## program or they have entered a vowel. Use the python function "len" to call
## a second function called "IsVowel(letter):" if the output of "len" = 1.
## Finally, the function shall output the input letter if it is a vowel.

def AskForLetter():
    while True:
        letter =    raw_input('Enter either one lower case or upper case letter: ')
        if letter == 'quit':
            break
        elif len(letter) == 1:
            IsVowel(letter)
        else:
            print "too many letters!"
                
def IsVowel(letter):
    if letter == ('a'):
        status = 'True'
        print status
    elif letter == ('e'):
        status = 'True'
        print status
    elif letter == ('i'):
        status = 'True'
        print status
    elif letter == ('o'):
        status = 'True'
        print status
    elif letter == ('u'):
        status = 'True'
        print status
    else:
        status = 'False'
        print status

IsVowel('p')
