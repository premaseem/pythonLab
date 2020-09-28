# Objective: Write to file in different modes
# @Author:  Aseem Jain
# @Github: https://github.com/premaseem


# create file if not exists
# read file in append mode and write data to it


import os.path

report_foler = "./report"

if not os.path.exists(report_foler):
    os.makedirs(report_foler)

file_name = report_foler+'/report_test1.txt'
with open(file_name, 'r') as file:

    # would read only 2 character
    print(file.read(2))

    # would read entire line
    print(file.readline())
    print(file.readline())

with open(file_name, 'r') as file:

    # would read only 2 character
    for l in file.readlines():
        print(l.strip("\n"))

with open(file_name, 'r') as file:
    l = file.readline()
    while l != "":
        print()
        l = file.readline()

f = open(file_name,'rt')
print(f)
for x in f:
    print(x)