import sys
def isSpring(a,b):
	ans=False
	if a==3:
		if 20<=b<32:
			ans= True
	elif a==4:
		if 0<b<31:
			ans= True
	elif a==5:
		if 0<b<32:
			ans= True
	elif a==6:
		if 0<b<21:
			ans= True
	return ans
 
a=eval(sys.argv[1])
b=eval(sys.argv[2])
print(isSpring(a,b))

