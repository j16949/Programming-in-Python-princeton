import random
import sys
m=eval(sys.argv[1])
n=eval(sys.argv[2])
p=eval(sys.argv[3])
a=[['.' for j in range(n)] for i in range(m)]
countp=round(m*n*p)
for i in range(countp):
	a[random.randrange(m)][random.randrange(n)]='*'

#print a
for i in range(m):
	for j in range(n):
		print(a[i][j],end=' ')
	print()
print()

b=[[' ' for j in range(n+2)] for i in range(m+2)]
for i in range(m):
	for j in range(n):
		b[i+1][j+1]=a[i][j]
#print b
for i in range(m+2):
	for j in range(n+2):
		print(b[i][j],end=' ')
	print()
print()

for i in range(m+2):
	for j in range(n+2):
		if b[i][j]=='.':
			s=0
			for x in range(i-1,i+2):
				for y in range(j-1,j+2):
					if b[x][y]=='*':
						s+=1
			b[i][j]=s
#print b
for i in range(m+2):
    for j in range(n+2):
        print(b[i][j],end=' ')
    print()
print()

