import random
n=3
a=[]
b=[]
c=0
for i in range(n):
	a.append([])
	for j in range(n):
		a[i].append(random.randrange(2))
print('a[]:\n',a)

for i in range(n):
	b.append([])
	for j in range(n):
		b[i].append(random.randrange(2))
print('b[]:\n',b)

for i in range(n):
	for j in range(n):
		c=(c or (a[i][j] and b[i][j]))
print('c:\n',c)


