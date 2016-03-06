__author__ = 'asee2278'
try:
    f = open('testfile','r')
    f.write('Test write this')
except:
    # This will check for any exception and then excute this print statement
   print "Error: Could not find file or read data"
else:
   print "Content written succesfully"
   f.close()
finally:
    print "The attempt was worth"


def askint():
    while True:
        try:
            val = int(raw_input("Please enter an integer: "))
        except:
            print "Looks like you did not enter an integer!"
            continue
        else:
            print 'Yep thats an integer!'
            break
        finally:
            pass
            # print "Finally, I executed!"
        print val
#askint()

x = 5
y = 0

try :
    z = x/y
except : print "divide by zero "
finally:print "calculation finished "


def ask():
    while True:
        try:
            val = int(raw_input("Enter an Integer"))
        except :
            print "An error occured! Please try again!"
            continue
        else :
            print "Thank you, you number squared is: "+ str( val ** 2 )
            break
ask()
