5## Michael Martin
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

vowels = ['a','e','i','o','u']

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
            pig_latin = ConvertWordToPigLatin(listed_sentence)
            PrintThreeWordPhrase(pig_latin[0],pig_latin[1],pig_latin[2])
            
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
        if (first_word[0] in vowels) == 1:
            first_pig_latin = first_word + 'hay'
        else:
            first_pig_latin = first_word[1:len(first_word)] + first_word[0] + 'ay'
        if (second_word[0] in vowels) == 1:
            second_pig_latin = second_word + 'hay'
        else:
            second_pig_latin = second_word[1:len(second_word)] + second_word[0] + 'ay'
        if (third_word[0] in vowels) == 1:
            third_pig_word = third_word + 'hay'
        else:
            third_pig_word =  third_word[1:len(third_word)] + third_word[0] + 'ay'
        return (first_pig_latin, second_pig_latin, third_pig_word)

## function to print the three words in Pig Latin
def PrintThreeWordPhrase(word_one,word_two,word_three):
    print word_one , word_two , word_three

AskUserForSentence()
