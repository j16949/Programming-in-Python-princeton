from math import *
import sys
#q=eval(input('请输入任意角度:'))
q=eval(sys.argv[1])
print(sin(degrees(q))**2+cos(degrees(q))**2)
