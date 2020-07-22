from board import *
from ai, human import *

gameboard = Board()
human = Human()
AI = AI()

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
