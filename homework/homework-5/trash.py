##f = open('example.txt','r+')
##pop = ''
##counter = 0
##for i, line in enumerate(f):
##    if line == '4\n':
##        print ' '
##        break
##    else:
##        print line
##        pop =       pop + str(i) +': ' + line
##        pop_file =  open('pop.txt','a+')
##        pop_file.write(str(pop))
##        pop_file.close()
##        
##print pop
##f.close()

##a = 'ATOM      1  N   LYS A   1       1.300  19.462  22.166  1.00 10.50           N '
##'ATOM' in a
##if 'ATOM' in a:
##    print 'ATOM in a'
##else:
##    print 'ATOM not in a'

import StringIO

foo = '''hello
world
guy '''
s = StringIO.StringIO(foo)
print foo
print s
for line in s:
    print line
