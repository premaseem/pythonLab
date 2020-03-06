__author__ = 'asee2278'

import json
dict = {"a":1,'c':2,"b":34,"city":"san Antonio"}

print(dict)

# Can use expandable tabs
for k, v in dict.items():
    print("{}:  \t  {} ".format(k, v).expandtabs(50))

# can convert it in json with indentation
print(json.dumps(dict, indent=2, sort_keys=True))



""" Sample Output """
# /Users/asee2278/virtualEnv/bpiNew/bpi/bin/python /Users/asee2278/gitRepo/playground/pythonPlayground/tricks/pretty_print_dict_json.py
# {'a': 1, 'city': 'san Antonio', 'c': 2, 'b': 34}
# {
#     "a": 1,
#     "b": 34,
#     "c": 2,
#     "city": "san Antonio"
# }

# With expand tabs
# a:                                                  1
# c:                                                  2
# b:                                                  34
# city:                                               san Antonio