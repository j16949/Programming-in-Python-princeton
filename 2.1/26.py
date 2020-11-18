#-----------------------------------------------------------------------
# reference gauss.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean 0.0
# and standard deviation 1.0 at the given x value.

def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean mu
# and standard deviation sigma at the given x value.

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma

#-----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean 0.0 and standard deviation 1.0 at the given z value.

def Phi(z):
    if z < -8.0:
        return 0.0
    if z > 8.0:
        return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2
#        print('total:',total,' ','term:',term,' ',i)
    return 0.5 + phi(z) * total

#-----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean mu and standard deviation sigma at the given z value.

def cdf(z, mu=0.0, sigma=1.0):
    return Phi((z - mu) / sigma)


#-----------------------------------------------------------------------

#Return the inverse of cdf,give percentage,return score
#如果数据是正态分布（或近似正态），那么根据『经验法则（empirical rule），或者叫 68-95-99.7 法则（https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule）』可知，99.7%（几乎全部）的数据在均值左右3个标准差范围内，也就是可以用
#均值±3×标准差
#大致判断最大值和最小值。
#故此处最大值设为mu+3sigma,最小值为mu-3sigma
#正太分布平均值，中位数，众数为同一个数字

def cdfInverse(p,minz,maxz,mu=0.0,sigma=1.0):
    z = (maxz+minz)/2
    print('cdf:',cdf(z,mu,sigma))
    print('z:',z)
    if abs(cdf(z,mu,sigma)-p/100) < 0.001:
        return z
    elif cdf(z,mu,sigma) < p/100:
        return cdfInverse(p,z,maxz,mu,sigma)
    elif cdf(z,mu,sigma) > p/100:
        return cdfInverse(p,minz,z,mu,sigma)
    else:
        return False

#-----------------------------------------------------------------------

# Accept floats z, mu, and sigma as command-line arguments. Use them
# to test the cdf() and pdf() functions. Write the
# results to standard output.

#z = float(sys.argv[1])
# p = float(sys.argv[1])
# mu = float(sys.argv[2])
# sigma = float(sys.argv[3])


#stdio.writeln(cdf(z, mu, sigma))
#stdio.writeln(cdfInverse(p,mu,mu,sigma))
stdio.writeln(cdfInverse(98.93,1019-3*209,1019+3*209,1019,209))

#-----------------------------------------------------------------------

# python gauss.py 820 1019 209
# 0.17050966869132106

# python gauss.py 1500 1019 209
# 0.9893164837383885

# python gauss.py 1500 1025 231
# 0.9801220907365491

