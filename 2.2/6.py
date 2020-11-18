import stdrandom
import stdstats
import stddraw
import sys
import math

def maxwellBo(sigma = 1.0):
	maxwellbo = math.sqrt(stdrandom.gaussian(0,sigma)**2+stdrandom.gaussian(0,sigma)**2+stdrandom.gaussian(0,sigma)**2)
	return maxwellbo

print(maxwellBo(eval(sys.argv[1])))
