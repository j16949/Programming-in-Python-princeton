#定义line为y=ax+b函数
from decimal import Decimal
import math

class Line:
    #严格要求x1<=x2;y1<=y2
    def __init__(self,x1,y1,x2,y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if x2 != x1:
            self._a = (y2-y1)/(x2-x1)
            self._b = y1 - self._a * x1
            self._c = None
        else:
            #一条 x = c 的竖线
            self._a = None
            self._b = None
            self._c = x1
        
        #self._length = math.sqrt((y2-y1)*(y2-y1)+(x2-x1)*(x2-x1))

    #判断两个一次函数是否相交，准确地说是一次函数的一部分(x1-x2)
    def cross(self,other):
        #取值范围为中间部分
        x_l = max(self._x1,other._x1)
        x_r = min(self._x2,other._x2)
        #判断是否存在竖线
        if self._c != None:
            #两条都是竖线
            if other._c == self._c:
                if other._y2 > self._y2 >= other._y1:
                    return True
                elif other._y2 >= self._y1 > other._y1:
                    return True
                elif self._y2 >= other._y2 >= other._y1 >= self._y1:
                    return True
            else:
                #当self是竖线，other是斜线时，判断当 x = self.c 时，斜线是否落在竖线上
                if other._x1 <= self._c <= other._x2:
                    if self._y1 <= other._a * self._c + other._b <= self._y2:
                        return True
        elif other._c != None:
            if self._x1 <= other._c <= self._x2:
                if other._y1 <= self._a * other._c + self._b <= other._y2:
                    return True
        #斜率不同有相交
        elif self._a != other._a:
            x = (other._b - other._b)/(self._a - other._a)
            if x_l <= x <= x_r :
                return True 
        #如果斜率相同，b也相同，说明是同一条直线，判断重合部分
        elif  self._b == other._b:
            #判断x是否重合
            if other._x2 > self._x2 >= other._x1:
                return True
            elif other._x2 >= self._x1 > other._x1:
                return True
            elif self._x2 >= other._x2 >= other._x1 >= self._x1:
                return True
        return False

def main():
    line1 = Line(0,0,1,1)
    line2 = Line(-1,-1,0,0)
    print(line1.cross(line2))
    line3 = Line(0,3,0,6)
    line4 = Line(0,1,0,3)
    print(line3.cross(line4))
    line5 = Line(3,0,6,0)
    line6 = Line(1,0,3,0)
    print(line5.cross(line6))
    print(line1.cross(Line(0,0.1,0,1)))
    print(line1.cross(Line(0,1,1,2)))
    print(line3.cross(Line(0,4,0,5)))
    linex = Line(-2,-3,-2,3)
    liney = Line(-4,-12,-4,14)
    print(linex.cross(liney))

if __name__ == '__main__':
    main()

