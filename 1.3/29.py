def gcd(a,b):
	while b != 0:
         t = a % b
         a = b
         b = t
	return a
n=10
for i in range(n):
	for j in range(n):
		if gcd(i,j)==1:
			print('*',end='')
		else:
			print(' ',end='')
	print()
	
