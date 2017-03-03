'''
lab_8_exercises_num_2_answer.py
'''

list_1 = [1, 3, 5, 7, 9, 11]

list_2 = [2, 4, 6, 8, 10, 12]

def UpdateList(list_to_update, original_value, new_value):

    if original_value in list_to_update:
        index = list_to_update.index(original_value)
        list_to_update[index] = new_value
        return list_to_update
    else:
        print original_value,'cannot be updated since it is not in the list'

def DeleteElementInList(list_to_update, value_to_delete):

    if value_to_delete in list_to_update:
        list_to_update.remove(value_to_delete)
        return list_to_update
    else:
        print value_to_delete,'cannot be deleted since it is not in the list'

    

def ConcatenateLists(list_1, list_2):

    return list_1 + list_2


def Run():

    print 'list_1 before we try to update it is:',list_1

    print 'list_1 after we update 5 with 55 is:',UpdateList(list_1, 5, 55)

    print 'list_2 after we delete 10 is:',DeleteElementInList(list_2, 10)

    print 'list_1 and list_2 concatenated togeter is:',ConcatenateLists(list_1, list_2)
    


Run()
            
