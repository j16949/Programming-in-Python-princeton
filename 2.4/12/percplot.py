#-----------------------------------------------------------------------
# percplot.py
#-----------------------------------------------------------------------

import sys
import stddraw
import estimate

#-----------------------------------------------------------------------

# Plot to standard draw a graph within the interval [x0, x1] from
# (x0, y0) to (x1, y1) that relates site vacancy probabilities to
# percolation probabilities.

def curve(m, n, x0, y0, x1, y1, trials=1000, gap=.1, err=.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimate.evaluate(m, n, xm, trials)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    curve(m, n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show(0.0)
    curve(m, n, xm, fxm, x1, y1)
    
#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Plot to standard draw
# a graph that relates site vacancy probability (control variable) to
# percolation probability (experimental observations) for a
# n-by-n system.

m = int(sys.argv[1])
n = int(sys.argv[2])
stddraw.setPenRadius(0.0)
curve(m, n, 0.0, 0.0, 1.0, 1.0)
stddraw.show()

#-----------------------------------------------------------------------

# python percplot.py 20

# python percplot.py 100
