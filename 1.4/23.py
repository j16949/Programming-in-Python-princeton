import random
n=20
m=100
t=0
for j in range(m):
	a=[i for i in range(n)]
	random.shuffle(a)
	#标记是否连续
	s=0
	for i in range(n-2):
		if a[i]+1==a[i+1]:
			s=1
	t+=s
print(t/m)
