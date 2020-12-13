import sys

n = eval(sys.argv[1])

s = ''

while n > 0:
	s += str(n%2)
	n //= 2

print(s[::-1])
