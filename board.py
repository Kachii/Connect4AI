class Board(object): 
    def __init__(self):
        self.values = [[(False,False)]*7]*6
    
    def __eq__(self,other):
        return self.values == other.values 

    def __repr__(self):
        st = ""
        for L in self.values:
            for (x,y) in L:
                if x:
                    if(y): st += "X "
                    else: st += "O "
                else: st+= "- "
            st += "\n"
        return st

    
    @staticmethod 
    def gameWinner(bd):
        for xstart in range(len(bd)):
            for ystart in range(len(bd[0])):
                (piece,player) = bd[xstart][ystart]
                if not(piece): continue
                if(Board.gameWinnerHelper(xstart,ystart,piece,player)!= None): return (True,player)
        if Board.boardFull(bd): return (False,False)
        else: return None 

    @staticmethod
    def gameWinnerHelper(xstart,ystart,piece,player):
        for xdir in [-1,0,1]:
            for ydir in [-1,0,1]:
                if(Board.gameWinnerHelperDirection(xstart,ystart,piece,player,xdir,ydir) != None): return (True,player)
        return None 

    @staticmethod 
    def gameWinnerHelperDirection(xstart,ystart,piece,player,xdir,ydir):
        for i in range(4):
            X = xstart + i*xdir
            Y = ystart + i*ydir 
            if (X < 0 or  X > 7 or  Y < 0 or  Y > 6): #checking if pieces within bounds of board
                return None
            (currPiece,currPlayer) = self.values[X][Y]
            if(currPiece or player != currPlayer): return None 
        return (True, player)

    @staticmethod
    def boardFull(bd):
        L = bd[0]
        for (piece, _) in L:
                if (not piece): return False
        return True

    def gameOver(self):
        return Board.gameWinner(self.values)

    def getValidMoves(self): 
        moves = []
        for i in range(len(self.values[0])):
            (piece, _) = self.values[0][i]
            if (not(piece)): moves.append(i)
        return moves



