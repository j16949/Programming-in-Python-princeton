import sys

def f(a=[]):
	for i in range(len(a)):
		a[i] = (a[i]-min(a))/(max(a)-min(a))
	return a

l = sys.argv[1:]
for t in range(len(l)):
	l[t] = eval(l[t])
print(f(l))
