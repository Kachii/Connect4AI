from player import *

class Human(object):
    def __init__(self):
        self.player = Player(False)

    def __eq__(self,other):
        return self.player == other.player
    


    