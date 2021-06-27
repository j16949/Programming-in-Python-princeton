#绘制龙形曲线，其中dragon()绘制期望的龙形曲线，nogard()绘制反方向
#参考1.2节32题，1.5节9题
#使用的是python自带的turtle，而且函数用的之前写的，和题目不太一致

import turtle

def re_s(s):
    rs=s
    if len(s)>1:
        m=s[len(s)//2]
        if m=='L':
            rs=s[:len(s)//2]+'R'+s[len(s)//2+1:]
        elif m=='R':
            rs=s[:len(s)//2]+'L'+s[len(s)//2+1:]
    return rs

def dragonString(n):
    s = 'F'
    for i in range(n):
        D = s+'L'+re_s(s)
        s = D
    return D

def dragon(n):
    step = 10
    turtle.speed(0)
    s = dragonString(n)
    for i in range(len(s)):
        if s[i] == 'F':
            turtle.fd(step)
        elif s[i] == 'L':
            turtle.left(90)
        elif s[i] == 'R':
            turtle.right(90)
    turtle.done()

def main():
    dragon(5)


if __name__ == '__main__':
    main()
