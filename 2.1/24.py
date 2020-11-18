import sys
import math

def harmonicSmall(n):
	s = 0
	for i in range(1,n+1):
		s += 1/i
	return s

def harmonicLarge(n):
	r = 0.577215664901532
	return math.log(n)+r+1/(2*n)-1/(12*n*n)+1/(120*n**4)

def harmonic(n):
	if n < 100:
		return harmonicSmall(n)
	else:
		return harmonicLarge(n)

print(harmonic(eval(sys.argv[1])))

