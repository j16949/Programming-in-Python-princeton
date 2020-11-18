import sys
import math

def between(ymin,ymax,a=[]):
	if ymin > ymax:
		return False
	betw = ymax - ymin
	mi = min(a)
	bea = max(a)-min(a)
	for i in range(len(a)):
		a[i] = ymin + (a[i]-mi)/bea*betw
	return a

ymin = eval(sys.argv[1])
ymax = eval(sys.argv[2])
b = []
for i in range(3,len(sys.argv)):
	b.append(eval(sys.argv[i]))
print(between(ymin,ymax,b))
