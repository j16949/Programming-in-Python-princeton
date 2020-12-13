#n为2的幂
import sys 

def t1(n):
	if n == 1 : return 1
	return t1(n/2)+1

def t2(n):
	if n == 1 : return 1
	return 2*t2(n/2)+1

def t3(n):
	if n == 1 : return 1
	return 2*t3(n/2)+n

def t4(n):
	if n == 1 : return 1
	return 4*t4(n/2)+3

#print(t1(eval(sys.argv[1])))
print(t4(eval(sys.argv[1])))
