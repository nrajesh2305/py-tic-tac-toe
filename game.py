
theBoard = [["", "", ""], ["", "", ""], ["", "", ""]]
playerOne = "X"
playerTwo = "O"
currentTurn = playerOne


def printBoard(theBoard):
    print(theBoard[0][0] + "|" + theBoard[0][1] + "|" + theBoard[0][2], end="\t1 2 3\n")
    print("-+-+-")
    print(theBoard[1][0] + "|" + theBoard[1][1] + "|" + theBoard[1][2], end="\t4 5 6\n")
    print("-+-+-")
    print(theBoard[2][0] + "|" + theBoard[2][1] + "|" + theBoard[2][2], end="\t7 8 9\n")
    print()

def checkForTie(theBoard):
    numFilled = 0
    for i in range(3):
        for j in range(3):
            if(len(theBoard[i][j]) > 1):
                numFilled += 1
    return numFilled == 9

def checkForWin(theBoard):
    numWins = 0
    if(theBoard[0][0] == theBoard[0][1] and theBoard[0][1] == theBoard[0][2] and (theBoard[0][0] == "X" or theBoard[0][0] == "O")):
        numWins += 1
    if(theBoard[1][0] == theBoard[1][1] and theBoard[1][1] == theBoard[1][2] and (theBoard[1][0] == "X" or theBoard[1][0] == "O")):
        numWins += 1
    if(theBoard[2][0] == theBoard[2][1] and theBoard[2][1] == theBoard[2][2] and (theBoard[2][0] == "X" or theBoard[2][0] == "O")):
        numWins += 1
    if(theBoard[0][0] == theBoard[1][1] and theBoard[1][1] == theBoard[2][2] and (theBoard[0][0] == "X" or theBoard[0][0] == "O")):
        numWins += 1
    if(theBoard[0][2] == theBoard[1][1] and theBoard[1][1] == theBoard[2][0] and (theBoard[0][2] == "X" or theBoard[0][2] == "O")):
        numWins += 1
    return numWins > 0

def isFilled(theBoard, currentPlayer, choice):
    match choice:
        case 1:
            return len(theBoard[0][0]) != 1
        case 2:
            return len(theBoard[0][1]) != 1
        case 3:
            return len(theBoard[0][2]) != 1
        case 4:
            return len(theBoard[1][0]) != 1
        case 5:
            return len(theBoard[1][1]) != 1
        case 6:
            return len(theBoard[1][2]) != 1
        case 7:
            return len(theBoard[2][0]) != 1
        case 8:
            return len(theBoard[2][1]) != 1
        case 9:
            return len(theBoard[2][2]) != 1

def fillSpot(theBoard, currentPlayer, choice):
    if(not isFilled(theBoard, currentPlayer, choice)):
        match choice:
            case 1:
                theBoard[0][0] = currentPlayer
            case 2:
                theBoard[0][1] = currentPlayer
            case 3:
                theBoard[0][2] = currentPlayer
            case 4:
                theBoard[1][0] = currentPlayer
            case 5:
                theBoard[1][1] = currentPlayer
            case 6:
                theBoard[1][2] = currentPlayer
            case 7:
                theBoard[2][0] = currentPlayer
            case 8:
                theBoard[2][1] = currentPlayer
            case 9:
                theBoard[2][2] = currentPlayer
    return theBoard

def swapPlayer(currentPlayer):
    if currentPlayer == playerOne:
        currentPlayer = playerTwo
    else:
        currentPlayer = playerOne
    return currentPlayer