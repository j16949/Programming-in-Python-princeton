n=10
a=[[0 for j in range(n)] for i in range(n)]
a[0][0]=0
a[0][1]=1
for i in range(n):
	for j in range(1,i+1):
		a[i][j]=(a[i-1][j-1]+a[i-1][j])
for i in range(n):
	for j in range(n):
		print(a[i][j],end=' ')
	print()
print()
