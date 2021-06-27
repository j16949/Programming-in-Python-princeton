# x =( -b +/- math.sqrt(b^2-4ac) )/2a
#复数除法运算方法：可以把除法换算成乘法做，在分子分母同时乘上分母的共轭。所谓共轭你可以理解为加减号的变换，互为共轭的两个复数相乘是个实常数。
from complex import Complex
import math

def fx(a,b,c):
    t = b*b - 4*a*c
    if t >= 0:
        return (-b + math.sqrt(t))/2/a,(-b - math.sqrt(t))/2/a
    else:
        b = Complex(b,0)
        a = Complex(a,0)
        k = Complex(0,math.sqrt(-t))
        p = 1/(a.conjugate()*a)._re
        x1 = (Complex(-1,0)*b + k)*Complex(.5,0)*a.conjugate()*Complex(p,0)
        x2 = (Complex(-1,0)*b - k)*Complex(.5,0)*a.conjugate()*Complex(p,0)
        return x1,x2
a = 2
b = -1
c = 1

x1,x2 = fx(a,b,c)
print(x1,x2)

