import stddraw
from line import Line

class Rectangle:

    # Construct self with center (x, y), width w, and height h.
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._width = w
        self._height = h
        self._line0 = Line(self._x-self._width/2,self._y+self._height/2,self._x+self._width/2,self._y+self._height/2)
        self._line1 = Line(self._x-self._width/2,self._y-self._height/2,self._x+self._width/2,self._y-self._height/2)
        self._line2 = Line(self._x-self._width/2,self._y-self._height/2,self._x-self._width/2,self._y+self._height/2)
        self._line3 = Line(self._x+self._width/2,self._y-self._height/2,self._x+self._width/2,self._y+self._height/2)
        self._lines = [self._line0,self._line1,self._line2,self._line3]

    # Return the area of self.
    def area(self):
        return self._width * self._height

    # Return the perimeter of self.
    def perimeter(self):
        return self._width*2 + self._height*2

    # Return True if self intersects other, and False otherwise.
    # 判断两个长方形是否相交，等同于判断两个长方形是否至少存在一条边相交，而判断一条边相交
    def intersects(self, other):
        t = False
        for i in self._lines:
            for j in other._lines:
                if j.cross(i):
                    t = True
                    break
            if t == True:
                break
        return t

    # Return True if other is completely inside of self, and False
    # otherwise.
    # 不相交且四角都小于大矩形就是包含，当然依据题意，需要排除两个相同矩形的情况
    def contains(self, other):
        if not self.intersects(other):
            #由于都是平行于X轴和Y轴的长方形，简单判断:other.x-w >= self.x-w等等
            if other._x - other._width/2 >= self._x - self._width/2:
                if other._x + other._width/2 <= self._x + self._width/2:
                    if other._y - other._height/2 >= self._y - self._height/2:
                        if other._y + other._height/2 <= self._y + self._height/2:
                            return True
        elif self == other:
            return True
        return False

    # Draw self on stddraw.
    def draw(self):
        #stddraw.rectangle(x,y,w,h)，x,y为左下角坐标
        x = self._x-self._width/2
        y = self._y-self._height/2
        # stddraw.setXscale(self._x-self._width/2-1,self._x+self._width/2+1)
        # stddraw.setYscale(self._y-self._height/2-1,self._y+self._height/2+1)
        stddraw.rectangle(x,y,self._width,self._height)
        

def main():
    r = Rectangle(0,0,4,6)
    r1 = Rectangle(1,1,10,27)
    r2 = Rectangle(3,4,3,3)
    print(r2.intersects(r))
    print(r2.contains(r))
    print(r2.contains(r2))
    print(r1.contains(r))
    print(r1.contains(r2))
    print(r.contains(r1))
    #手工设置画布,否则要判断很多
    stddraw.setCanvasSize(1000,1000)
    stddraw.setXscale(-17,17)
    stddraw.setYscale(-17,17)
    r.draw()
    r1.draw()
    r2.draw()
    stddraw.show()

if __name__ == '__main__':
    main()

