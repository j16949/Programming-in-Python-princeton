import sys
import stdarray
from matrix import multiplyVM
from matrix import multiplyMM

moves = int(sys.argv[1])
p = stdarray.readFloat2D()
ranks = stdarray.create1D(len(p),0.0)
ranks[0]=1.0
for i in range(moves):
	p = multiplyMM(p,p)
stdarray.write1D(multiplyVM(ranks,p))
