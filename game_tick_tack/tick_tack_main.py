__author__ = 'asee2278'



tick = [ [None,None,None],[None,None,None],[None,None,None]]
player = 1

def printBoard() :
    print "$$$ Current status $$$$$$$$$$$$$$ "
    for row in tick :
        print row
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ "

def inputBoard(sign,row,column) :
    if row > 2 or column > 2 :
        print " invalid input try again "
        return False
    if tick[row][column] <> None :
        print " Cell is already occupied"
        return False
    tick[row][column] = sign
    return True

def validateRow():
    for row in tick :
        if row[0] <> None :
            if row[0] == row[1] and row[0] == row[2] :
                print "Game Over Row victory" , row
                return True
    return False


def validateDiagonal() :
    if tick[0][0] <> None :
        if tick[0][0] == tick[1][1] and tick[0][0] == tick[2][2] :
                print "Game Over Diagonal Victory"
                return True
    if tick[0][2] <> None :
        if tick[0][2] == tick[1][1] and tick[0][2] == tick[2][0] :
                print "Game Over Diagonal Victory"
                return True
    return False

def validateColumn(num) :
    if tick[0][num] <> None :
            if tick[0][num] == tick[1][num] and tick[0][num] == tick[2][num] :
                print "Game Over Column victory"
                return True
    return False

def validateBoard():
    if validateRow() or validateDiagonal() or validateColumn(0) or validateColumn(1) or validateColumn(2):
        print "Thanks for playing "
        return True

    return False

print "welcome to Tic Tack game ... "







def takeInput(ply):

    if ply == 1 : s = 'X'
    else : s = '0'
    print "player {} with sign {} take your turn and select coordinate".format(ply,s)
    r = int(raw_input("Enter Row ... "))
    c = int(raw_input("Enter Column ... "))

    return inputBoard(s,r,c)



counter = 1
while not validateBoard() :

    if counter % 2 == 0 :
        ply = 2
    else :
        ply = 1

    if takeInput(ply) :
        counter = counter + 1
    printBoard()

print "Congratulation player",player



