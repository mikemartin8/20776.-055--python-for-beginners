'''
lab_8_exercises_num_1_answer.py
'''

def CalcAverage(ages):

    return sum(ages) / len(ages)

def CalcMax(ages):

    return max(ages)

def CalcMin(ages):

    return min(ages)

def SortList(ages):

    return sorted(ages)


def AskForAges():

    ages = []
    stop = False
    
    while stop == False:
        raw_age = raw_input('What is age of family member? Type "quit" when finished')
        if raw_age != 'quit':
            try:
                int_age = int(raw_age)
                ages.append(int_age)
            except ValueError:
                print 'The age you entered is not a valid integer'
        else:
            stop = True

    return ages

def GenerateReport(ages):

    print 'The original input list of ages are:',ages

    print 'The minimum age is:',CalcMin(ages)

    print 'The maximum age is:',CalcMax(ages)

    print 'The sorted list of ages is:',SortList(ages)

    print 'The average of the ages is:',CalcAverage(ages)

    print 'The original input list of ages are:',ages

    


def Run():

    ages = AskForAges()
    GenerateReport(ages)


Run()
            
