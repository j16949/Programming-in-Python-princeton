#-----------------------------------------------------------------------
# 改写potential.py，从命令行读取参数n,用stdrandom.gaussian(mu,sigma)自动生成n个电荷
# 按照原题标准差10，图像无内容，改为150有图像
# potential.py
#-----------------------------------------------------------------------

import stddraw
import stdio
import stdarray
import stdrandom
import sys
from charge import Charge
from color import Color
from picture import Picture

# Read values from standard input to create an array of charged
# particles. Set each pixel color in an image to a grayscale value
# proportional to the total of the potentials due to the particles at
# corresponding points. Draw the resulting image to standard draw.

MAX_GRAY_SCALE = 255

# Read charges from standard input into an array.
#n = stdio.readInt()
n = eval(sys.argv[1])
charges = stdarray.create1D(n)
for i in range(n):
    x0 = round(stdrandom.uniformFloat(0,1),2)
    y0 = round(stdrandom.uniformFloat(0,1),2)
    q0 = stdrandom.gaussian(50,150)
    charges[i] = Charge(x0, y0, q0)
    print(str(charges[i]))

# Create a Picture depicting potential values.
pic = Picture()
for col in range(pic.width()):
    for row in range(pic.height()):
        # Compute pixel color.
        x = 1.0 * col / pic.width()
        y = 1.0 * row / pic.height()
        v = 0.0

        for i in range(n):
            v += charges[i].potentialAt(x, y)    
        v = (MAX_GRAY_SCALE / 2.0)  + (v / 2.0e10)
        if v < 0:
            grayScale = 0
        elif v > MAX_GRAY_SCALE:
            grayScale = MAX_GRAY_SCALE
        else:
            grayScale = int(v)            
        color = Color(grayScale, grayScale, grayScale)
        pic.set(col, pic.height()-1-row, color)

# Draw the Picture.
stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show()


#-----------------------------------------------------------------------

# python potential.py < charges.txt
