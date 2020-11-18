import sys
import math

x=eval(sys.argv[1])
y=eval(sys.argv[2])
r=pow(x**2+y**2,0.5)
th=math.atan2(y,x)
print(r,math.degrees(th))
