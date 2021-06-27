#绘制龙形曲线，其中dragon()绘制期望的龙形曲线，nogard()绘制反方向
#参考1.2节32题，1.5节9题
#使用的是书中的turtle+题目要求的递归

import turtleBook
import stddraw

def dragon(n):
    if n == 1:
        return 'F'
    else:
        return dragon(n-1) + 'L' + nogard(n-1)

def nogard(n):
    if n == 1:
        return 'F'
    else:
        return dragon(n-1) + 'R' + nogard(n-1)


def dragonDraw(s):
    step = 0.07
    t = turtleBook.Turtle(.5,.5,0)
    for i in range(len(s)):
        if s[i] == 'F':
            t.goForward(step)
        elif s[i] == 'L':
            t.turnLeft(90)
        elif s[i] == 'R':
            t.turnLeft(360-90)

def main():
    n = 6
    #print(dragon(n))
    #print(nogard(n))
    dragonDraw(nogard(n))
    dragonDraw(dragon(n))
    stddraw.show()

if __name__ == '__main__':
    main()
