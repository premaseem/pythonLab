__author__ = 'asee2278'

list = [2,2.2,0," " ]
count = 0
for item in list :
    print "index "+ str(count) +" has element ",
    print item
    count+=1

for index,item in enumerate(list):
    if index >2 : break;
    print( index , item)

lst = [2==2,2==3,4%2==0]
print all(list)

print complex(1,2)
er = complex('2+2j')
print er

