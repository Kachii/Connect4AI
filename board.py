class Board(object): 
    def __init__(self):
        self.values = [[(False,False)]*7]*6
    
    def __eq__(self,other):
        return self.values == other.values 

    def boardFull(self):
        for (x,y) in self.values:
            if (not x) return False
        return True
    
    def gameWinner(self):
        for i in range(len(self.values)):
            for j in range(len(self.values[0])):
                (piece,player) = self.values[i][j]
                if(gameWinnerHelper(i,j,piece,player)) return (True,player)
        return None
    @staticmethod
    def gameWinnerHelper(xstart,ystart,piece,player):
        


