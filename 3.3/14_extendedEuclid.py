#-----------------------------------------------------------------------
#标准答案
#-----------------------------------------------------------------------
'''
def gcd(p, q):
    if q == 0: return (p, 1, 0)
    (d, a, b) = gcd(q, p % q)
    return (d, b, a - (p // q) * b)

print(gcd(169,121))
'''
#-----------------------------------------------------------------------
#可行答案之一

#-----------------------------------------------------------------------
#gcd,greatest common divisor
def gcd(p,q,x=0,y=0):
    if q == 0:
        x,y=1,0
        return p,x,y
    res,x,y = gcd(q,p%q,x,y)
    tmp = x
    x = y
    y = tmp - p//q*y
    return res,x,y

def main():
    print(gcd(169,121))

if __name__=='__main__':
    main()




#-----------------------------------------------------------------------
# below is wrong
'''
# euclid.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Return the greatest common divisor of p and q.

def gcd(p, q):
    if q == 0:
        return (d,a,b)
    return gcd(q, p % q)

#-----------------------------------------------------------------------

# Accept integers p and q as command-line arguments, compute the
# greatest common divisor of p and q, and write the result to
# standard output.

def main():
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    divisor = gcd(p, q)
    stdio.writeln(divisor)

if __name__ == '__main__':
    main()
  
#-----------------------------------------------------------------------

# python euclid.py 1440 408
# 24

# python euclid.py 314159 271828
# 1
'''
