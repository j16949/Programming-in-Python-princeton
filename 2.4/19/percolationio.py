#-----------------------------------------------------------------------
# percolationio.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
import stdrandom

#-----------------------------------------------------------------------

# Return a random n-by-n matrix, each entry True with probability p.

def random(n, p):
    a = stdarray.create2D(2*n-1, n, False)
    for i in range(2*n-1):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    #方格的横线比竖线少一
    for i in range(0,2*n-1,2):
        a[i][-1] = False
    return a

#-----------------------------------------------------------------------

# Draw system a to standard draw. Parameter which indicates whether
# to display the entries corresponding to True or to False.

def draw(a, which):
    n = len(a[0])
    stddraw.setXscale(-.5, n + .5)
    stddraw.setYscale(-.5, n + .5)
    for i in range(2*n-1):
        for j in range(n):
            if a[i][j] == which:
                if i % 2 == 0:
                    stddraw.line(j,n-i/2-1,j+.98,n-i/2-1)
                else:
                    stddraw.line(j,n-(i+1)/2,j,n-(i+1)/2-.98)
                #stddraw.show(100)

#-----------------------------------------------------------------------

# For testing.

def main():
    # n = int(sys.argv[1])
    # p = float(sys.argv[2])
    n = 6
    p = 1
    test = random(n, p)
    draw(test, True)
    stddraw.show()
    
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python percolationio.py 10 0.8

