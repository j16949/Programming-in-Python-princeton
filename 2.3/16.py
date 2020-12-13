#和H图不同，递归的是x和y的值
import sys
import stddraw

def paper(n):
	if n == 1 :
		global width,height
		x = [0,width,width,0]
		y = [height,height,0,0]
		stddraw.polygon(x,y)
		return x,y
	t = paper(n-1)
	if n % 2 == 0:
		x = t[0]
		y = [0]*4
		for i in range(4):
			y[i] = t[1][i]/2
	else:
		x = [0]*4
		for i in range(4):
			x[i] = t[0][i]/2
		y = t[1]
	stddraw.polygon(x,y)
	return x,y

width = 10
height = width*2**0.5 

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
#x = [0,width,width,0]
#y = [height,height,0,0]
n = eval(sys.argv[1])
#n = 2
paper(n)
stddraw.show()
