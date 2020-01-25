__author__ = 'asee2278'


#1 The function will have an input of a string, and output a list of integers.
def word_lengths(phrase):
    return map(lambda x:len(x) ,phrase.split())

phrase = "How long are the words in this phrase"
print word_lengths(phrase);


#2 Use reduce to take a list of digits and return the number that they correspond to. Do not convert the integers to strings!
def digits_to_num(digits):
    nlist = digits[::-1]
    print nlist

    return reduce(lambda x,y : x*10 +y ,digits)

print digits_to_num([3,4,3,2,1])

#3 Use filter to return the words from a list of words which start with a target letter.
def filter_words(word_list, letter):
    return filter( lambda x: str(x).startswith(letter),word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print filter_words(l,'h')

#4 Use zip and list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them. Look at the example output below:
def concatenate(L1, L2, connector):
    lst= zip(L1,L2,range(3))
    newLst =[]
    for x,y,z in lst:
        newLst.append(x+connector+y)
    return newLst

print concatenate(['A','B','C'],['a','b','c'],'-')

#5 Use enumerate and other skills to return a dictionary which has the values of the list as keys and the index as the value. You may assume that a value will only appear once in the given list.
def d_list(L):
    return { key:value for value,key in enumerate(L) }

print d_list(['a','b','c'])

#6 Use enumerate and other skills from above to return the count of the number of items in the list whose value equals its index.

def count_match_index(lst):
    newLst=[]
    for i,e in enumerate(lst) :
        if i ==e :
            newLst.append(i)
    return len(newLst)


print count_match_index([0,2,2,1,5,5,6,10])