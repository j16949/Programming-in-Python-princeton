#-----------------------------------------------------------------------
# percplot.py
# 红色函数图像整体比黑色偏右，可见定向渗透要达到相同的渗透概率需要的网格空置率更高
#-----------------------------------------------------------------------

import sys
import stddraw
import estimate
import estimated

#-----------------------------------------------------------------------

# Plot to standard draw a graph within the interval [x0, x1] from
# (x0, y0) to (x1, y1) that relates site vacancy probabilities to
# percolation probabilities.
# 正常全向渗透，用黑色表示

def curve(n, x0, y0, x1, y1, trials=10000, gap=.1, err=.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimate.evaluate(n, xm, trials)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    curve(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show(0.0)
    curve(n, xm, fxm, x1, y1)
    
#-----------------------------------------------------------------------
# 定向渗透，用红色表示
def curved(n, x0, y0, x1, y1, trials=10000, gap=.1, err=.0025):
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimated.evaluate(n, xm, trials)
    stddraw.setPenColor(stddraw.RED)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
    curved(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, .005)
    stddraw.show(0.0)
    curved(n, xm, fxm, x1, y1)
 
# Accept integer n as a command-line argument. Plot to standard draw
# a graph that relates site vacancy probability (control variable) to
# percolation probability (experimental observations) for a
# n-by-n system.

n = int(sys.argv[1])
stddraw.setPenRadius(0.0)
curve(n, 0.0, 0.0, 1.0, 1.0)
curved(n, 0.0, 0.0, 1.0, 1.0)
stddraw.show()

#-----------------------------------------------------------------------

# python percplot.py 20

# python percplot.py 100
