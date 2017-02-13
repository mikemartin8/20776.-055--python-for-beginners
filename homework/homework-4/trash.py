##for i in range(3,0,-1):
##    print i,
##print 'CONTACT'
##
##for char in 'Python yo!':
##    print char
##
##list_1 = ['GO','PACK','GO']
##for chant in list_1:
##    print chant
##    
##for i in range(99,0,-1):
##    print i,'bottles of beer on the wall,',i,' bottles of beer!'
##    print 'So take it down, pass it around,',i-1,' more bottles of beer on the wall!'

##list_1 = ['Yo Yo Ma', 1234, 2011, ['Yo Yo Pa']]
##for item in enumerate(list_1):
##    print item

city_list = ['sf','sf','sf','SSF','sf']

length = len(city_list)
for i in range(0,length,1):
    for j in range(i,length,1):
        if (city_list[i] == city_list[j]) & (i != j):
            print i,j, 'duplicate'#'i=',i,'j=',j,city_list[i],'is a duplicate'
        elif i == j:
            print i, j,'same indices'
        else:
            print i,j, 'not duplicate'


                
##print a
####print a[-1]
####print a[0]
####print a[1]
####print a[2]
####print a[3]
####print a[4]
##
##for j in range(0,len(a),1):
##    if a[int(j)] == 'sf':
##        print j,a[int(j)],'pass'
##    else:

    
##        print j,a[int(j)],'fail'
##
##b = 'sf'
##if b in a:
##    print 'haha'
##
##print ''
##
##d = any(a.count(x) > 1 for x in a)
##print 
