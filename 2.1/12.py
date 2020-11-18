import sys

def f(x):
	s = 2*x
	r = s//10 + s % 10
	return r

def cs(l):
	st = 0
	for j in range(len(l)):
		if j % 2 == 0:
			st += eval(l[j])
		else:
			st += f(eval(l[j]))
	for i in range(10):
		if (st + i)%10 == 0:
			l += str(i)
	return l

print(cs(sys.argv[1]))
