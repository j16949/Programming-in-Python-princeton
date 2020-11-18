import numpy as np

def multiply(a=[],b=[]):
	if len(a[0]) != len(b):
		print('a的列数不等于b的行数')
		return False
	else:
		n = len(b)
	l = len(b[0])
	w = len(a)
	c =[ [0]*l for i in range(w) ]
	for i in range(w):
		for j in range(l):
			for t in range(n):
				c[i][j] += a[i][t]*b[t][j]
	return c

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(multiply(a,b))
				
