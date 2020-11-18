import sys
import math

def DtoRadin(d=[]):
	r = [ 0 for i in range(len(d))]
	for i in range(len(d)):
		r[i] = d[i]/180*math.pi
	return r

def subtend(d1,a1,d2,a2):
	d = d2 - d1
	a = a2 - a1
	return 2*math.asin(((math.sin(d/2))**2+math.cos(d1)*math.cos(d2)*(math.sin(a/2))**2)**(1/2))/math.pi*180

d = [0]*4
for i in range(1,5):
	d[i-1] = eval(sys.argv[i])
r=DtoRadin(d)
print(subtend(r[0],r[1],r[2],r[3]))
