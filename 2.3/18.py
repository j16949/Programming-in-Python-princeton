import sys
import math

#函数返回一个列表，列表中元素为排列字符串，分别在字符串的第i个位置插入序号为n的字母
def permutationofk(n,k):
	if n < k : return []
	if k == 0 : return []
	if n == 1 : return ['a']
	l = permutationofk(n-1,k-1)
	r = []
	for i in range(k):
		for j in range(len(l)):
			r.append(l[j][:i]+chr(n+96)+l[j][i:])	#使用ascii/unicode码
	if l == [] : return [chr(n+96)] + permutationofk(n-1,k)
	return r + permutationofk(n-1,k)

n = 5
k = 3
print(permutationofk(n,k))
print(len(permutationofk(n,k)))
print(math.factorial(n)/math.factorial(n-k))

		
