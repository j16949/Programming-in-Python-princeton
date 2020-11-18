#-----------------------------------------------------------------------
# coupon.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import sys
import random
import math

#----------------------------------------------------------------------
def binoDistr(k,n,p):
	return p**k*(1-p)**(n-k)*math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

#-----------------------------------------------------------------------

# Return a random coupon between 0 and n-1.

def getCoupon(n):
    return random.randrange(0, n)

#-----------------------------------------------------------------------

# binomail get coupon

def getCouponbyBino(n):
	x = random.random()
	s = 0
	j = 0
	p = 0.5
	while x >= s:
		s += binoDistr(j,n,p)
		j += 1
	print(x)
	return j-1

#-----------------------------------------------------------------------

# Collect coupons until getting one of each value in the range
# 0 to n-1.  Return the number of coupons collected.

def collect(n):
    found = stdarray.create1D(n+1, False)
    couponCount = 0
    distinctCouponCount = 0
    while distinctCouponCount < n:
        coupon = getCouponbyBino(n)
        couponCount += 1
        if not found[coupon] and coupon != 0:
            distinctCouponCount += 1
            found[coupon] = True
    return couponCount

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard
# output the number of coupons you collect before obtaining one of
# each of n types.

#n = int(sys.argv[1])
n = 10
couponCount = collect(n)
stdio.writeln(couponCount)

#-----------------------------------------------------------------------

# python coupon.py 1000
# 6456

# python coupon.py 1000
# 8815

# python coupon.py 1000000
# 16079795

