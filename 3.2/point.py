import math

class Point:
    
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def distanceTo(self,b):
        return math.sqrt((self._x - b._x)**2 + (self._y - b._y)**2)

    def __str__(self):
        return '('+str(self._x)+','+str(self._y)+')'

def main():
    p1 = Point(0,0)
    p2 = Point(4,3)
    print(p1)
    print(p1.distanceTo(p2))

if __name__ == '__main__':
    main()
