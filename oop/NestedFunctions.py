__author__ = 'asee2278'


def mother():
    mvar = "mvar"
    print "Mother funciton started "
    print locals()
    def nidhi():
        nvar = "nvar"
        print "inside nidhi function"
        print locals()
        def pihu(): print "pagal"
        return pihu()
    def gudda():
        gvar = "gvar"
        print "inside gudda function"

    def __str__():
        print "abc"
    return nidhi();



# print globals()
x = mother
print x()

########## Function within function

def jobFunction():
    return "I finished job"

def printFunction(func):
    print func() + " tradeMark"

printFunction(jobFunction)