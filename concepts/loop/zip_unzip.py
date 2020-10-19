# Python code to demonstrate the working of unzip

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]

for i in range(len(name)):
    print(name[i],roll_no[i], marks[i])

for l1,l2,l3 in zip(name,roll_no,marks):
    print(l1,l2,l3)

zipedobj= zip(name,roll_no,marks)
con_list = list(zipedobj)
print(con_list)

l1,l2,l3 = zip(*con_list)
print(l1)





#using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print ("The zipped result is : ",end="")
print (mapped)

print("\n")

nl = ['Manjeet', 4, 40], ['Nikhil', 1, 50], ['Shambhavi', 3, 60]
# print(type(nl))
e1,e2,e3  = zip(*nl)
print(e1)
print(e2)
print(e3)

# unzipping values
namz, roll_noz, marksz = zip(*mapped)

print ("The unzipped result: \n",end="")

# printing initial lists
print ("The name list is : ",end="")
print (namz)

print ("The roll_no list is : ",end="")
print (roll_noz)

print ("The marks list is : ",end="")
print (marksz)