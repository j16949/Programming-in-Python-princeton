#表示经纬度
import math

class Location:
    
    #经纬度,x,y为弧度
    def __init__(self,x,y):
        self._x = x
        self._y = y

    #两点间的大圆距离
    def distanceTo(self,other):
        return 60 * math.degrees(math.acos(math.sin(self._x)*math.sin(other._x)+math.cos(self._x)*math.cos(other._x)*math.cos(self._y-other._y)))

def main():
    pairs = Location(math.radians(48.87),math.radians(-2.33))
    sanfan = Location(math.radians(37.8),math.radians(122.4))
    print(pairs.distanceTo(sanfan))

if __name__=='__main__':
    main()
