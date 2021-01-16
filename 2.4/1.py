import sys
import stddraw
import PofInt
import percolationio
import hadamard
from scipy.special import comb

def PofRelativelyPrime(n):
	l = [[False] * n for i in range(n)]
	for i in range(n):
		for j in range(n):
			if PofInt.relativelyPrime(i,j):
				l[i][j] = True
	percolationio.draw(l,True)

def Pofhadamard(n):
	l = hadamard.had(n)
	percolationio.draw(l,True)

def odd(n):
	if n % 2 == 0:
		return False
	return True

def Pofx(n):
	l = [[False] * n for i in range(n)]
	for i in range(n):
		for j in range(n):
			if odd(comb(i,j)):
				l[i][j] = True
	percolationio.draw(l,True)

n = eval(sys.argv[1])
#n = 4
#PofRelativelyPrime(n)
#Pofhadamard(n)
Pofx(n)
stddraw.show()
