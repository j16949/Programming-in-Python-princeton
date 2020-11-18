import sys
ls=[eval(sys.argv[1]),eval(sys.argv[2]),eval(sys.argv[3])]
ls.sort()
if ls[0]+ls[1]>ls[2]:
	print(True)
else:
	print(False)
