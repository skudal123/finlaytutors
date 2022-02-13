#Main.py

from math import *
import turtle

def DoNothing():
    return

def Pythagorus(opposite, adjacent, hypotenuse):

    if hypotenuse == 0:
        hypotenuse = sqrt((opposite**2) + (adjacent**2))
        return hypotenuse        
    elif adjacent == 0:
        adjacent = sqrt((hypotenuse**2) - (opposite**2))
        return adjacent
    elif opposite == 0:
        opposite = sqrt((hypotenuse**2) - (adjacent**2))
        return opposite  
    
opposite = int(input("Please input the length of the opposite"))
adjacent = int(input("Please input the length of the adjacent"))
hypotenuse = int(input("Please input the length of the hypotenuse"))    

print(Pythagorus(opposite, adjacent, hypotenuse))
var=input("Bye")
