import random
# computes the exact probability distribution for the sum of two dice
p=[0 for i in range(13)]
for i in range(1,7):
	for j in range(1,7):
		p[i+j]+=1
for i in range(13):
	print(i,end=', ')
print()
print(p)
print(sum(p))
for k in range(2,13):
	p[k]/=36.0
print(p)

#simulate n dice throws
n=eval(input('please input n:'))
dice1,dice2=0,0
r=[0 for i in range(13)]
for i in range(n):
	dice1=random.randint(1,6)
	dice2=random.randint(1,6)
	r[dice1+dice2]+=1
print('r:',r)
s=sum(r)
probability=[0 for i in range(13)]
for i in range(2,13):
	probability[i]=r[i]/s
print('probability:',probability)

