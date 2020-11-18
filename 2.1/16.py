import sys

def histogram(m,a=[]):
	b=[0] * eval(m)
	for t in a:
		b[eval(t)]+=1
	return b

print(histogram(sys.argv[-1],sys.argv[1:-1]))

