import copy
list1 = [10, 20, 30, ['A' , 'B' , 'C']]
list_ref = list1
list2 = list1.copy()
list3 = copy.deepcopy(list1)
list1[3][1] = "replaced"
list1[1] = "replaced"

# original updated list
print(list1)

# reference
print(list_ref)

# shallow copy
print(list2)

# deep copy
print(list3)