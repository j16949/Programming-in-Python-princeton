#最大可计算100000
import sys
import math
a=eval(sys.argv[1])
s=[]
for i in range(2,a+1):
	signal=0
	for j in range(2,int(i**.5)+1):
		if i % j==0:
			signal=1
	if signal==0:
		s.append(i)
#print(s)
print(len(s))

