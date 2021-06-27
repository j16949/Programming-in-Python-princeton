#官网JAVA翻译版
import stddraw
from turtle import Turtle
import sys
import math

ANGLE = 19.106605350869094394
size = 0.07

def gosperIsland(n,turtle):
    global size
    size = (7.0 / 16.0) / (math.sqrt(7.0)**n)
    gosper(n)
    turtle.turnLeft(60)
    gosper(n)
    turtle.turnLeft(60)
    gosper(n)
    turtle.turnLeft(60)
    gosper(n)
    turtle.turnLeft(60)
    gosper(n)
    turtle.turnLeft(60)
    gosper(n)
    turtle.turnLeft(60)


def gosper(n):
    #global size
    if n == 0:
        turtle.goForward(size)
    else:
        turtle.turnLeft(-ANGLE)
        gosper(n-1)
        turtle.turnLeft(60)
        gosper(n-1)
        turtle.turnLeft(-60)
        gosper(n-1)
        turtle.turnLeft(ANGLE)
        
n = 3
turtle = Turtle(9.0/32.0, 1.0/8.0, 0.0)
gosperIsland(n,turtle)
stddraw.show()
