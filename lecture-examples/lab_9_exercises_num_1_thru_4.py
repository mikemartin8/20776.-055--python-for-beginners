'''
lab_9_exercises_num_1_thru_4.py - Shows how to read and write files (file I/O)
'''

def PrintLinesInFile(filename):

    try:
        file = open(filename)
    except IOError:
        print 'File cannot be found!'
    else:
        for line in file:
            print line
        file.close()

def CreateNewFile(filename):

    file = open(filename, 'w')
    file.close()

def WriteLineToFile(line, filename):

    try:
        file = open(filename, 'a')
    except IOError:
        print 'File cannot be found!'
    else:
        file.write(line)
        file.close()

def OpenFileRead(filename):

    try:
        file = open(filename)

        return file
    except IOError:
        print 'File cannot be found!'
    
def CountLinesInFile(filename):

    file = OpenFileRead(filename)

    counter = 0
    lines = file.readlines()
    for line in lines:
        counter = counter + 1
    file.close()

    return counter

def CreateNewNumberedLinesFile(filename):

    file = OpenFileRead(filename)

    lines_list = []
    lines = file.readlines()
    for i, line in enumerate(lines):
        lines_list.append(str(i + 1) + '.  ' + line)
    
    new_filename = filename.rsplit('.')[0] + '_numbered.' + filename.rsplit('.')[1]

    file.close()

    file = open(new_filename, 'w')
    for line in lines_list:
        file.write(line + '\n')
    file.close()
    
    

def Run():

    CreateNewFile('/Users/donaldk/Desktop/Python_Beginners_Course_Materials/lab_9_exercises.txt')
    WriteLineToFile('First line\n', '/Users/donaldk/Desktop/Python_Beginners_Course_Materials/lab_9_exercises.txt')
    WriteLineToFile('Second line\n', '/Users/donaldk/Desktop/Python_Beginners_Course_Materials/lab_9_exercises.txt')
    WriteLineToFile('Third line\n', '/Users/donaldk/Desktop/Python_Beginners_Course_Materials/lab_9_exercises.txt')
    WriteLineToFile('Fourth line\n', '/Users/donaldk/Desktop/Python_Beginners_Course_Materials/lab_9_exercises.txt')
    PrintLinesInFile('/Users/donaldk/Desktop/Python_Beginners_Course_Materials/lab_9_exercises.txt')
    print CountLinesInFile('/Users/donaldk/Desktop/Python_Beginners_Course_Materials/lab_9_exercises.txt')
    CreateNewNumberedLinesFile('/Users/donaldk/Desktop/Python_Beginners_Course_Materials/lab_9_exercises.txt')
    PrintLinesInFile('/Users/donaldk/Desktop/Python_Beginners_Course_Materials/lab_9_exercises_numbered.txt')
    
Run()
