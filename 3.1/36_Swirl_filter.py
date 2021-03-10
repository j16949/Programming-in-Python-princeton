#从命令行接收参数，旋转图片 
#dc =si-ci ,dr =sj-cj
#r = math.sqrt(dc**2+dr**2)
#angle = math.pi / 256.0 *r
#ti = dc*costha-dr*sintha+ci
#tj = dc*sintha+dr*costha+cj


import sys
from picture import Picture
import stddraw
import math

p = sys.argv[1]

source = Picture(p)
w = source.width()
h = source.height()
ci = h/2
cj = w/2
target = Picture(w,h)

for si in range(h):
    for sj in range(w):
        dc =si-ci
        dr =sj-cj
        r = math.sqrt(dc**2+dr**2)
        angle = math.pi / 256.0 *r
        ti = dc*math.cos(angle)-dr*math.sin(angle)+ci
        tj = dc*math.sin(angle)+dr*math.cos(angle)+cj
        #target.set(int(tj),int(ti),source.get(sj,si))
        if 0<=tj<w and 0<= ti <h:
            target.set(int(sj),int(si),source.get(int(tj),int(ti)))

stddraw.picture(target)
stddraw.show()
