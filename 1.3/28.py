import sys
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

x=eval(sys.argv[1])
y=eval(sys.argv[2])
print(gcd(x,y))
