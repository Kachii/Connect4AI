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
        moves = currPlayer.getValidMoves()
        
        while True:
            try: 
                col = input("Please choose a column: ")
                moves.index(col)
                break
            except ValueError:
                print ("Not a valid move, try again.")

        currPlayer.makeMove(gameboard, col)
        currPlayer = AI
    
    else :
        #gameboard.printBoard()
        #currPlayer.makeMove
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