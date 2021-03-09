"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

Using the Python defaultdict Type for Handling Missing Keys and doing

1. Grouping Items
2. Grouping Unique Items
3. Counting Items
4. Accumulating Values or Aggregation

"""
from collections import defaultdict

def group_by(l):
    m = defaultdict(list)
    for d,e in l:
        m[d].append(e)
    print(m)

def group_by_unique(l):
    m = defaultdict(set)
    for d,e in l:
        m[d].add(e)
    print(m)

def count(l):
    """counts the number of employees per department"""
    m = defaultdict(int)
    for d,_ in l:
        m[d] += 1
    print(m)

def accumulate(l):
    m = defaultdict(float)
    for prod,price in l:
        m[prod] += price
    print(m)


dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]

group_by(dep)
group_by_unique(dep)
count(dep)

incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]
accumulate(incomes)

