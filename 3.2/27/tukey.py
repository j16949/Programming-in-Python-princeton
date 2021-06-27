import stdstats
import stddraw

def compute(a=[]):
	a.sort()
	b = []
	b.append(stdstats.mean(a))
	b.append(stdstats.stddev(a))
	b.append(a[int(len(a)/10)])
	b.append(a[int(len(a)*9/10)])
	#print(b)
	return b

def TukeyPlot(b=[]):
	stddraw.setXscale(0,6)
	stddraw.setYscale(b[2]-1,b[3]+1)
	stddraw.line(3,b[2],3,b[3])	#绘制中线
	x = [2,4,4,2]
	ly = b[0]-b[1]
	hy = b[0]+b[1]
	y = [hy,hy,ly,ly]
	stddraw.polygon(x,y)

def TP(a=[]):
	return TukeyPlot(compute(a))

def main():
	c = [1,2,3,4,5,6,7,8,9]
	c1 = [3,3,3,4,5,7,7,7,7]
	TP(c)
	stddraw.show()

if __name__=='__main__':
	main()