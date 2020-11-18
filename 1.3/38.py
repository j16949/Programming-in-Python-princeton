import math
import sys
import time
start = time.time()
x=math.pi/2
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
end = time.time()
print('Taylor\'s time:',str(end-start))
start = time.time()	
print('math.sin:',math.sin(x))
end = time.time()
print('Math\'s time:',str(end-start))
