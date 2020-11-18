import math
import random

def printmatrix2D(a=[]):
	m = len(a)
	n = len(a[0])
	for i in range(m):
		for j in range(n):
			print(a[i][j],end='\t')
		print()
	print()
	return True

def rand(m,n):
	a = [[0]*n for i in range(m)]
	for i in range(m):
		for j in range(n):
			a[i][j] = random.uniform(0,1)
	return a

def idenity(n):
	a = [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			if i == j:
				a[i][j] = 1
	return a

def dot(v1,v2):
	n = len(v1)
	t = 0
	for i in range(n):
		t += v1[i]*v2[i]
	return t

def transpose(m):
	row = len(m)
	columns = len(m[0])
	mt = [[0]*row for i in range(columns)]
	for i in range(row):
		for j in range(columns):
			mt[j][i] = m[i][j]
	return mt

def add(m1,m2):
	row = len(m1)
	col = len(m1[0])
	m3 = [[0]*col for i in range(row)]
	for i in range(row):
		for j in range(col):
			m3[i][j] = m1[i][j] + m2[i][j]
	return m3

def subtract(m1,m2):
	row = len(m1)
	col = len(m1[0])
	m3 = [[0]*col for i in range(row)]
	for i in range(row):
		for j in range(col):
			m3[i][j] = m1[i][j] - m2[i][j]
	return m3

def multiplyMM(m1,m2):
	row = len(m1)
	comm = len(m1[0])
	col = len(m2[0])
	m3 = [[0]*col for i in range(row)]
	for i in range(row):
		for j in range(col):
			for k in range(comm):
				m3[i][j] += m1[i][k] * m2[k][j]
	return m3

#矩阵乘以向量，返回一个一维数组1*n,n=len(m)
def multiplyMV(m,v):
	row = len(m)
	col = len(m[0])
	mv = [0] * row
	for i in range(row):
		for j in range(col):
			mv[i] += m[i][j] * v[j]
	return mv

#向量乘以矩阵，返回一个一维数组1*n,n=len(m)
def multiplyVM(v,m):
	row = len(v)
	col = len(m[0])
	mv = [0] * col
	for i in range(row):
		for j in range(col):
			mv[j] += m[i][j] * v[i]
	return mv


def main():
	printmatrix2D(rand(3,2))
	printmatrix2D(idenity(3))
	x1=[1,2,3]
	y1=[3,2,1]
	print(dot(x1,y1))
	x2=[[1,2,3],[4,5,6]]
	y2=[[4,5,6],[1,2,3]]
	printmatrix2D(transpose(x2))
	printmatrix2D(add(x2,y2))
	printmatrix2D(subtract(x2,y2))
	printmatrix2D(multiplyMM(x2,transpose(y2)))
	print(multiplyMV(x2,x1))
	print(multiplyVM(x1,transpose(x2)))

if __name__ == '__main__': main()
