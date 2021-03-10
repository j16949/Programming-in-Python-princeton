#从命令行接受一个图片文件名，展示出m*n的图片地板图案

import sys
import stddraw
from picture import Picture

m = 5
n = 4
w = 70
h = 70
#p = sys.argv[1]
p = 'me.jpg'
source = Picture(p)

#压缩或放大图片到w*h
def scale(source,w,h):
    target = Picture(w,h)
    for tCol in range(w):
        for tRow in range(h):
            sCol = tCol * source.width() // w
            sRow = tRow * source.height() // h
            target.set(tCol, tRow, source.get(sCol, sRow))
    return target

#缩小后的图片
scPicture = scale(source,w,h)

#大图片，也就是m*n的小图片的集合
TaPicture = Picture(w*m,n*h)

for i in range(m):
    for j in range(n):
        for col in range(w):
            for row in range(h):
                TaPicture.set(i*w+col,j*h+row,scPicture.get(col,row))

stddraw.picture(TaPicture)
stddraw.show()


