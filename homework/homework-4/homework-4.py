# Michael Martin
# 2/11/2017
# Homework #4

# Program Requirements
# ====================
# 1)  Program asks the user to input the name(s) of cities he/she wants to visit.
# 2)  Program asks the user how many cities he/she wants to visit.
# 3)  The user may input the same city twice, however, the program shall only
#     count unique inputs
# 4)  Capitalization is not required to be checked
# 5)  Once cities have been collected, the program shall print a sentence in
#     the following format:
#     "You would like to visit San Francisco as city 1 and San Diego as City 2
#     and Palo Alto as city 3 on your trip." and so on.
# 6)  The program will then take the previously created sentence string and
#     add 1 to each city number and then output the string with the update.
# 7)  The first sentence must be split into a list.
# 8)  Use 'isdigit()' to determine which list elements are digits.
# 9)  Add 1 to each list element that is identified as a digit.
# 10) Use 'join()' to join the new list elements together
# 11) You must use a for loop in your code

import sys

# this function asks the user how many cities he/she would like to visit.
def AskForNumberCities():
    num_cities = raw_input('How many different cities do you want to travel to?\n')
    # checking to see if the input is a number. Program stops if input is not.
    try:
        num_cities = int(num_cities)
    except ValueError:
        print 'You must enter a real, rational, non-zero number only!'
        sys.exit()
    else:
        'ok'
    return num_cities

# this function asks for the names of the cities he/she would like to visit.
def AskForCityNames(num_cities):
    list_length =   len(range(0,num_cities+1,1))
    city_list =     []
    # Using a for loop to check the input of each city...
    # Using checks against each input to ensure each is in an acceptable format
    for i in range(0,num_cities,1):
        city_name =     [raw_input("Enter the name of as city you'd like to visit:\n")]
        # checking if there is white space in the input
        if ' ' in city_name[0]:
            if city_name[0].strip() == '':
                print 'Your city names must contain letters'
                sys.exit()
            else:
                city_list = city_list + city_name
        # checking to see if input contains letters
        elif city_name[0].isalpha() == False:
            print 'Your city names must contain letters only.'
            sys.exit()
        else:
            city_list = city_list + city_name
    return city_list

# this function checks for duplicate entries. If there is a duplicate entry,
# then the first entry is removed from the list
def CheckForDuplicatesInList(city_list):
    length = len(city_list)
    for i in range(0,length,1):
        for j in range(1,length,1):
            if (city_list[i] == city_list[j]) & (i != j):
                city_list[i] = ""
            else:
                'ok'
    cities = city_list
    return cities

# this function take a final list of cities and creates the required sentence
# output
def CitiesToVisitSentence(cities):
    length =            len(cities)
    updated_cities =    filter(None,cities)
    trip_summary =      ''
    preamble =          'You would like to visit '
    end =               'on your trip.'
    for k in range(0,len(updated_cities),1):
        trip_summary = trip_summary + updated_cities[k] + ' as city ' + str(k+1) + ' and '
    trip_summary = preamble + trip_summary + end
    trip_summary = trip_summary.replace('and on your trip.',end)
    return trip_summary

# this function takes the previously generated sentence and adds one to each of
# the numeric values
def UpdateTripSentence(trip_sentence):
    trip_sentence_list =    trip_sentence.split()
    list_length =           len(trip_sentence_list)
    white_space =           ' '
    for ii in range(0,list_length,1):
        if trip_sentence_list[ii].isdigit() == True:
            integer_value = int(trip_sentence_list[ii])+1
            trip_sentence_list[ii] = str(integer_value)
        else:
            'skip'
    updated_trip_summary = white_space.join(trip_sentence_list)
    return updated_trip_summary

# running the functions
num_cities =        AskForNumberCities()
city_list =         AskForCityNames(num_cities)
cities =            CheckForDuplicatesInList(city_list)
sentence =          CitiesToVisitSentence(cities)
sentence_update =   UpdateTripSentence(sentence)
print sentence
print sentence_update
