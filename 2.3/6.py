#-----------------------------------------------------------------------
# gcd(gcd,gcd)等于求4个数的最大公约数
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Return the greatest common divisor of p and q.

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

#-----------------------------------------------------------------------

# Accept integers p and q as command-line arguments, compute the
# greatest common divisor of p and q, and write the result to
# standard output.

def main():
    p = 4 
    q = 10
    a = 12
    b = 8
    divisor = gcd(gcd(p, q),gcd(a,b))
    stdio.writeln(divisor)

if __name__ == '__main__':
    main()
  
#-----------------------------------------------------------------------

# python euclid.py 1440 408
# 24

# python euclid.py 314159 271828
# 1
