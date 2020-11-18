import sys
import random
import math
import stddraw

def gaussian():
    r = 0.0
    while (r >= 1.0) or (r == 0.0):
        x = random.uniform(-1.0, 1.0) 
        y = random.uniform(-1.0, 1.0)
        r = x*x + y*y
    return x * math.sqrt(-2.0 * math.log(r) / r)

def gaussiansin():
	u=random.random()
	v=random.random()
	w=math.sin(2*math.pi*v)*(-2*math.log(u))**0.5
	return w

def draw(a=[]):
	stddraw.setXscale(-1,21)
	stddraw.setYscale(0,700)
	for k in range(len(a)):
		stddraw.filledRectangle(k,0,0.5,a[k])
	stddraw.show()

def g20(n):
	l = []
	a = [0] * 20
	for i in range(n):
		l.append(gaussian())
	#print('l:',l)	
	i = -5
	while i < 5:
		for t in l:
			if i < t < (i+0.5):
				a[int(2*i)+10] += 1
		i += 0.5
	draw(a)
	return a

def g20sin(n):
	l = []
	a = [0] * 20
	for i in range(n):
		l.append(gaussiansin())
	#print('l:',l)
	for i in range(20):
		for t in l:
			if i*.05 < t < (i+1)*.05:
				a[i] += 1
	return a


print(g20(eval(sys.argv[1])))
print(g20sin(eval(sys.argv[1])))

