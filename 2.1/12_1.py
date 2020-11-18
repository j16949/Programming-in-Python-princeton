'''为了和12.py做对比，发现str和list的传参不完全一样，
str虽然可以用s[i]取值，但是不能更改，类似tuple,但可以增加(s += 'abc')。
但是list传参就是引用，append会导致原数组边长。
'''
import sys

def f(x):
	s = 2*x
	r = s//10 + s % 10
	return r

def cs(l=[]):
	st = 0
	for j in range(len(l)):
		if j % 2 == 0:
			st += l[j]
		else:
			st += f(l[j])
	for i in range(10):
		if (st + i)%10 == 0:
			l.append(i) 

l1=[ i for i in range(4) ]
print('l1_old',l1)
cs(l1)
print('l1_new',l1)
