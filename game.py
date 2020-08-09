from board import Board
from ai import AI
from human import Human


human = Human()
AI = AI()
gameboard = Board()
currPlayer = human
print(gameboard)

while(gameboard.gameOver() == None):
    if (type(currPlayer is Human)):
        print("It is the Human's turn.\n")
    
        #gameboard.printBoard()
        moves = gameboard.getValidMoves()
        print(moves)
        while True:
            try: 
                col = int(input("Please choose a column: "))
                moves.index(col)
                break
            except ValueError:
                print ("Not a valid move, try again.")

        currPlayer.makeMove(gameboard, col)
        print(gameboard)
        #currPlayer = AI
    
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