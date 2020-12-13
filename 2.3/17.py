import sys
import math

#函数返回一个列表，列表中元素为排列字符串，分别在字符串的第i个位置插入序号为n的字母
def permutation(n):
	if n == 1 : return ['a']
	l = permutation(n-1)
	r = []
	for i in range(n):
		for j in range(len(l)):
			r.append(l[j][:i]+chr(n+96)+l[j][i:])	#使用ascii/unicode码
	return r

n = 4
print(permutation(n))
print(len(permutation(n)))
print(math.factorial(n))

		
