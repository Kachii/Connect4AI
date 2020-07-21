from board import *
from player import *

gameboard = Board()
human = Player(False)
AI = Player(True)


while(gameboard.gameWinner() == None):
    print("TODO")
    
    
(x, y) = gameboard.gameWinner()
if (x & y):
    print("AI wins")
elif (x):
    print("Human wins")
else: 
    print("Draw")    

print("Works!")
print(human.whichPlayer())
print(AI.whichPlayer())
