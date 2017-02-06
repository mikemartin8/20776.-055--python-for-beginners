## Michael Martin
## 2/3/2017
## Homework #3

## Write a program that takes a 3-word phrase and then converts the words to
## Pig Latin.
##
## The rule for converting to Pig Latin is as follows: Take the first letter
## of the English word, and put it at the end of the word, and then appends it
## with the letters "ay". The only exception is that if the first letter of the
## word starts with a vowel. In which case, the word remains as is, but is
## appended with the letters "hay".

vowels = ['A','a','E','e','I','i','O','o','U','u']

def AskUserForSentence():
    while True:
        sentence =              raw_input('Enter a three worded sentence without any punctuation.\n')
        lower_case_sentence =   LowercaseSentence(sentence)
        listed_sentence =       SplitSentenceIntoList(lower_case_sentence)
        if sentence == 'quit':
            break
        elif len(listed_sentence) < 3:
            print 'Your sentence does not have enough words!'
        elif len(listed_sentence) > 3:
            print 'Your sentence has too many words!'
        else:
            print '...'
            blah = ConvertWordToPigLatin(listed_sentence)
            print blah

## function to force sentence to be lower case
def LowercaseSentence(sentence):
    lower_case_sentence = sentence.lower()
    return lower_case_sentence

## function that splits the sentence into a list
def SplitSentenceIntoList(sentence):
    listed_sentence = sentence.split()
    return listed_sentence

## function to convert your words to Pig Latin
def ConvertWordToPigLatin(listed_sentence):
    first_word =    listed_sentence[0]
    second_word =   listed_sentence[1]
    third_word =    listed_sentence[2]
    if first_word.isalpha() == False or second_word.isalpha() == False or third_word == False:
        print 'Your sentence contain letters only!'
    else:
        return
AskUserForSentence()
##def ConvertWordToPigLatin
##def PrintThreeWordPhrase
