"""
Understand Argument Parsing in python by coding calculator application
input argument will be 2 number
input arugment will be ADD / SUB / MUL


"""

__author__ = "Aseem Jain"
__profile__ = "https://www.linkedin.com/in/premaseem/"

import argparse
import sys


def calc(args):
    if args.opt == 'add':
        return args.x + args.y
    elif args.opt == 'mul':
        return args.x * args.y
    elif args.operation == 'sub':
        return args.x - args.y

    elif args.operation == 'div':
        return args.x / args.y

import functools
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, required=True,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add', dest = "opt",
                        help='What operation? Can choose add, sub, mul, or div')
    args = parser.parse_args()
    print(args)
    sys.stdout.write(str(calc(args)))
    # s = functools.reduce(sum,[1,2,3,4,5])
    s = list(functools.reduce(sum,list(range(10))))
    print(s)