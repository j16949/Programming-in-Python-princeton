import euclid

class Rational:

    def __init__(self,x,y):
        divisor = euclid.gcd(x,y)
        self._x = x/divisor
        if y != 0:
            self._y = y/divisor
        else:
            #raise ValueException('被除数不能为0')
            raise Exception("ValueException:'被除数不能为0'")

    def __add__(self,b):
        return self._x/self._y + b

    def __sub__(self,b):
        return self._x/self._y - b

    def __mul__(self,b):
        return self._x/self._y * b

    def __abs__(self):
        return abs(self._x/self._y)

    def __str__(self):
        return str(int(self._x))+'/'+str(int(self._y))

def main():
    r = Rational(-2,0)
    print(r)
    print(r+1)
    print(r-1)
    print(r*2)
    print(abs(r))
    
if __name__ == '__main__':
    main()
