import sys
import math
r=0.03
p=eval(sys.argv[1])
t=eval(sys.argv[2])
print(p*math.e**(r*t))
