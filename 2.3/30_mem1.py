#使用字典,持久化更多数据，相比多于基于list的30_mem.py
import sys

total = 0

d = dict()


def collatz(n):
	global d,total
	total += 1
	if n == 1:
		return str(n)+' '
	elif n % 2 == 0:
		temp0 = n//2
		if temp0 not in d:
			d[temp0]=str(n)+' '+collatz(n // 2)
		return d[temp0]				
	else:
		temp = 3*n + 1
		if temp not in d:
			d[temp]=str(n)+' '+collatz(3*n + 1)
		return d[temp]

#m = eval(sys.argv[1])
m = 29
r = 0
l = ['' for i in range(m)]
for i in range(1,m):
	print(collatz(i))
	l[i]=collatz(i)
	print('total:',total)
	total = 0


longest = 0
il = 0
for i in range(1,len(l)):
	t = len(l[i])
	if t > longest:
		longest=t
		il=i

li = l[il].split()
print('result:',len(li))

# for key in d:
# 	print(d[key])
