import stdrandom
import stdstats
import stddraw

def twodice():
	a1 = stdrandom.uniformInt(1,7)
	a2 = stdrandom.uniformInt(1,7)
	return a1+a2

def SicheDice():
	d1 = [1,3,4,5,6,8]
	d2 = [1,2,2,3,3,4]
	a1 = stdrandom.uniformInt(0,6)
	a2 = stdrandom.uniformInt(0,6)
	return d1[a1]+d2[a2]

def crap(n):
	r = [0] * 13
	for i in range(n):
		t = twodice()
		r[t] += 1
	return r

def crapS(n):
	r = [0] * 13
	for i in range(n):
		t = SicheDice()
		r[t] += 1
	return r

def drawDice(a = []):
	stddraw.setYscale(0,1.1*max(a))
	stdstats.plotBars(a)

n = 1000000
d = crap(n)
dS = crapS(n)
print(d)
print(dS)
print(((d[7]+d[11]))/sum(d))
print((d[2]+d[3]+d[12])/sum(d))
drawDice(d)
stdstats.plotLines(dS)
stddraw.show()
