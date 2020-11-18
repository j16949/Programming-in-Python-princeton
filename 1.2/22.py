import sys

 # Accept as command-line arguments a temperature t (in Fahrenheit)
 # and a wind speed v (in miles per hour). Compute the wind chill
 # w using the formula from the National Weather Service.
 # Write w to standard output.
 #
 #  Reference:  http://www.nws.noaa.gov/om/windchill/index.shtml

t = float(sys.argv[1])
v = float(sys.argv[2])

w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)

print(w)
