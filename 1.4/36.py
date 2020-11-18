import random

n=1000
s=[]
for i in range(n):
	r=[]
	while True:
		b=random.randrange(365)
		if b in r:break
		r.append(b)
	s.append(len(r))
print(sum(s)/len(s))
