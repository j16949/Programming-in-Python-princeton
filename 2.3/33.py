#-----------------------------------------------------------------------
# brownianisland.py
#-----------------------------------------------------------------------

import sys
import math
import stddraw
import stdrandom

#-----------------------------------------------------------------------

# Draw a Brownian bridge from (x0, y0) to (x1, y1) with the given
# variance and scaleFactor.

def curve(x0, y0, x1, y1, variance, scaleFactor,n=11):
    if n == 0:
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    delta = stdrandom.gaussian(0, math.sqrt(variance))
    delta1 = stdrandom.gaussian(0, math.sqrt(variance))
    xm = (x0 + x1) / 2.0+delta
    ym = (y0 + y1) / 2.0+delta1
    curve(x0, y0, xm, ym, variance/scaleFactor, scaleFactor,n-1)
    curve(xm, ym, x1, y1, variance/scaleFactor, scaleFactor,n-1)

#-----------------------------------------------------------------------

# Accept a Hurst exponent as a command-line argument.
# Use the Hurst exponent to compute a scale factor.
# Draw a Brownian bridge from (0, .5) to (1.0, .5) with
# variance .01 and that scale factor.

def main():
    hurstExponent = float(sys.argv[1])
    stddraw.setPenRadius(0.0)
    stddraw.clear(stddraw.LIGHT_GRAY)
    scaleFactor = 2 ** (2.0 * hurstExponent)
    curve(.5, .5, .5, .5, .01, scaleFactor)
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python brownian.py 1

# python brownian.py .5

# python brownian.py .05
