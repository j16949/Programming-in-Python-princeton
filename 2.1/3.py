import sys
import stdarray

def noif(a=[]):
	return (a[0] or a[1]) and (a[1] or a[2]) and (a[0] or a[2])

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
print(noif(ll))
