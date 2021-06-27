#-----------------------------------------------------------------------
# mandelbrot.py
#-----------------------------------------------------------------------

import sys
import stddraw
from color import Color
from picture import Picture
from stopwatch import Stopwatch
import math

#-----------------------------------------------------------------------

# Compute the Mandelbrot iteration sequence starting at z0, and 
# return the number of iterations for which the magnitude stays less
# than 2, up to the limit.

def mandel(z0, limit):
    z = z0
    for t in range(limit):
        if abs(z) > 2.0:
            return t
        z = z * z + z0
    return limit

#不使用复数，使用浮点数加减法
def mandel1(x0,y0, limit):
    x = x0
    y = y0
    for t in range(limit):
        if abs(math.sqrt(x*x+y*y)) > 2.0:
            return t
        x = x * x - y * y + x0  #1*1-3*3+1=-7
        y = y * x + x * y + y0  #3*1+1*3+1=7
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
n = 512
xc = -.5
yc = 0
size = 2


w1 = Stopwatch()
pic = Picture(n, n)
for col in range(n):
    for row in range(n):
        x0 = xc - (size / 2) + (size * col / n)
        y0 = yc - (size / 2) + (size * row / n)
        z0 = complex(x0, y0)
        gray = MAX - mandel(z0, MAX)
        color = Color(gray, gray, gray)
        pic.set(col, n-1-row, color)
print(w1.elapsedTime())


w2 = Stopwatch()
pic = Picture(n, n)
for col in range(n):
    for row in range(n):
        x0 = xc - (size / 2) + (size * col / n)
        y0 = yc - (size / 2) + (size * row / n)
        #z0 = [x0,y0]
        gray = MAX - mandel1(x0,y0, MAX)
        color = Color(gray, gray, gray)
        pic.set(col, n-1-row, color)
print(w2.elapsedTime())


stddraw.setCanvasSize(n, n)
stddraw.picture(pic)
stddraw.show()


#-----------------------------------------------------------------------
#bai@ubuntu:~/pythonProject/princeton/3.2$ python3 14_mandelbrotTime.py 
#pygame 1.9.6
#Hello from the pygame community. https://www.pygame.org/contribute.html
#5.372214317321777
#37.89339089393616

