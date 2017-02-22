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
        #print line THIS IS WHERE I STOPPED. NOW KNOW HOW TO HAVE THIS IF STATEMENT HANDLE 'ATOM'. PROCEED
        if 'ATOM' in line:
            print i
            print 'hahah'
            break
        else:
            #print line
            tmp = tmp + str('{:0>4d}'.format(i)) + ': ' + line
    all_file_contents = tmp
    file_name.close()
    return all_file_contents

def BuildHeadList(all_file_contents):
    for i, line in enumerate(all_file_contents):
        print line + str(i)
    
    
    
    
AskForFileName()
