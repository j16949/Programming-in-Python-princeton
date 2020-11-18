import sys
import stddraw
import math


def fouspike(n):
	m = 500
	x = [0] * m
	y = [0] * m
	t = -10
	for i in range(m):
		x[i] = t
		y[i] = 0
		for j in range(1,n+1):
			y[i] += math.cos(j*t)
		y[i] = y[i]/n
		t += 1/25
	stddraw.setXscale(-11,11)
	stddraw.setYscale(-3,3)
	for i in range(m-1):
		stddraw.line(x[i],y[i],x[i+1],y[i+1])
	stddraw.show()


fouspike(500)
