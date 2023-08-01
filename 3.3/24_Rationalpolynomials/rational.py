import euclid

class Rational:

    def __init__(self,x,y):
        divisor = euclid.gcd(x,y)
        self._x = x/divisor
        if y != 0:
            self._y = y/divisor
        else:
            print('被除数不能为0')

    def __add__(self,b):
        return self._x/self._y + b

    def __sub__(self,b):
        return self._x/self._y - b

    def __mul__(self,b):
        return self._x/self._y * b

    def __abs__(self):
        return abs(self._x/self._y)

    def __str__(self):
        if self._x == 0:
            return '0'
        return str(int(self._x))+'/'+str(int(self._y))

    #为了配合format
    def __format__(self,specification):
        if self._x/self._y <=0:
            return self.__str__()
        return '+'+self.__str__()

def main():
    r = Rational(-2,6)
    print(r)
    print(r+1)
    print(r-1)
    print(r*2)
    print(abs(r))
    print(format(r,"%s"))
    
if __name__ == '__main__':
    main()
