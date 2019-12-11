# Objective is to find if string has word in it
# @Author Aseem Jain

line= "test-elasticsearch-aseemelastic2"
print(line.rfind("elasticsearch"))

if "elastic" in "test-elasticsearch-aseemelastic2":
    print("found")
else:
    print("not found")

import re

if re.findall("elastic4", "test-elasticsearch-aseemelastic2", re.IGNORECASE):
    print("found")
else:
    print("not found")