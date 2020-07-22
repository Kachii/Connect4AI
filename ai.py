from player import * 

class AI(Player):
    def __init__(self):
        self.player = Player(True)

    def __eq__(self,other):
        return self.player == other.player

    def makeMove(self, board, col):
        return 0

    def minimax(self, board):
        return 0
    
    def alphabeta(self, board):
        return 0
