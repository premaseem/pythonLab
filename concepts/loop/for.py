# Else would be executed after the for loop and would be skipped with break

#!/usr/bin/python3

numbers = [11,33,55,39,55,75,37,21,23,41,13,2]

for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list doesnot contain even number')

#############################################
lst = range(2,15,2)
# for a in lst:
#     print(a)

#############################################
# print reverse of string
str = "aseem jain is a good man"
newstr = ""
for i in range(len(str)):
    #print(str[i])
    newstr = newstr + str[i]
print(newstr)

#############################################
# iterating with index

for index in range(len(str)):
    print(str[index])


#############################################

# iterating with index using enumerator
colors = ["red", "green", "blue", "purple"]
for index, color in enumerate(colors):
    print(f"{index} has {color}")


#############################################
# loop over multiple iterables

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
sizes = ["xs", "s","m","l"]
for color, ratio, size in zip(colors, ratios, sizes):
    print(color,ratio, size)