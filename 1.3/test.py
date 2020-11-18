import math
import sys
# x=eval(sys.argv[1])
x=math.pi/3
total=0
term=x
i=2
while total!=total+term:
	total+=term
	term*=x/i
	i+=1
	term*=(-1)*x/i
	i+=1
	print(total)
print(total)
print('math.sin:',math.sin(x))
