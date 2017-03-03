'''
lab_7_exercises_num_4_answer.py
'''
for i in range(99, 0, -1):
        if i == 1:
                print '1 bottle of beer on the wall, 1 bottle of beer!' 
                print 'So take it down, pass it around, no more bottles of beer on the wall!' 
        elif i == 2:
                print '2 more bottles of beer on the wall, 2 more bottles of beer!' 
                print 'So take one down, pass it around, 1 more bottle of beer on the wall!' 
        else:
                print i,' bottles of beer on the wall,',i,'bottles of beer!' 
                print 'So take it down, pass it around,',i - 1,'more bottles of beer on the wall!'
