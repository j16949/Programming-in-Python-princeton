import sys

def areTriangular(a=[]):
	a = [eval(x) for x in a]
	print(a)
	if a[0] + a[1] > a[2]:
		if a[1] + a[2] > a[0]:
			if a[0] + a[2] > a[1]:
				return True
	return False

sys.argv.pop(0)
print(areTriangular(sys.argv))
