import sys
import stdarray

def odd(a=[]):
	s = 0
	for t in a:
		if t == True:
			s += 1
#	print(s)
	if s % 2 == 0:
		return False
	else:
		return True

#把[0，1，0，1，1]输入转化为[False,True.....]
def trans(b=[]):
	c = stdarray.create1D(len(b))
	for i in range(len(b)):
		if b[i] == '1':
			c[i] = True
		else:
			c[i] = False
	return c

l = []
for t in sys.argv:
	l.append(t)
l.pop(0)
ll=trans(l)
#print(ll)
print(odd(ll))
