# Objective is to add or override value in dict
# @Author Aseem Jain

mydict = {"key1": "value",
"key2": "value",
"key3": "value"
         }
print(mydict)

# add required key over here

mydict['key4'] = "value4"
mydict['key3'] = "updated value"

print(mydict)

# get will not raise the key error
print(mydict.get("key3"))

print(mydict["key3"])

