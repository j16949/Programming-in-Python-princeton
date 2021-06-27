import stddraw

class Rectangle:

    # Construct self with center (x, y), width w, and height h.
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._width = w;
        self._height = h;

    # Return the area of self.
    def area(self):
        return self._width * self._height

    # Return the perimeter of self.
    def perimeter(self):
        return self._width*2 + self._height*2

    # Return True if self intersects other, and False otherwise.
    def intersects(self, other):
        pass

    # Return True if other is completely inside of self, and False
    # otherwise.
    def contains(self, other):
        pass

    # Draw self on stddraw.
    def draw(self):
        #stddraw.rectangle(x,y,w,h)，x,y为左下角坐标
        x = self._x-self._width/2
        y = self._y-self._height/2
        stddraw.rectangle(x,y,self._width,self._height)
        stddraw.show()

def main():
    r = Rectangle(0,0,.4,.5)
    r.draw()

if __name__ == '__main__':
    main()

