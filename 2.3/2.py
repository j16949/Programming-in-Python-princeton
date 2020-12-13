import sys
import math

def lnFactorial(n):
	if n == 1: return 0
	return math.log(n,math.e)+lnFactorial(n-1)

print(lnFactorial(eval(sys.argv[1])))
