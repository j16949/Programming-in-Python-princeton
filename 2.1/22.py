import random

def birthday():
	s=[]
	i=random.randint(0,364)
	c=0
	while i not in s:
		s.append(i)
		i = random.randint(0,364)
		c += 1
	return c

t=0
for i in range(1000):
	t += birthday()
print(t/1000)
