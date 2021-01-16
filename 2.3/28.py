#更好的实现版本，用数组存储已经计算过的值，其实不如用循环直接算
import math
import sys

total = 0	#记录总数

n = 10
k = 5

#数组a用于存储计算过的二项分布的值a
a = []
for i in range(n+1):
	a.append([0] * (i+1)) 
a[0][0]=1

def binomial(n,k):
	global total
	global a
	#if (n==0) and (k==0): return 1.0
	if (n<0) or (k<0) or (k>n): return 0.0
	total += 1
	
	if (n-1)<k:
		x = 0
	elif a[n-1][k]:
		x = a[n-1][k]
	else:
		x = binomial(n-1,k)
	if k-1 < 0:
		y = 0
	elif a[n-1][k-1]:
		y = a[n-1][k-1]
	else:
		y = binomial(n-1,k-1)
	a[n][k]=(x+y)/2
	return (x+y)/2

#k=eval(sys.argv[1])
#n=eval(sys.argv[2])

#测试数据
'''
k=0
n=5

for i in range(n):
	for j in range(i+1):
		print(binomial(i,j),end=' ')
	print()
'''
print(binomial(n,k))
print(a)
print(total)

'''''''''''''''''''''''''''''''''''

a[0][0]=1
a[1][0]=1/2 =(a[0][0]+a[0][-1])/2=（1+0）/2
a[1][1]=1/2 =(a[0][1]+a[0][0])/2=(0+1)/2



书中原方法
def binomial(n,k):
	if (n==0) or (k==0): return 1.0
	if (n<0) or (k<0): return 0.0
	return (binomial(n-1,k)+binomial(n-1,k-1))/2

#k=eval(sys.argv[1])
#n=eval(sys.argv[2])
k=0
n=2

print('递归：',binomial(n,k))
'''

