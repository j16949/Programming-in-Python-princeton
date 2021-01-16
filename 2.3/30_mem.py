#使用list,可以将部分持久化，如果需要持久化更多数据，参见30_mem1.py,即基于dict
import sys

total = 0
s = ''
#d = dict()


def collatz(n):
	global s,l,total
	s += str(n) + ' '
	total += 1
	if n == 1:
		return
	elif n % 2 == 0:
		if n//2 < len(l) and l[n//2]:
			s += l[n//2]
		else:
			collatz(n // 2)
	else:
		temp = 3*n + 1
		if temp < len(l) and l[temp]:
			# if l[temp]:
			s += l[temp]
		else:
			collatz(3*n + 1)

#m = eval(sys.argv[1])
m = 29
r = 0
l = ['' for i in range(m)]
for i in range(1,m):
	collatz(i)
	l[i]=s
	print('['+str(i)+']'+'total:',total)
	total = 0
	s = ''

longest = 0
il = 0
for i in range(1,len(l)):
	t = len(l[i])
	if t > longest:
		longest=t
		il=i
	print(l[i])

li = l[il].split()
print('result:',len(li))
