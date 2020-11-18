import random
import sys
# m=eval(sys.argv[1])
# n=eval(sys.argv[2])
m,n=3,10000
s=[]
for i in range(n):
	a=[i for i in range(m)]
	for j in range(m):
		r=random.randrange(j,m)
		#Problem 23 bad shuffling
		# r=random.randrange(0,m)
		temp=a[r]
		a[r]=a[j]
		a[j]=temp
	s.append(a)
# print('s:',s)
b=[[0]*m for i in range(m)]
for k in range(m):
	for i in range(m):
		si=0
		for j in range(n):
			if s[j][i]==k:
				si+=1
		b[k][i]=si/n
print('b:',b)
	
