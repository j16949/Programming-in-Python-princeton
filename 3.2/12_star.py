import stddraw
import sys
import math
from turtle import Turtle

def main():
    n = int(sys.argv[1])
    #n = 5
    turtle = Turtle(.5, .0, 90-(180.0/n/2))
    stepSize = math.sin(math.radians(180.0/n))*n/3
    stddraw.clear(stddraw.LIGHT_GRAY)
    for i in range(n):
        turtle.goForward(stepSize)
        turtle.turnLeft((1-1/n)*180.0)
        stddraw.show(1000)
    stddraw.show()

if __name__ == '__main__':
    main()

