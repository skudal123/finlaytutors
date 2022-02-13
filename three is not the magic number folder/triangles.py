import turtle
import math


# Draw an equilateral triangle with sides = SideLength
def DrawTriangle(SideLength):
    for i in range(3):
        turtle.forward(SideLength)
        turtle.left(120)


# find the center of the drawing and move to the first corner
def CenterDrawing(SideLength):
    centerX = 0 - (SideLength / 2)  # X will always be half way along a side
    centerY = 0 - (((math.sqrt(3) / 2) * SideLength) / 2)  # Y is calculated using pythagoras
    turtle.setpos(centerX, centerY)


def Sierpinski(SideLength, LevelOfRecursion):
    if LevelOfRecursion == 0:
        DrawTriangle(SideLength)  # if no more levels to do just draw the triangle
    else:
        for i in range(3):
            Sierpinski(SideLength / 2, LevelOfRecursion - 1)  # make the sidelength smaller and the level of
            # recursion smaller to draw inner triangles
            turtle.forward(SideLength)  # reposition between inner triangles
            turtle.left(120)


def Main(Size, Levels, TurtleSpeed):
    turtle.speed(TurtleSpeed)  # set speed of the turtle
    turtle.penup()
    CenterDrawing(Size)  # move to the start location without drawing anything
    turtle.pendown()
    Sierpinski(Size, Levels)  # start the recursion program
    turtle.exitonclick()  # enable exit on click of mouse


def GetInput():
    # get size, number of times to recur and what speed the turtle should move at
    OverallSize = turtle.numinput("Size", "Please enter a size", 350, 100, 1000)
    NumberOfLevels = turtle.numinput("Levels of Recursion", "how many levels would you like us to render?", 3, 0, 6)
    Speed = turtle.numinput("Speed", "What speed would you like me to draw at? 1 is the slowest and 10 the fastest", 6,
                            0, 10)
    # call the main program with the wanted variable
    Main(OverallSize, NumberOfLevels, Speed)


# run the input grabbing code and start drawing triangles, comment out for testing
GetInput()
# This is for debug of main code, it will skip user input
# Main(300,3,6)
