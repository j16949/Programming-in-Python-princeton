#-----------------------------------------------------------------------
# percplot.py
#-----------------------------------------------------------------------

import sys
import stddraw
import estimate
import math

#-----------------------------------------------------------------------

# Plot to standard draw a graph within the interval [x0, x1] from
# (x0, y0) to (x1, y1) that relates site vacancy probabilities to
# percolation probabilities.

def curve(n, x0, y0, x1, y1, trials=10000, gap=.01, err=.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = math.sin(xm)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    curve(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show(0.0)
    curve(n, xm, fxm, x1, y1)
    
#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Plot to standard draw
# a graph that relates site vacancy probability (control variable) to
# percolation probability (experimental observations) for a
# n-by-n system.

n = int(sys.argv[1])
stddraw.setPenRadius(0.0)
stddraw.setXscale(-2,5)
stddraw.setYscale(-2,5)
curve(n, 0.0, math.sin(0), math.pi, math.sin(math.pi))
stddraw.line(-2,0,5,0)
stddraw.line(0,-2,0,5)
stddraw.show()

#-----------------------------------------------------------------------

# python percplot.py 20

# python percplot.py 100
