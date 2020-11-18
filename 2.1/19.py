def any(a=[]):
	for t in a:
		if t:
			return True
	return False

def all(a=[]):
	for t in a:
		if not t:
			return False
	return True

a=[True,False,True]
b=[True,True]
c=[False]
print('a:',a,'any:',any(a),'all:',all(a))
print('b:',b,'any:',any(b),'all:',all(b))
print('c:',c,'any:',any(c),'all:',all(c))
