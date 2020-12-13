import sys
import random

#用数组模拟Pancake,从1-n表示饼的大小
def init_Pancake(n):
	l = []
	for i in range(1,n+1):
		l.append(i)
	random.shuffle(l)
	print('init_Pancake:',l)
	return l

def flip(n,l):
	global f 	#用于记数
	if n == 1 : return [1]
	#把第n块反转到最下方
	index = l.index(n)
	while index != n-1:
		#n位于顶部，全部反转
		if index == 0:
			l.reverse()
			print(l)
			f += 1
		#n不位于顶部，反转从顶部至第index块
		else:
			t = l[:index+1]
			l = t[::-1]+l[index+1:]
			print(l)
			f += 1
		index = l.index(n)
	#flip上面的n-1块
	l=flip(n-1,l[:-1])+[l[-1]]
	return l



n = 5
f = 0
print(flip(n,init_Pancake(n)))
print('最大允许反转:',2*n-3)
print('实际反转:',f)
	
