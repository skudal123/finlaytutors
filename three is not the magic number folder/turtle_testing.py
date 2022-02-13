#turtle_testing.py

import turtle
from math import *
from time import sleep

def GetInput():
    OverallSize = turtle.numinput("Size", "Please enter a size", 350, 100, 1000)
    Speed = turtle.numinput("Speed", "What speed would you like me to draw at? 1 is the slowest and 10 the fastest",
                            6, 0, 10)
    Main(OverallSize, Speed)

def DrawRightTriangle(Opp,Adj,Hyp,startX,startY):
    turtle.setx(startX)
    turtle.sety(startY)
    turtle.left(180)
    turtle.forward(Adj)
    turtle.right(90)
    turtle.forward(Opp)
    turtle.goto(startX,startY)
    turtle.exitonclick() 
    sleep(2000)
    
    
def DrawEqualateral(Size):
    turtle.forward(Size)
    turtle.left(120)
    turtle.forward(Size)
    turtle.left(120)
    turtle.forward(Size)
    
def Main(OverallSize, Speed):
    turtle.speed(Speed)
#    turtle.penup()
#    CenterDrawing(Size)  # move to the start location without drawing anything
    turtle.pendown()
    DrawTriangle(OverallSize)  # start the recursion program
    turtle.exitonclick()  # enable exit on click of mouse
    

DrawRightTriangle(300,400,500,0,0)
