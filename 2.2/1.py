import math
import stdstats
import stddraw

def sinh(x):
	e = math.e
	return (e**x-e**(-x))/2

def cosh(x):
	e = math.e
	return (e**x+e**(-x))/2

def main():
	sh = []
	ch = []
	x = -5
	while x < 5:
		sh.append(sinh(x))
		ch.append(cosh(x))
		x += 0.2
	y = max(max(sh),max(ch))
	print(sh)
	print(ch)
	print(y)
	stddraw.setYscale(-y,y)
	stdstats.plotPoints(sh)
	stdstats.plotLines(ch)
	stddraw.show()

if __name__ == '__main__':main()
