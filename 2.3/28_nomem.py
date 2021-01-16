#更好的实现版本，用数组存储已经计算过的值，其实不如用循环直接算
import math
import sys

total = 0	#记录总数

n = 10
k = 5


def binomial(n,k):
	global total
	if (n==0) and (k==0): return 1.0
	if (n<0) or (k<0) or (k>n): return 0.0
	total += 1
	return (binomial(n-1,k)+binomial(n-1,k-1))/2

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

