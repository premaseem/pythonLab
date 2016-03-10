__author__ = 'asee2278'
import re

patterns = ['sex','boobs']
text = "when you do sex you hace to press boobs"

print re.search("sss",text)

for pattern in patterns :
        mat = re.search(pattern,text)
        if mat :
            print "match found"
            print mat.start()
            print mat.end()

        else : print "match not found"


split_term = '@'
text = "I want do @ the rate of @ boobs "
print re.split(split_term,text)

print re.findall('@',text)

print re.findall('match','test phrase match is in middle match')

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print 'Searching the phrase using the re check: %r' %pattern
        print re.findall(pattern,phrase)
        print '\n'

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)

test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=[ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+'] # one upper case letter followed by lower case letters

multi_re_find(test_patterns,test_phrase)
