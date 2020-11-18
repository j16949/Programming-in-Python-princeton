import sys
import random
n=eval(sys.argv[1])
r=n**2
x,y=0,0
i=0
while x**2+y**2<r:
	t=random.randrange(4)
	if t==0:x+=1
	elif t==1:x-=1
	elif t==2:y+=1
	elif t==3:y-=1
	i+=1
print(i)
