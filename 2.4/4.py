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
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    for i in range(trials):
        j = 0
        while j < 1:
            isOpen = percolationio.random(n, j)
            stddraw.clear()
            stddraw.setPenColor(stddraw.BLACK)
            percolationio.draw(isOpen, False)
            stddraw.setPenColor(stddraw.BLUE)
            full = percolation.flow(isOpen)
            percolationio.draw(full, True)
            stddraw.show(1000.0)
            j += p
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python visualize.py 20 .65 3

# python visualize.py 20 .60 1

# python visualize.py 20 .55 1

