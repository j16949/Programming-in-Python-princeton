n=eval(input('Please input n:'))
s=input('Please input n-1 distinct integers(between 1 and n):')
ls=s.split(' ')
for i in range(1,n+1):
	if str(i) not in ls:
		print(i)
