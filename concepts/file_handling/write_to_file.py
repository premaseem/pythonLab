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
f = open(file_name, 'a+')
f.write('\n python rules')
f.close()