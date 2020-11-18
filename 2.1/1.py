import sys

def max2(a,b):
	if a > b :
		return a
	else:
		return b

def max3(a,b,c):
	return max2(max2(a,b),c)

a,b,c=sys.argv[1],sys.argv[2],sys.argv[3]
print(max3(a,b,c))
