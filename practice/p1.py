# Iterating multiple lists or enumerable objects together, runs to shorted of 2
lst = [1,2,3,4,6,8,10,None,None,None]

print(len(list(filter(lambda x: not x, lst))))