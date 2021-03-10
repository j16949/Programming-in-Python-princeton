import sys
import luminance
import stdstats
import stddraw
from picture import Picture

pic = Picture(sys.argv[1])
h = pic.height()
w = pic.width()
flipPic = Picture(h,w)

for col in range(pic.width()):
    for row in range(pic.height()):
        pixel = pic.get(col,row)
        flipPic.set(row,col,pixel)

stddraw.picture(flipPic)
stddraw.show()

