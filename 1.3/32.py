import sys
a=eval(sys.argv[1])
n=a+1
for i in range(n):
	if i**3>a:break
	for j in range(i+1,n):
		if j**3+i**3>a:break
		for p in range(i+2,n):
			for q in range(p+1,n):
					if i**3+j**3<p**3+q**3:break
				#if i!=p and i!=q and j!=p and j!=q:
					if i**3+j**3==p**3+q**3:
						print(i,j,p,q)
