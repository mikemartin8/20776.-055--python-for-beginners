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
    num_cities = '4' #raw_input('How many different cities do you want to travel to?\n')
    if num_cities.isdigit() == False:
        print 'You must enter a real, rational, non-zero number only!'
    else:
        print num_cities
    return int(num_cities)

def AskForCityNames(num_cities):
    list_length =   len(range(0,num_cities+1,1))
    city_list =          []
    for i in range(0,num_cities,1):
        print i
        city_name =     [raw_input("Enter a new city you'd like to visit:\n")]
        print 'length of city list',len(city_name)
        city_list =     city_list + city_name
    print city_list
    return city_list

def CheckForDuplicatesInList(city_list):
    length = len(city_list)
    for i in range(0,length,1):
        for j in range(1,length,1):
            if i == j:
                print 'skipping checks at same indeces'
            elif (city_list[i] == city_list[j]) & (i != j):
                print 'No duplicate entries'
            else:
                print i,j

        
blah = AskForNumberCities()
AskForCityNames(blah)
