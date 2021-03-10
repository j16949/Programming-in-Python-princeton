#rawpicture.py模块，使用例子参加26.py
import stddraw
from picture import Picture
from color import Color
import stdio

#不带参数，从标准输入读入数据 python3 xxx.py < a.txt,返回图片对象p
def read():
    w = stdio.readInt()
    h = stdio.readInt()
    p = Picture(w,h)
    for col in range(w):
        for raw in range(h):
            r = stdio.readInt()
            g = stdio.readInt()
            b = stdio.readInt()
            c = Color(r,g,b)
            p.set(col,raw,c)
    return p

#输入Picture对象p，返回p的长宽和每个点的像素rgb值
def write(p):
    h = p.height()
    w = p.width()
    l = [[[0 for k in range(3)] for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            c = p.get(j,i)
            l[i][j][0] = c.getRed()
            l[i][j][1] = c.getGreen()
            l[i][j][2] = c.getBlue()
    return w,h,l

def main():
    p = Picture('heroes-Peter.jpg')
    w,h,l=write(p)
    print(w)
    print(h)
    for i in range(2):
        print(l[i])

if __name__ == '__main__':
    main()
