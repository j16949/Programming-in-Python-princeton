f=open('11.txt')
line=f.readline()
i=0
ls=[]
t=''
while line:
	ls.append([])
	for s in line:
		if s == '\n':
			ls[i].append(eval(t))
			t=''
			break
		if s != ' ':
			t+=s
		else:
			ls[i].append(eval(t))
			t=''
	line=f.readline()
	i+=1
print(ls)
m=len(ls)
n=len(ls[0])
#ts=[ [0]*m for i in range(n)]
#print(ts)
for i in range(len(ls)):
	for j in range(i,len(ls[i])):
		t=ls[i][j]
		ls[i][j]=ls[j][i]
		ls[j][i]=t
print(ls)

