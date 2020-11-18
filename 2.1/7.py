import sys

def lg(x):
	s = 0
	while x > 1:
		x = x // 2
		s += 1
	return s

print(lg(eval(sys.argv[1])))
