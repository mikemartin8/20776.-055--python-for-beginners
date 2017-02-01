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
        letter = raw_input('Enter either one lower case or upper case letter: ')
        if letter == 'quit':
            break
        elif len(letter) == 1:
            IsVowel(letter)
        else:
            print "too many letters!"

## Creating the function "IsVowel(letter)". This function shall take the user
## defined input to determine whether or not it is a vowel or not. If it is not
## a vowel, it shall print that. If it is a vowel, it will call two additional
## functions, "IsLowerCase(letter") & "IsUpperCase(letter)" to determine
## whether or not the vowel is upper case or lower case.
def IsVowel(letter):
    if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or letter == 'o'or letter == 'O' or letter == 'u'  or letter == 'U':
        status = 'True: the input letter is a vowel.'
        print status
        IsLowerCaseVowel(letter)
        IsUpperCaseVowel(letter)
    else:
        status = 'False: your input was not a vowel.\n'
        print status

## Creating the function "IsLowerCaseVowel(letter)" to determine if an input is
## a lower case vowel or not.
def IsLowerCaseVowel(letter):
    vowels = ('a','e','i','o','u')
    if letter.startswith(vowels) == 1:
        print 'True: the input letter is a lower case vowel.'
    else:
        print 'False: the input letter is NOT a lower case vowel.'

## Creating the function "IsUpperCaseVowel(letter)" to determine if an input is
## a upper case vowel or not.
def IsUpperCaseVowel(letter):
    vowels = ('A','E','I','O','U')
    if letter.startswith(vowels) == 1:
        print 'True: the input letter is an upper case vowel.\n'
    else:
        print 'False: the input letter is NOT an upper case vowel.\n'
       
AskForLetter()
