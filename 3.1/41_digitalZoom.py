#图像聚焦,选择坐标放大图片某个部分
#带命令行参数4个，图片名p,比例s,坐标x,y

import sys
import stddraw
from picture import Picture

p = sys.argv[1]
source = Picture(p)
s = eval(sys.argv[2])
x = eval(sys.argv[3])
y = eval(sys.argv[4])
w = source.width()
h = source.height()

print(w,h)

#目标图像
target = Picture(w,h)

x0 = x-int(w*s/2)
x1 = x+int(w*s/2)
y0 = y-int(h*s/2)
y1 = y+int(h*s/2)

#中间图像
tw = x1-x0
th = y1-y0
mp = Picture(tw,th)

for i in range(x0,x1):
    for j in range(y0,y1):
        mp.set(i-x0,j-y0,source.get(i,j))

for colT in range(w):
    for rowT in range(h):
        colS = colT * tw // w
        rowS = rowT * th // h
        target.set(colT,rowT,mp.get(colS,rowS))

stddraw.picture(target)
stddraw.show()
