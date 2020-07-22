from board import *
from ai import *
from human import *

gameboard = Board()
human = Human()
AI = AI()

currPlayer = human
while(gameboard.gameWinner() == None):
    if (type(currPlayer is Human)):
        print("It is the Human's turn.\n")
    
        gameboard.printBoard()
        currPlayer.getValidMoves()
    
        col = input("Please choose a column: ")

        currPlayer = AI
    
    else :
        currPlayer.makeMove
        currPlayer = human

(x, y) = gameboard.gameWinner()
if (x & y):
    print("AI wins")
elif (x):
    print("Human wins")
else: 
    print("Draw")    

print("Works!")