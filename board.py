class Board(object): 
    def __init__(self):
        self.values = [[(False,False)]*7]*6
    
    def __eq__(self,other):
        return self.values == other.values 

    """
    these methods are to going to be used to check if the game is over
    """
    @staticmethod:
    def boardFull(bd):
        for (x,y) in bd:
            if (not x) return False
        return True
    
    @staticmethod 
    def gameWinner(bd):
        for i in range(len(bd)):
            for j in range(len(bd[0])):
                (piece,player) = bd[i][j]
                if(gameWinnerHelper(i,j,piece,player)) return (True,player)
        return None

    @staticmethod
    def gameWinnerHelper(xstart,ystart,piece,player):
        return None
    @staticmethod 
    def gameWinnerHelperDirection(xstart,ystart,piece,player,xdir,ydir):
        return None 

    def gameOver(self):
        if(boardFull(self.values)):
            return None 
        else:
            return gameWinner(self.values)



