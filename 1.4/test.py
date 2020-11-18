s=''
f=open('10.txt')
line=f.readline()
s+=line
while line:
	line=f.readline()
	s+=line
print(s)
ls=list(s.split(' '))
print(ls)

n=2
a=[]
for i in range(n):
	a.append([])
	for j in range(n):
		a[i].append([])
		for p in range(n):
			a[i][j].append([])
print(a)


import numpy as np

data_array = np.zeros((3,5,6),dtype = np.int)
data_array[1,2,3] = 1

print(data_array)
a=list(data_array)
print(a)
