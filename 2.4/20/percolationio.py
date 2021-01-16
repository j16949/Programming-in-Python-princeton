#-----------------------------------------------------------------------
# percolationio.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
import stdrandom
import math

#-----------------------------------------------------------------------

# Return a random n-by-n matrix, each entry True with probability p.

def random(n, p):
    a = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    #方格的横线比竖线少一
    for i in range(0,n,2):
        for j in range(int((n-1)/2),n):
            a[i][j] = False
    return a

#-----------------------------------------------------------------------

# Draw system a to standard draw. Parameter which indicates whether
# to display the entries corresponding to True or to False.

def draw(a, which):
    n = len(a[0])
    stddraw.setXscale(-.5*n, n + .5)
    stddraw.setYscale(-.5*n, n + .5)
    for i in range(n):
        for j in range(n):
            if a[i][j] == which:
                if i % 2 == 0:
                    stddraw.line(j-.5*i/2,n-i/2*(1*math.sin(math.pi/3))-1,j-.5*i/2+.98,n-i/2*(1*math.sin(math.pi/3))-1)
                else:
                    if j % 2 == 0:
                        jt = j/2-(i-1)/2*.5
                        stddraw.line(jt,n-(i-1)/2*(1*math.sin(math.pi/3))-1,jt-.5,n-(i+1)/2*(1*math.sin(math.pi/3))-1)
                    else:
                        jt = (j+1)/2-(i-1)/2*.5
                        stddraw.line(jt-1,n-(i-1)/2*(1*math.sin(math.pi/3))-1,jt+.5-1,n-(i+1)/2*(1*math.sin(math.pi/3))-1)
                #stddraw.show(100)

#-----------------------------------------------------------------------

# For testing.

def main():
    # n = int(sys.argv[1])
    # p = float(sys.argv[2])
    n = 4
    n = 2*n + 1
    p = .5
    test = random(n, p)
    draw(test, True)
    stddraw.show()
    
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python percolationio.py 10 0.8

