import gaussian
import stdstats
import stddraw
import sys

#模拟SAT，总分范围400到1600，均值mu=1019,标准差sigma=209
def md(mu=1019,sigma=209):
	phi = []
	for i in range(400,1600,50):
		phi.append(gaussian.pdf(i,mu,sigma))
	stddraw.setYscale(0,1.1*max(phi))
	stdstats.plotLines(phi)
	stddraw.show()

mu = eval(sys.argv[1])
sigma = eval(sys.argv[2])
md(mu,sigma)
