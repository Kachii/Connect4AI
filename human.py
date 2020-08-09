from player import * 

class Human(Player):
    def __init__(self):
        self.player = Player(False)

    def __eq__(self,other):
        return self.player == other.player
    

    def makeMove(self, board, col):

        for i in range(len(board[i][col])):
            (x, _) = board[i][col]
            if (not(x)):
                board[i][col] = (True, False)
 