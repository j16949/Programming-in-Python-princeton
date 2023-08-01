#-----------------------------------------------------------------------
# vector2D.py
#-----------------------------------------------------------------------

import math
import stdio
import stdarray
from complex import Complex

#-----------------------------------------------------------------------

class Vector2DComplex:

    # Construct a new Vector2DComplex object with numeric Cartesian coordinates
    # given in array a.
    def __init__(self,c):
        # Make a defensive copy to ensure immutability.
        self._x = c.re()  #
        self._y = c.im()  #

    # Return the ith Cartesian coordinate of self.
    def __getitem__(self, i):
        if i == 0:
            return self._x
        elif i ==1:
            return self._y
        else:
            raise Exception('index out of range')

    # Return the sum of self and Vector2DComplex object other.
    def __add__(self, other):
        return Vector2DComplex(Complex(self._x+other._x,self._y+other._y))

    # Return the difference of self and Vector2DComplex object other.
    def __sub__(self, other):
        return Vector2DComplex(Complex(self._x-other._x,self._y-other._y))

    # Return the product of self and numeric object alpha.
    def scale(self, alpha):
        return Vector2DComplex(Complex(alpha*self._x,alpha*self._y))

    # Return the inner product of self and Vector2DComplex object other.
    def dot(self, other):
        result = 0
        result += self._x * other._x
        result += self._y * other._y
        return result

    # Return the magnitude, that is, the Euclidean norm, of self.
    def __abs__(self):
        return math.sqrt(self.dot(self))

    # Return the unit vector of self.
    def direction(self):
        return self.scale(1.0 / abs(self))

    # Return a string representation of self.
    def __str__(self):
        return str((self._x,self._y))
        
    # Return the dimension of self.
    def __len__(self):
        return 2
        
#-----------------------------------------------------------------------

# For testing.
# Create and use some Vector2DComplex objects.

def main():

    a = Complex(1.0,2.0)
    b = Complex(5,2)
    x = Vector2DComplex(a)
    y = Vector2DComplex(b)

    stdio.writeln('x        = ' + str(x))
    stdio.writeln('y        = ' + str(y))
    stdio.writeln('x + y    = ' + str(x + y))
    stdio.writeln('x - y  = ' + str(x - y))
    stdio.writeln('10x      = ' + str(x.scale(10.0)))
    stdio.writeln('|x|      = ' + str(abs(x)))
    stdio.writeln('<x, y>   = ' + str(x.dot(y)))
    stdio.writeln('|x - y|  = ' + str(abs(x - y)))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------
'''
bai@ubuntu:~/pythonProject/princeton/3.3$ python3 vector2D.py 
x        = (1.0, 2.0)
y        = (5, 2)
x + y    = (6.0, 4.0)
x - y  = (-4.0, 0.0)
10x      = (10.0, 20.0)
|x|      = 2.23606797749979
<x, y>   = 9.0
|x - y|  = 4.0
'''
