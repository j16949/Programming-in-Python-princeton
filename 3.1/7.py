#不知道理解是否正确，输出一个不包含白色的矩形,未完成
import sys
import luminance
import stdstats
import stddraw
from picture import Picture
from color import Color

#pic = Picture(sys.argv[1])
pic = Picture('me.jpg')
h = pic.height()
w = pic.width()
WEIGHT = str(Color(255,255,255))
tb = [[0,0] for i in range(h)]  #每行非白色起点
te = [[0,0] for i in range(h)]  #每行非白色终点

row = 0
col = 0
while row < pic.height():
    while col < pic.width():
        pixel = pic.get(col,row)
        if col-1 >= 0 and str(pic.get(col-1,row)) == WEIGHT and str(pixel) != WEIGHT: 
            tb[row] = [row,col]
            while str(pixel) != WEIGHT:
                pixel = pic.get(col,row)
                col += 1
            te[row] = [row,col]
        col += 10
    row += 10
    col = 0

temp1 = 0
temp2 = 0
for i in range(h):
    if temp1 < tb[i][0]:
        temp1 = tb[i][0]
        temp2 = te[i][0]
print(temp1)
print(temp2)

'''
temp2 = w
for i in range(h):
    if te[i][0] != 0:
        if temp2 > te[i][0]:
            temp2 = te[i][0]
print(temp2)
'''
#stddraw.picture(pic)
stddraw.rectangle(temp1,0,temp2-temp1+1,h)
stddraw.rectangle(1,1,10,10)
stddraw.show()

