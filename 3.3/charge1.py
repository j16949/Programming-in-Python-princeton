#-----------------------------------------------------------------------
# charge.py
#-----------------------------------------------------------------------

import sys
import math
import stdio

#-----------------------------------------------------------------------

class Charge:

    # Construct self centered at (x, y) with charge q.
    def __init__(self, x0, y0, q0):
        self._rx = x0  # x value of the query point
        self._ry = y0  # y value of the query point
        self._q = q0   # Charge

    # Return the potential of self at (x, y).
    def potentialAt(self, x, y):
        COULOMB = 8.99e09
        dx = x - self._rx
        dy = y - self._ry
        r = math.sqrt(dx*dx + dy*dy)
        if r == 0.0: # Avoid division by 0
            if self._q >= 0.0:
                return float('inf')
            else:
                return float('-inf')
        return COULOMB * self._q / r

    # Return a string representation of self.
    def __str__(self):
        result = str(self._q) + ' at ('
        result += str(self._rx) + ', ' + str(self._ry) + ')'
        return result
    '''   
    def __eq__(self, other):
        if self._rx != other._rx: return False
        if self._ry != other._ry: return False
        if self._q  != other._q:  return False
        return True
    #test
    '''
    '''
    def __ne__(self,other):
        return (self is not other)
        '''
    def __hash__(self):
        a = (self._rx,self._ry,self._q)
        return hash(a)
#-----------------------------------------------------------------------

# For testing.
# Accept floats x and y as command-line arguments. Create a Charge
# objects with fixed position and electrical charge, and write to
# standard output the potential at (x, y) due to the charge.

def main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    c = Charge(.51, .63, 21.3)
    c1 = Charge(.51, .63, 21.3)
    d = Charge(.52, .63, 21.3)
    stdio.writeln(c)
    stdio.writeln(c.potentialAt(x, y))
    print(hash(c))
    print(c==d)
    print(c is c1)
    print(c==c1)
    print(hash(c)==hash(c1))

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python charge.py .5 .5
# 21.3 at (0.51, 0.63)
# 1468638248194.164

