import sys
a=eval(sys.argv[1])
b=eval(sys.argv[2])
if a%b==0 or b%a==0:
	print('True')
