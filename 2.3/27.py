#-----------------------------------------------------------------------
# sierpinski.py递归版
#-----------------------------------------------------------------------

import sys
import stddraw
import stdrandom
import math

# Accept integer n as a command-line argument. Play chaos game on
# triangle to produce Sierpinski triangle of n points.

def sier(n,xl,yl,xr,yr,xm,ym):
	if n == 0:return

	stddraw.line(xl,yl,xr,yr)
	stddraw.line(xl,yl,xm,ym)
	stddraw.line(xr,yr,xm,ym)

	sier(n-1,xl,yl,xm,yr,(xl+xm)/2,(yl+ym)/2)
	sier(n-1,xm,yl,xr,yr,(xr+xm)/2,(yr+ym)/2)
	sier(n-1,(xl+xm)/2,(yl+ym)/2,(xr+xm)/2,(yr+ym)/2,xm,ym)

def main():
	n = int(sys.argv[1])
	stddraw.setXscale(-0.1,1.1)
	stddraw.setYscale(-0.1,1.1)
	sier(n,0,0,1,0,0.5,math.sin(math.pi/3))
	stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python sierpinski.py 1000

# python sierpinski.py 10000

# python sierpinski.py 100000

