#-----------------------------------------------------------------------
# complex.py
#-----------------------------------------------------------------------

import stdio
import math

# A Complex object is a complex number.

# A Complex object is immutable.  So once you create and initialize
# a Complex object, you cannot change it.

class Complex:

    # Construct self with real part real and imaginary
    # part imag. real defaults to 0.0. imag also defaults to 0.0.
    def __init__(self, re=0.0, im=0.0):
        self._re = re
        self._im = im

    # Return the real part of self.
    def re(self):
        return self._re

    # Return the imaginary part of self.
    def im(self):
        return self._im

    # Return the conjugate of self.
    def conjugate(self):
        return Complex(self._re, -self._im)

    # Return a new Complex object which is the sum of self and 
    # Complex object other.
    def __add__(self, other):
        re = self._re + other._re
        im = self._im + other._im
        return Complex(re, im)
    
    def __sub__(self,other):
        re = self._re - other._re
        im = self._im - other._im
        return Complex(re, im)

    # Return a new Complex object which is the product of self and
    # Complex object other.
    def __mul__(self, other):
        re = self._re * other._re - self._im * other._im
        im = self._re * other._im + self._im * other._re
        return Complex(re, im)
        
    #除法,分母分子同时乘以分母的共轭，返回一个复数
    def __truediv__(self,other):
        con = other.conjugate()     #分母的共轭
        t = (other*con).re()      #分母乘以自己的共轭的实部
        d = self*con                #分子复数
        re = d.re()/t
        im = d.im()/t
        return Complex(re,im)
        
    # Return True if self and Complex object other are equal, and
    # False otherwise.
    def __eq__(self, other):
        return (self._re == other._re) and (self._im == other._im)

    # Return True if self and Complex object other are unequal, and
    # False otherwise.
    def __ne__(self, other):
        return not self.__eq__(other)

    # Return the absolute value of self.
    def __abs__(self):
        return math.sqrt(self._re*self._re + self._im*self._im)
        # Alternative: return math.hypot(self._re, self._im)
        # Alternative: return self.__mul__(self.conjugate())

    # Return a string representation of self.
    def __str__(self):
        re = self._re
        im = abs(self._im)
        if self._im >= 0:
            zhengfu = '+'
        else:
            zhengfu = '-'
        if self._im % 1 == 0:
            im = int(im)
        if self._re % 1 == 0:
            re = int(re)
        if im == 0:
            return str(re)
        if re == 0:
            return str(im) + 'i'
        if im == 1:
            im = ''
        return str(re) + zhengfu + str(im) + 'i'
    
    # 返回相位角，即x轴为实部，y轴为虚部
    def theta(self):
        if self._re == 0:
            if self._im < 0:
                return -90
            else:
                return 90
        return math.degrees(math.atan(self._im/self._re))
    
    #返回复数的次方
    def __pow__(self,n):
        p = self
        for i in range(n-1):
            p *= self
        return p
#-----------------------------------------------------------------------

# For testing.
# Create and use some Complex objects.

def main():

    z0 = Complex(1.0, 1.0)
    z = z0
    z = z * z + z0
    z = z * z + z0
    stdio.writeln(z)
    z1 = Complex(-3,-1)
    z2 = Complex(3,0)
    z3 = Complex(0,3)
    # print(z1.theta())
    # print(z2.theta())
    # print(z3.theta())
    # print(z1**2)
    # print(z2**3)
    print(z3**2)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python complex.py 
# -7.0 + 7.0i

