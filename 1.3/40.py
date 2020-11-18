import random
n=100
total=0
for i in range(n):
	s=0
	for j in range(6):
		t=random.randrange(1,7)
		if t==1:
			s=1
	if s==1:
		total+=1
print(total/6/n)
