import random
n=10000
a=[]
for i in range(1,14):
	a.append('clubs')
for i in range(14,27):
	a.append('diamonds')
for i in range(27,40):
	a.append('hearts')
for i in range(40,53):
	a.append('spades')
fir,se,th=0,0,0

for j in range(n):
	random.shuffle(a)
	c,d,h,s=0,0,0,0
	for i in range(1,14):
		if a[i]=='clubs':
			c+=1
		elif a[i]=='diamonds':d+=1
		elif a[i]=='hearts':h+=1
		elif a[i]=='spades':s+=1
	
	if c==5 and d==3 and h==3 and s==2:fir+=1
	if c==4 and d==4 and h==3 and s==2:se+=1
	if c==4 and d==3 and h==3 and s==3:th+=1
print(fir,se,th)
