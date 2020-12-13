import sys
import stddraw

def ruler(n):
	if n == 1: return '1'
	return ruler(n-1) + str(n) + ruler(n-1)

def drawRuler(n):
	s = ruler(n)
	l = len(s)
	stddraw.setXscale(-1,l+1)
	stddraw.setYscale(0,n*1.1)
	for i in range(l):
		stddraw.line(i,0,i,eval(s[i]))
	stddraw.show()

drawRuler(4)

