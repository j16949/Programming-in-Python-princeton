import random
def benLaw(a=[]):
	l=[0]*10
	for t in a:
		for i in range(1,len(l)):
			if eval(t[0]) == i:
				l[i] += 1
	total=sum(l)
	for i in range(len(l)):
		l[i] = '%.2f'%(l[i]/total*100)+'%'
	k = 0
	for t in l:
		k += eval(t[0:-1])
	print('k:',k)
	return l

with open('30.txt','r') as f:
	a=f.readlines()
print(benLaw(a))

n = 100
l = []
for i in range(n):
	l.append(str(random.randrange(1,1000)))
print(benLaw(l))