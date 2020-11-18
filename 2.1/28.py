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
def bsov(s,x,r,sigma,t):
	a = (math.log(s/x)+(r+sigma**2/2)*t)/(sigma*t**(1/2))
	b = a-sigma*t**(1/2)
	return s*cdf(a,0,sigma)-x*math.exp(-r*t)*cdf(b,0,sigma)


#-----------------------------------------------------------------------
def imVol(s,x,r,t,y):
	low = 0
	high = 1
	z = (high+low)/2
	while abs(bsov(s,x,r,z,t)-y) > 0.0001:
		temp = bsov(s,x,r,z,t)
		if temp>y:
			high = z
		elif temp<y:
			low = z
		z = (high + low)/2
	return z


#print(bsov(s,x,r,sigma,t))
print(bsov(23.75,15.00,0.01,0.35,0.5))
print(bsov(30.14,15.0,0.01,0.332,0.25))
print(bsov(23.75,15.00,0.01,0.1,0.5))
print(bsov(23.75,15.00,0.01,0.6,0.5))


print(imVol(30.14,15.0,0.01,0.25,15.177462481558178))
print(imVol(23.75,15.00,0.01,0.5,9.529766259063438))
print(imVol(23.75,15.00,0.01,0.5,8.824812812109766))


