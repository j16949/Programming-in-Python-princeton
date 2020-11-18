import math
import sys

def binoDistr(k,n,p):
	return p**k*(1-p)**(n-k)*math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def totalbin(n,p):
	k = 0
	total = 0 
	for k in range(n+1):
		total += binoDistr(k,n,p)
	return total
	
#----------------------------------------------------------------------

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

#二项分布正态近似值

def binomialcdf(k,n,p):
    return cdf(k+0.5,n*p,math.sqrt(n*p*(1-p)))-cdf(k-0.5,n*p,math.sqrt(n*p*(1-p)))

k=eval(sys.argv[1])
n=eval(sys.argv[2])
p=eval(sys.argv[3])
print(binoDistr(k,n,p))
print(totalbin(n,p))
print(binomialcdf(k,n,p))
