#-----------------------------------------------------------------------
# percolationio.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
import stdrandom

#-----------------------------------------------------------------------

# Return a random n-by-n matrix, each entry True with probability p.

def random(m, n, p):
    a = stdarray.create2D(m, n, False)
    for i in range(m):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    return a

#-----------------------------------------------------------------------

# Draw system a to standard draw. Parameter which indicates whether
# to display the entries corresponding to True or to False.

def draw(a, which):
    #print(a)
    m = len(a)
    n = len(a[0])
    scale_length = max(m,n)
    stddraw.setXscale(-.5, scale_length)
    stddraw.setYscale(-.5, scale_length)
    for i in range(m):
        for j in range(n):
            if a[i][j] == which:
                stddraw.filledSquare(j, m-i-1, .49)

#-----------------------------------------------------------------------

# For testing.

def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    p = float(sys.argv[3])
    test = random(m, n, p)
    draw(test, False)
    stddraw.show()
    
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python percolationio.py 10 0.8

