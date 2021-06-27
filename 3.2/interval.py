
class Interval:
    
    def __init__(self,left,right):
        self._l = left
        self._r = right

    def contains(self,other):
        if self._r >= other._r >= other._l >= self._l:
            return True
        return False
    
    def intersects(self,other):
        if other._r > self._r >= other._l:
            return True
        elif other._r >= self._l > other._r:
            return True
        elif self.contains(other):
            return True
        return False

def main():
    i1 = Interval(0,5)
    i2 = Interval(6,10)
    print(i2.contains(i1))
    print(i1.intersects(i2))

if __name__ == '__main__':
    main()
