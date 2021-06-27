from complex import Complex
from picture import Picture
from color import BLACK, Color
import stddraw
import sys


def coloring(x,y):
    z = Complex(x,y)
    l = [Complex(1,0),Complex(-1,0),Complex(0,1),Complex(0,-1)]
    c = [Color(255,0,0),Color(0,255,0),Color(0,0,255),Color(255,255,255)]
    t = 0
    while z not in l and z != Complex(0,0):
        z = z - ((z**4-Complex(1,0))/(Complex(4,0)*z**3))
        t += 1
        if t > 100:
            return Color(0,0,0)
        #print(z)
    #print('end:',z)
    for i in range(len(l)):
        if l[i] == z:
            return c[i]
    return Color(0,0,0)

#原版
#原版错误原因在于题中写明初始值收敛与4个根之一，而此处coloring函数的i的范围（0-200），j的范围(0-200)
#正确的coloring范围为x(-1,1),y(-1,1)
#n = eval(sys.argv[1])
n = 200
p = Picture(n,n)
for i in range(n):
    for j in range(n):
        p.set(i,j,coloring(i,j))
'''

#根据JAVA版改编
#n = eval(sys.argv[1])
xmin   = -1.0
ymin   = -1.0
width  =  2.0
height =  2.0
n = 200
p = Picture(n,n)
for i in range(n):
    for j in range(n):
        x = xmin + i * width  / n
        y = ymin + j * height / n
        p.set(i,j,coloring(x,y))
'''

stddraw.picture(p)
stddraw.show()
