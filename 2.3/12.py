#f(n)调用f(1)的次数,为f(n-1)调用f(1)的次数+f(n-2)调用f(1)的次数
#其中f(1)==1,f(0)==0
import sys

def fib(n):
	if n == 0: return 0
	if n == 1: return 1
	return fib(n-1)+fib(n-2)

def countf(n):
	if n == 0: return 0
	if n == 1 : return 1
	return countf(n-1) + countf(n-2)

n = int(sys.argv[1])
print(fib(n))
