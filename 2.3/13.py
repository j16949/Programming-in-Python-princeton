#-----------------------------------------------------------------------
# euclid.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Return the greatest common divisor of p and q.

s = 0

def gcd(p, q):
    global s
    s += 1
    if q == 0:
        return p
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
    print('递归次数为:{}'.format(s))

if __name__ == '__main__':
    main()
  
#-----------------------------------------------------------------------

# python euclid.py 1440 408
# 24

# python euclid.py 314159 271828
# 1
