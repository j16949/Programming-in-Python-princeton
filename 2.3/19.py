import sys

def ntos(n):
	s =''
	for i in range(n):
		s = s + chr(97+i)
	return s

def combinations(s):
	if s == '' : return {' '}
	r = set()
	for i in range(len(s)):
		subStrings = combinations(s[:i]+s[i+1:])
		for subString in subStrings:
			r.add(subString)
	r.add(s)
	return r
	
n = eval(sys.argv[1])
print(ntos(n))
print(combinations(ntos(n)))
