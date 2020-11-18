f=open('10.txt')
'''s=f.read().replace('\n',' ')
ls=s.split(' ')[:-1]
print(ls)'''
line=f.readline()
i=0
j=0
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
ts=[ [0] for i in range(m)]
print(ts)
weights=[0.25,.25,.5]
for i in range(len(ls)):
	for j in range(len(ls[i])):
		ts[i][0]+=ls[i][j]*weights[j]
print(ts)

