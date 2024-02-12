from game import *

win_is_not_detected = False
tie_detected = False
currentPlayer = "X"
winner = ""
theBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

print("\nWelcome to Tic-Tac-Toe!\n")
printBoard(theBoard)

while(not win_is_not_detected or not tie_detected):
    move = int(input("What is " + currentPlayer + "'s move? (1-9)\n> "))
    if(move < 1 or move > 9):
        print("Invalid position. Please input a valid position.")
        continue
    if(isFilled(theBoard, currentPlayer, move)):
        print("That spot is already taken. Please input a different spot.")
        continue
    else:
        tie_detected = checkForTie(theBoard)
        theBoard = fillSpot(theBoard, currentPlayer, move)
        printBoard(theBoard)
        win_is_not_detected = checkForWin(theBoard)
        if(tie_detected):
            winner = ""
            break
        if(win_is_not_detected):
            winner = currentPlayer
            break
        else:
            currentPlayer = swapPlayer(currentPlayer)

if(len(winner) > 0):
    print(winner + " has won the game!")
else:
    print("The game is a tie!")

print("Thanks for playing!")