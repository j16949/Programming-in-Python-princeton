import sys

n = int(sys.argv[1])
a = 0
b = 1

for i in range(2,n+1):
	t = a
	a = b 
	b = t + b
	#print('l['+str(i)+']:',l[i])

print(b)
