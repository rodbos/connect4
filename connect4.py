"""
This is a python script that creates a command line vesrsion of the connect 4 game.  The script
draws a board and allows two players to take turns placings pieces on the board.  The first player
to get 4 across or diagonal wins.
"""
import numpy as np
RowCount = 6
ColumnCount = 7

#draw the board using the numpy zeros function
def drawBoard():
    board = np.zeros((RowCount,ColumnCount))
    return board

#Add the pieces to the board
def addPiece(board, row, column, piece):
    board[row][column] = piece

#Verifying that the location is valid
def validLocation(board, column):
    return board[RowCount - 1][column] == 0

def getNextOpenRow(board, column):
    for r in range(RowCount):
        if board[r][column] == 0:
            return r

#Print the Board so that the first value is at the bottom
def printBoard(board):
    print(np.flip(board, 0))

#Check for winning move in the horizontal, vertical and diaganol
def winningMove(board, piece):
    #check horizontal locations for win
    for c in range(ColumnCount - 3):
        for r in range(RowCount):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #check vertical location for win
    for c in range(ColumnCount):
        for r in range(RowCount - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #check diaganols for win
    for c in range(ColumnCount - 3):
        for r in range(RowCount - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True    

    for c in range(ColumnCount - 3):
        for r in range(3, RowCount):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True    

board = drawBoard()
printBoard(board)
gameOver = False
Player = 0

while not gameOver:
    #Ask for Player 1 Input
    if Player == 0:
        print("",np.array([0.,1.,2.,3.,4.,5.,6.]))
        while True:
            try:
                column = int(input("Player 1 Maker your Selection (0-6):"))
            except ValueError:
                print("Sorry, I didn't understand that please make another selection.")
                continue
            else:
                if column >= 0 and column <= 6:
                    break
                else:
                    print("Sorry,",column,"is out the range of 0-6 please make another selection")
                    continue

        if validLocation(board, column):
                row = getNextOpenRow(board, column)
                addPiece(board, row, column, 1)

                if winningMove(board, 1):
                    print("Player 1 WINS!!!")
                    gameOver = True

    #Ask for Player 2 Input
    else:
        print("",np.array([0.,1.,2.,3.,4.,5.,6.]))
        while True:
            try:
                column = int(input("Player 2 Maker your Selection (0-6):"))
            except ValueError:
                print("Sorry, I didn't understand that please make another selection.")
                continue
            else:
                if column >= 0 and column <= 6:
                    break
                else:
                    print("Sorry,",column,"is out the range of 0-6 please make another selection")
                    continue

        if validLocation(board, column):
            row = getNextOpenRow(board, column)
            addPiece(board, row, column, 2)

            if winningMove(board, 2):
                print("Player 2 WINS!!!")
                gameOver = True

    printBoard(board)

    Player += 1
    Player = Player%2
