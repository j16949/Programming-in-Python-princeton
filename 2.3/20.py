import sys
import math

def ntos(n):
	s =''
	for i in range(n):
		s = s + chr(97+i)
	return s

def comb(s,k):
	if len(s) == k : return {s}
	r = set()
	for i in range(len(s)):
		subStrings = comb(s[:i]+s[i+1:],k)
		for subString in subStrings:
			r.add(subString)
	return r
	
n = eval(sys.argv[1])
k = eval(sys.argv[2])
print(ntos(n))
print(comb(ntos(n),k))
print(math.factorial(n)/math.factorial(n-k)/math.factorial(k))

