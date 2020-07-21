<<<<<<< HEAD
class Board(object): 
    def __init__(self):
        self.values = [[(False,False)]*7]*6
    
    def __eq__(self,other):
        return self.values == other.values 
=======

rows, cols = (6, 7)
board = [[(False,False)] * cols]*rows 
print(board)
>>>>>>> 3e636dba297cf8d2dc3834a9d176dd2c6cfeb074
