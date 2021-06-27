#画Gosper Island
#使用的书中的turtle
#n = 1:六边形 2：六个边每个边变为3条 3：六个边每个边变为9条，也就是18条边，每个变为3条；即*3的节奏

import turtle
import stddraw
import sys

def gosper(n):
    if n == 0:
        return 'F'
    else:
        return 'B' + gosper(n-1) + 'L' +gosper(n-1) + 'R' + gosper(n-1) + 'A'

def treblih(n):
    if n == 1:
        return 'RFLFLFR'
    else:
        return 'R' + hilbert(n-1) + 'F' + 'L' + treblih(n-1) + 'F' + treblih(n-1) + 'L' + 'F' + hilbert(n-1) + 'R'



def draw(s,n):
    step = .07/n
    ANGLE = 19.106605350869094394
    t = turtle.Turtle(.5,.5,0)
    for i in range(len(s)):
        if s[i] == 'F':
            t.goForward(step)
        elif s[i] == 'L':
            t.turnLeft(60)
        elif s[i] == 'R':
            t.turnLeft(360-60)
        elif s[i] == 'A':
            t.turnLeft(ANGLE)
        elif s[i] == 'B':
            t.turnLeft(-ANGLE)
    

def main():
    n = eval(sys.argv[1])
    #n = 1
    #print(dragon(n))
    #print(nogard(n))
    g = gosper(n)
    print(g)
    draw(g,n)
    #dragonDraw(dragon(n))
    stddraw.show()

if __name__ == '__main__':
    main()

    
