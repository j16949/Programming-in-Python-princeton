import sys

#定义类，因为在递归中数组不会初始化，当开启新一个数字的递归时，上一个数组延续。用类来为每一个对象实例化一个LIST
class Ysfj:
	def __init__(self):
		self.l = []

# def ysfj_result(n):
# 	l = []
# 	yinshifenjie(n)
# 	return l

	def yinshifenjie(self,n):
		i = 2
		t = 1
		while t != 0 and i < n:
			t = n % i
			i += 1
		if t == 0:
			self.l.append(i-1)
			a = n // (i-1)
			Ysfj.yinshifenjie(self,a)
		else:
			self.l.append(n)




def euler(n):
	s = 1
	tc =[None] * n
	N = Ysfj()
	N.yinshifenjie(n)
	for i in range(1,n):
		tc[i] = Ysfj()
		tc[i].yinshifenjie(i)
		j = 0		#判断一个数的因数分解结果是否在属于另一个数
		for t in tc[i].l:
			if t in N.l:
				j += 1
		if j == 0 and (n % i != 0):
			s += 1
			print('i:',i)
	return s

#print(euler(eval(sys.argv[1])))
#print(yinshifenjie(eval(sys.argv[1])))
#yinshifenjie(eval(sys.argv[1]))
# l=Ysfj()
# l.yinshifenjie(8)
# print(l.l)
# l=Ysfj()
# l.yinshifenjie(10)
# print(l.l)
print(euler(eval(sys.argv[1])))
