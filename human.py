from player import * 
from board import *

class Human(Player):
    def __init__(self):
        self.player = Player(False)

    def __eq__(self,other):
        return self.player == other.player

    def makeMove(self, board, col):
        for i in range(len(board.values)-1,-1,-1):
            (x, _) = board.values[i][col]
            if (not(x)):
                board.values[i][col] = (True, False)
                break


board = Board()
hum = Human() 

hum.makeMove(board,2)
hum.makeMove(board,3)
print(board.gameOver())
hum.makeMove(board,3)
hum.makeMove(board,3)
hum.makeMove(board,3)
print(board.gameOver())
hum.makeMove(board,5)

