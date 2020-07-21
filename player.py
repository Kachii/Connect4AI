class Player(object): 
    def __init__(self, player):
        self.values = player
    
    def __eq__(self,other):
        return self.values == other.values 
    
    def whatbool(self):
        return self.values