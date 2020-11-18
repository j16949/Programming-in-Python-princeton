import stdrandom
import math

def exp(lamda):
	x = stdrandom.uniformFloat(0,1)
	return -math.log(x/lamda)

print(exp(10))
