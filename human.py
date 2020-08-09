from player import * 
from board import *

class Human(Player):
    def __init__(self):
        self.player = Player(False)

    def __eq__(self,other):
        return self.player == other.player
    

    def makeMove(self, board, col):

        for i in range(len(board.values)):
            (x, _) = board.values[i][col]
            if (not(x)):
                board.values[i][col] = (True, False)
                print(board.values)
            return
        return
 
board = Board()
human = Human()

print(board)
human.makeMove(board, 0)
print(board)


