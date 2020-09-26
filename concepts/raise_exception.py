import sys


class Myexception(Exception):
    pass

if len(sys.argv) != 2:
    raise Myexception("Argument not passed ")

