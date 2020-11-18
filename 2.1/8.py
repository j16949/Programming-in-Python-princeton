import sys

def signum(x):
	if x > 0:
		return 1
	elif x < 0:
		return -1
	else:
		return 0

print(signum(eval(sys.argv[1])))
