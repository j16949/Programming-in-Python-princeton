import math
import sys

def evaluate(x,a=[]):
	i = len(a)-1
	t = a[i]
	while i > 0:
		t = a[i-1]+x*t
		i -= 1
	return t

def exp(x):
	n = 100	#泰勒展开n项
	a =[1]
	t = 1	#计算阶乘
	for i in range(1,n+1):
		t = t*i
		a.append(1/t)
	return evaluate(x,a)

#print(exp(eval(sys.argv[1])))
print(exp(-5))
print(math.e**-5)
print(exp(0))
print(math.e**0)
print(exp(0.5))
print(math.e**0.5)
print(exp(1))
print(math.e**1)
print(exp(6))
print(math.e**6)
print(exp(66))
print(math.e**66)