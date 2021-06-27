#-----------------------------------------------------------------------
# juliaSets.py
# 并不明白算法，x0,y0改变算法，照搬JAVA版
#-----------------------------------------------------------------------

import sys
import stddraw
import stdio
from color import Color
from picture import Picture

#-----------------------------------------------------------------------

# Compute the Mandelbrot iteration sequence starting at z0, and 
# return the number of iterations for which the magnitude stays less
# than 2, up to the limit.

def julia(z,c,limit):
    #z = z0
    for t in range(limit):
        if abs(z) > 2.0:
            return t
        z = z * z + c
    return limit

#-----------------------------------------------------------------------

# Accept float command-line arguments xc, yc, and size that specify
# the center and size of a square region of interest. Make a digital
# image showing the result of sampling the Mandelbrot set in that
# region at a 512*512 grid of equally spaced pixels. Color each pixel
# with a grayscale value that is determined by counting the number of
# iterations before the Mandelbrot sequence for the corresponding
# complex number grows past 2.0, up to 255.

MAX = 255

#n = int(sys.argv[1])
#xc = float(sys.argv[2])
#yc = float(sys.argv[3])
#size = float(sys.argv[4])
#c = float(sys.argv[5])

n = 512
xc = -2
yc = -2
size = 4
c = complex(-0.75,0.1)

mColor = []
for i in range(256):
    r=stdio.readInt()
    g=stdio.readInt()
    b=stdio.readInt()
    mColor.append(Color(r,g,b))

pic = Picture(n, n)
for col in range(n):
    for row in range(n):
        #x0 = xc - (size / 2) + (size * col / n)
        #y0 = yc - (size / 2) + (size * row / n)
        x0 = xc  + (size * col / n)
        y0 = yc  + (size * row / n)
        z0 = complex(x0, y0)
        temp = julia(z0,c,MAX)
        #print(temp,end = ' ')
        #gray = MAX - julia(z0,c,MAX)
        #gray = MAX - temp
        color = mColor[temp]
        pic.set(col, n-1-row, color)

stddraw.setCanvasSize(n, n)
stddraw.picture(pic)
stddraw.show()


#-----------------------------------------------------------------------
#python3 juliaSets.py < mandel.txt 

# python mandelbrot.py 512 -.5 0 2

# python mandelbrot.py 512 .1015 -.633 .01
