__author__ = 'aseem jain'

def my_func(x, y, z):
    print(x,y,z)

my_func(1,2,3)
my_typle = (4,5,6)
my_dict={'x': 1,'y':2,'z':3}

# unpacking with * and **
my_func( * my_typle)
my_func( ** my_dict)