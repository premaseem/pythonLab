__author__ = 'asee2278'



tick = [ [None,None,None],[None,None,None],[None,None,None]]
turn =0
player = 2

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







def takeInput():
    global player
    if  player ==1 : player = 2
    else : player = 2

    if player == 1 : s = 'X'
    else : s = 'Y'
    print "player {} with sign {} take your turn and select coordinate".format(player,s)
    r = int(raw_input("Enter Row ... "))
    c = int(raw_input("Enter Column ... "))

    return inputBoard(s,r,c)




while not validateBoard() :
    takeInput()
    printBoard()

print "Congratulation player",player



