from stdrandom import *
from stdstats import *
import stddraw

n = 3000
ui = []
uf = []
bm = []
gas = []
disc = []

for i in range(n):
	ui.append(uniformInt(0,10))
	uf.append(uniformFloat(0.0,10.0))
	bm.append(binomial(10,0.5))
	gas.append(gaussian(5.0,1.0))
	disc.append(discrete([5,3,1,1]))

def drawFun(a=[]):
	s = [0] * 10
	l = len(a)
	for i in range(l):
		for j in range(10):
			if j <= a[i] < j+1:
				s[j] += 1
	total=sum(s)
	print(s)
	for i in range(10):
		s[i] = s[i]/total
	plotBars(s)

stddraw.setYscale(0,1)
drawFun(gas)
stddraw.show()
