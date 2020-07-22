from board import *
from ai import *
from human import *


human = Human()
AI = AI()
gameboard = Board()

currPlayer = human
while(gameboard.gameOver() == None):
    if (type(currPlayer is Human)):
        print("It is the Human's turn.\n")
    
        #gameboard.printBoard()
        currPlayer.getValidMoves()
    
        col = input("Please choose a column: ")

        currPlayer = AI
    
    else :
        #gameboard.printBoard()
        currPlayer.makeMove
        currPlayer = human

#gameboard.printBoard()
(x, y) = gameboard.gameOver()
if (x & y):
    print("AI wins!")
elif (x):
    print("Human wins!")
else: 
    print("Draw!")    

print("Works!")