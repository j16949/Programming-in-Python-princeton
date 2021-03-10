#colorstudy.py 显示Albers正方形，从上到下蓝色递减，从左至右黑色递减
#蓝色为底色，上画灰度小方形

import stddraw
from color import Color
import luminance

n = 16  #16*16的正方形

stddraw.setXscale(-1,17)
stddraw.setYscale(-1,17)

#蓝底色
for y in range(n):
    c = Color(0,0,256-(y+1)*16)
    for x in range(n):
        stddraw.setPenColor(c)
        stddraw.filledSquare(x,y,.51)

#灰度方块
for x in range(n):
    c = Color(x*16,x*16,x*16)
    cg = luminance.toGray(c)
    for y in range(n):
        stddraw.setPenColor(cg)
        stddraw.filledSquare(x,y,.3)

stddraw.show()
