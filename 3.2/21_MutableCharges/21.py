from charge import Charge
import stddraw
import stdarray
from picture import Picture
from color import Color

a = stdarray.create1D(3)
a[0] = Charge(.4, .6, 50)
a[1] = Charge(.5, .5, -5)
a[2] = Charge(.6, .6, 50)

MAX_GRAY_SCALE = 255
p = Picture()
stddraw.setCanvasSize(p.width(),p.height())
for t in range(100):
    # Compute the picture p.
    for col in range(p.width()):
        for row in range(p.height()):
            # Compute pixel color.
            x = 1.0 * col / p.width()
            y = 1.0 * row / p.height()
            v = 0.0

            for i in range(3):
                v += a[i].potentialAt(x, y)    
            v = (MAX_GRAY_SCALE / 2.0)  + (v / 2.0e10)
            if v < 0:
                grayScale = 0
            elif v > MAX_GRAY_SCALE:
                grayScale = MAX_GRAY_SCALE
            else:
                grayScale = int(v)            
            color = Color(grayScale, grayScale, grayScale)
            p.set(col, p.height()-1-row, color)

    stddraw.clear()
    stddraw.picture(p)
    stddraw.show(0)
    a[1].increaseCharge(-2.0)
    #print(a[1]._q)

