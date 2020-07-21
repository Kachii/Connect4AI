class Board(object): 
    def __init__(self):
        self.values = [[(False,False)]*7]*6
    
    def __eq__(self,other):
        return self.values == other.values 