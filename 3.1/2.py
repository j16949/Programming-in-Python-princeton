from color import Color
import stddraw
import sys
from picture import Picture

r = eval(sys.argv[1])
g = eval(sys.argv[2])
b = eval(sys.argv[3])

c = Color(r,g,b)

pic = Picture(256,256)

for col in range(256):
    for row in range(256):
        pic.set(col,row,c)

stddraw.picture(pic)
stddraw.show()
