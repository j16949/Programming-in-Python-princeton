import stdrandom

t = 10000
s = 0 
for i in range(t):
	if stdrandom.binomial(12,0.05) > 0:
		s += 1
print(s/t)
