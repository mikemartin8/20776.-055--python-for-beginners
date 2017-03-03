# Michael Martin
# 2/19/2016
# Homework 5

def AskForFileName():
    filename = '1JKB.pdb'#raw_input('Enter the name of the input file:\n')
    while filename != '1JKB.pdb':
        if filename != '1JKB.pdb':
            print 'you entered the wrong filename.'
            filename = raw_input('Enter the name of the input file:\n') 
        else:
            continue
    data = open(filename,'r')
    all_file_contents = ReadFileContents(data)
    #print all_file_contents
 #   BuildHeadList(all_file_contents)
    
        
def ReadFileContents(file_name):
    tmp = ''
    for i, line in enumerate(file_name):
        tmp = tmp + str('{:0>4d}'.format(i)) + ': ' + line
    file_name.close()
    all_file_contents = tmp
    return all_file_contents

def BuildHeadList(all_file_contents):
    tmp = ''
    for i, line in enumerate(file_name):
        if 'ATOM   ' in line:
            break
        else:
            tmp = tmp + str('{:0>4d}'.format(i)) + ': ' + line
    
    
    
    
AskForFileName()
