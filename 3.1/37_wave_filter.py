#从命令行接收参数，波浪化扭曲图片
#ti = (si-ci)*costha-(sj-cj)sintha+ci
#tj = (si-ci)*sintha+(sj-cj)costha+cj


import sys
from picture import Picture
import stddraw
import math

p = sys.argv[1]
#degree = sys.argv[2]
amplitude = 20
frequency = 64

#tha = math.radians(eval(degree))    #radian(弧度)转角度
source = Picture(p)
w = source.width()
h = source.height()
ci = h/2
cj = w/2
target = Picture(w,h)

for si in range(h):
    for sj in range(w):
        ti = si 
        tj = sj + amplitude*math.sin(2*math.pi*sj/frequency)
        #target.set(int(tj),int(ti),source.get(sj,si))
        if 0<=tj<w and 0<= ti <h:
            target.set(int(sj),int(si),source.get(int(tj),int(ti)))

stddraw.picture(target)
stddraw.show()
