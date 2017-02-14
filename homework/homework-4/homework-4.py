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


def AskForNumberCities():
    num_cities = '1' #raw_input('How many different cities do you want to travel to?\n')
    if num_cities.isdigit() == False:
        print 'You must enter a real, rational, non-zero number only!'
    else:
        'ok'
    return int(num_cities)

def AskForCityNames(num_cities):
    list_length =   len(range(0,num_cities+1,1))
    city_list =          []
    for i in range(0,num_cities,1):
        city_name =     [raw_input("Enter a new city you'd like to visit:\n")]
        city_list =     city_list + city_name
    return city_list

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

def CitiesToVisitSentence(cities):
    length =        len(cities)
    trip_summary =  ''
    for i in range(0,length,1):
        if cities[i] == "":
            'is blank'
        else:
            'do'"You would like to visit " + trip_summary
    updated_cities =    filter(None,cities)
    preamble =          'You would like to visit '
    end =               'on your trip.'
    trip_summary =      ''
    for j in range(0,len(updated_cities),1):
        trip_summary = trip_summary + updated_cities[j] + ' as city ' + str(j+1) + ' and '
    trip_summary = preamble + trip_summary + end
    print trip_summary
    return trip_summary

def UpdateTripSentence(trip_sentence):
    trip_sentence_list =    trip_sentence.split()
    list_length =           len(trip_sentence_list)
    for k in range(0,list_length,1):
        if trip_sentence_list[k].isdigit() == True:
            print trip_sentence_list[k]
            integer_value = int(trip_sentence_list[k])+1
            print integer_value
            trip_sentence_list[k] = str(integer_value)
            print trip_sentence_list[k]
            print 'something'
        else:
            'skip'
    return trip_sentence
            
        
blah =      AskForNumberCities()
city_list = AskForCityNames(blah)
cities =    CheckForDuplicatesInList(city_list)
sentence =  CitiesToVisitSentence(cities)
a = UpdateTripSentence(sentence)
print a

#     "You would like to visit San Francisco as city 1 and San Diego as City 2
#     and Palo Alto as city 3 on your trip."
