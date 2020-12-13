import sys
import stddraw

width = 10
height = width * 2**0.5

stddraw.setXscale(-1,height+1)
stddraw.setYscale(-1,height+1)
'''测试用
x = [0,width,width,0]
y = [height,height,0,0]
stddraw.polygon(x,y)
#stddraw.square(5,5,2.5)
for i in range(len(y)):
	y[i] = y[i]/2
stddraw.polygon(x,y)
'''
n = eval(sys.argv[1])
x = [0,width,width,0]
y = [height,height,0,0]
for i in range(1,n+1):
	if i == 1:
		True
	elif i % 2 == 0:
		for i in range(4):
			y[i] = y[i]/2
	else:
		for i in range(4):
			x[i] = x[i]/2
	stddraw.polygon(x,y)		
stddraw.show()
