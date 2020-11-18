import sys
		
def had(ho,n):
	# if n==1:
	# 	return [[True]]
	hn=[[[] for j in range(2*n)] for i in range(2*n)]
	for i in range(n):
		for j in range(n):
			hn[i][j]=ho[i][j]
	for i in range(n):
		for j in range(n,2*n):
			hn[i][j]=ho[i][j-n]
	for i in range(n,2*n):
		for j in range(n):
			hn[i][j]=ho[i-n][j]
	for i in range(n,2*n):
		for j in range(n,2*n):
			hn[i][j]=not ho[i-n][j-n]
	# for i in range(2*n):
	# 	for j in range(2*n):
	# 		print(hn[i][j],end=',')
	return hn

#n=eval(sys.argv[1])
n=8
g=[[] for i in range(2*n+1)]
g[1]=[[True]]
i=1
while i<=n:
	g[i*2]=had(g[i],i)
	i*=2
print('g{}:\n{}'.format(2*n,g[2*n]))




