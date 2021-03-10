import sys
import luminance
import stdstats
import stddraw
from picture import Picture
from color import Color

pic = Picture(sys.argv[1])
h = pic.height()
w = pic.width()
redPic = Picture(w,h)
greenPic = Picture(w,h)
bluePic = Picture(w,h)

for col in range(pic.width()):
    for row in range(pic.height()):
        pixel = pic.get(col,row)
        redPic.set(col,row,Color(pixel.getRed(),0,0))
        greenPic.set(col,row,Color(0,pixel.getRed(),0))
        bluePic.set(col,row,Color(0,0,pixel.getRed()))

#stddraw.setXscale(-10,10000)
#stddraw.setYscale(-10,10000)

stddraw.picture(redPic)
stddraw.show(1000)
stddraw.picture(greenPic)
stddraw.show(1000)
stddraw.picture(bluePic)
stddraw.show()

