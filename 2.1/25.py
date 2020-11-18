import sys
import random
import math

def gaussian():
    r = 0.0
    while (r >= 1.0) or (r == 0.0):
        x = random.uniform(-1.0, 1.0) 
        y = random.uniform(-1.0, 1.0)
        r = x*x + y*y
    return x * math.sqrt(-2.0 * math.log(r) / r)

def g20(n):
	l = []
	a = [0] * 20
	for i in range(n):
		l.append(gaussian())
	print('l:',l)
	for i in range(20):
		for t in l:
			if i*.05 < t < (i+1)*.05:
				a[i] += 1
	return a

print(g20(eval(sys.argv[1])))

