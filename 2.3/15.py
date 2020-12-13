#十进制转二进制，字符法;无法显示0
import sys

def binary(n):
	if n == 0 : return ''
	r = n % 2
	y = n // 2
#	if y == 0 : return ''
	return  binary(y) + str(r)

n = eval(sys.argv[1])
print(binary(n))
