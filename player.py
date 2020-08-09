class Player(object): 
    def __init__(self, player):
        self.values = player
    
    def __eq__(self,other):
        return self.values == other.values 
    
    '''We don't need this method anymore'''
    def getValidMoves(self, board):
        return board.getValidMoves()
    
    def makeMove(self, board, col):
        return 