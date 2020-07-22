class Board(object): 
    def __init__(self, player1, player2):
        self.values = [[(False,False)]*7]*6
        self.player1 = player1
        self.player2 = player2 
    
    def __eq__(self,other):
        return self.values == other.values 

    """
    these methods are to going to be used to check if the game is over
    """
    @staticmethod:
    def boardFull(bd):
        for L in bd:
            for (x,y) in L:
                if (not x) return False
        return True
    
    @staticmethod 
    def gameWinner(bd):
        for xstart in range(len(bd)):
            for ystart in range(len(bd[0])):
                (piece,player) = bd[xstart][ystart]
                if(gameWinnerHelper(xstart,ystart,piece,player)!= None) return (True,player)
        return None

    @staticmethod
    def gameWinnerHelper(xstart,ystart,piece,player):
        for xdir in [-1,0,1]:
            for ydir in [-1,0,1]:
                if(gameWinnerHelperDirection(xstart,ystart,piece,player,xdir,ydir) != None) return (True,player)
        return None 
    @staticmethod 
    def gameWinnerHelperDirection(xstart,ystart,piece,player,xdir,ydir):
        for i in range(4):
            X = xstart + i*xdir
            Y = ystart + i*ydir 
            (currPiece,currPlayer) = self.values[X][Y]
            (if X < 0 or  X > 7 or  Y < 0 or  Y > 6): #checking if pieces within bounds of board
                return None
            (currPiece,currPlayer) = self.values[X][Y]
            if((currPiece != piece) or )
    def gameOver(self):
        #return gameWinner(self.values)
         



