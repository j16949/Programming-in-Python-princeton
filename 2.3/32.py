#import stddraw   #stddraw 是根据坐标画图，而此题更符合按照角度画图，用turtle

import turtle
import sys

def reTree(n,t,l):
	if n == -1 : return
	t.forward(l)
	turtle.delay(0)
	m = t.clone()
	m.left(70)
	reTree(n-1,m,3/5*l)
	m1 = t.clone()
	m1.left(20)
	reTree(n-1,m1,1/5*l)
	t.right(30)
	reTree(n-1,t,3/5*l)

n = eval(sys.argv[1])
t = turtle.Turtle()
t.seth(90)
t.hideturtle()
reTree(n,t,100)	
turtle.done()	#保持画布
