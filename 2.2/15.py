import stdrandom
import stdstats
import stddraw

def twodice():
	a1 = stdrandom.uniformInt(0,6)
	a2 = stdrandom.uniformInt(0,6)
	return a1+a2+2

def twoloadeddice(a=[]):
	a1 = stdrandom.discrete(a)
	a2 = stdrandom.discrete(a)
	return a1+a2+2	#a1和a2取值范围为0-5，所以加2

def crap(dice,a):
	x = dice(a)
	if x == 7 or x == 11:
		return True
	elif x == 2 or x == 3 or x == 12:
		return False
	else:
		y = dice(a)
		while y != x and y != 7:
			y = dice(a)
	if y == x:
		return True
	else:
		return False

def trycrap(n,dice1,a):
	s = 0
	for i in range(n):
		if crap(dice1,a):
			s += 1
	return s/n

n=10000
#print(trycrap(n,twodice))
a=[1,1,1,1,1,1]
print(trycrap(n,twoloadeddice,a))
b=[1.5,1,1,1,1,.5]
print(trycrap(n,twoloadeddice,b))
