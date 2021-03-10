#幻灯片放映，从命令行接受n个图片名称，进行幻灯片放映，间隔两秒，从图片渐变到黑，再渐变到下一张图片
import sys
#import fade
import color
from color import Color
from picture import Picture
import stddraw

#根据alpha渐变图片
def blend(c1, c2, alpha):
    r = (1-alpha)*c1.getRed()   + alpha*c2.getRed()
    g = (1-alpha)*c1.getGreen() + alpha*c2.getGreen()
    b = (1-alpha)*c1.getBlue()  + alpha*c2.getBlue()
    return Color(int(r), int(g), int(b))

#压缩或放大图片到w*h
def scale(source,w,h):
    target = Picture(w,h)
    for tCol in range(w):
        for tRow in range(h):
            sCol = tCol * source.width() // w
            sRow = tRow * source.height() // h
            target.set(tCol, tRow, source.get(sCol, sRow))
    return target

#获取图片集
p = sys.argv[1:]

#将图片改为统一大小
w = 400
h = 500
l = len(p)
for i in range(l):
    p[i] = scale(Picture(p[i]),w,h)        

#从source渐变到target
def slideOne(source,target,n,w,h):
    pic = Picture(w,h)
    for t in range(n):
        for col in range(w):
            for row in range(h):
                c0 = source.get(col, row)
                cn = target.get(col, row)
                alpha = float(t) / float(n)
                c = blend(c0, cn, alpha)
                pic.set(col, row, c)
        stddraw.picture(pic)
        stddraw.show(2000.0/n)  #2秒一张为2000/n

#幻灯片放映,p为照片集，n为2秒内变化的张数
def slideShow(p,n,w,h):
    l = len(p)
    #创建黑色图像
    blackP = Picture(w,h)
    for col in range(w):
        for row in range(h):
            blackP.set(col,row,color.BLACK)

    for i in range(l-1):
        slideOne(p[i],blackP,n,w,h)
        slideOne(blackP,p[i+1],n,w,h)
    
    stddraw.picture(p[l-1])
    stddraw.show()

slideShow(p,3,400,500)
stddraw.show()

'''
for i in range(l):
    stddraw.picture(p[i])
    stddraw.show(1000)

c1 = Color(0,0,0)
c2 = Color(255,255,255)
alpha = .5

print(blend(c1,c2,alpha))
'''


