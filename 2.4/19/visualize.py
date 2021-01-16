#-----------------------------------------------------------------------
# visualize.py
#-----------------------------------------------------------------------

import sys
import stddraw
import percolation
import percolationio

#-----------------------------------------------------------------------

# Accept integer n, float p, and integer t as command-line arguments.
# Generate a n-by-n random system with site vacancy probability p.
# Compute the directed percolation flow, and draw result to standard
# draw. Repeat t times.

def main():
    # n = int(sys.argv[1])
    # p = float(sys.argv[2])
    # trials = int(sys.argv[3])
    n = 20
    p = .5
    trials = 5
    for i in range(trials):
        isOpen = percolationio.random(n, p)
        stddraw.clear()
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setPenRadius(0.005)
        percolationio.draw(isOpen, True)
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.setPenRadius(0.05)
        full = percolation.flow(isOpen)
        percolationio.draw(full, True)
        stddraw.show(1000.0)
    #print('over')
    stddraw.show()
    

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python visualize.py 20 .65 3

# python visualize.py 20 .60 1

# python visualize.py 20 .55 1

