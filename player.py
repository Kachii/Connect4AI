class Player(object): 
    def __init__(self, player):
        self.values = player
    
    def __eq__(self,other):
        return self.values == other.values 

    def getValidMoves(self, board):
        moves = []
        for i in range(len(board[0])):
            (x, _) = board[0][i]
            if (not x):
                moves.append(i)
        return moves
    
    def makeMove(self, board, col):
        for i in range(len(board[i][col])):
            (x, _) = board[i][col]
            if (x):
                board[i][col] = (True, self.values)
                return
        
        