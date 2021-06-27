#画希尔伯特曲线，通过一对方法
#使用的书中的turtle
#边长为2^n-1
#wikipedia:
# Alphabet : A, B
# Constants : F + −
# Axiom : A
# Production rules:
# A → +BF−AFA−FB+
# B → −AF+BFB+FA−
# Here, "F" means "draw forward", "+" means "turn left 90°", "-" means "turn right 90°" (see turtle graphics), and "A" and "B" are ignored during drawing.

import turtle
import stddraw
import sys

def hilbert(n):
    if n == 1:
        return 'LFRFRFL'
    else:
        return 'L' + treblih(n-1) + 'F' + 'R' + hilbert(n-1) + 'F' + hilbert(n-1) + 'R' + 'F' + treblih(n-1) + 'L'

def treblih(n):
    if n == 1:
        return 'RFLFLFR'
    else:
        return 'R' + hilbert(n-1) + 'F' + 'L' + treblih(n-1) + 'F' + treblih(n-1) + 'L' + 'F' + hilbert(n-1) + 'R'



def draw(s,n):
    step = 1/(2**n-1)-0.001
    t = turtle.Turtle(.001,.001,0)
    for i in range(len(s)):
        if s[i] == 'F':
            t.goForward(step)
        elif s[i] == 'L':
            t.turnLeft(90)
        elif s[i] == 'R':
            t.turnLeft(360-90)
    

def main():
    n = eval(sys.argv[1])
    #n = 1
    #print(dragon(n))
    #print(nogard(n))
    draw(hilbert(n),n)
    #dragonDraw(dragon(n))
    stddraw.show()

if __name__ == '__main__':
    main()

    
