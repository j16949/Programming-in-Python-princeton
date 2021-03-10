#图片玻璃化效果
#ti = si + random(-5,5)
#tj = sj + random(-5,5)


import sys
from picture import Picture
import stddraw
import math
import random

p = sys.argv[1]

x = 5   #模糊度
source = Picture(p)
w = source.width()
h = source.height()
target = Picture(w,h)

for si in range(h):
    for sj in range(w):
        ti = si + random.randint(-x,x)
        tj = sj + random.randint(-x,x)
        if 0<=tj<w and 0<= ti <h:
            target.set(int(sj),int(si),source.get(int(tj),int(ti)))

stddraw.picture(target)
stddraw.show()
