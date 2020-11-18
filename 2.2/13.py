import random

def shuffle(a=[]):
	n = len(a)
	for i in range(n):
		r = random.randrange(i,n)
		temp = a[r]
		a[r] = a[i]
		a[i] = temp
	
b = [1,2,3,4,5]
shuffle(b)
print(b)
