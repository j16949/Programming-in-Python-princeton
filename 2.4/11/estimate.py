#-----------------------------------------------------------------------
# estimate.py
#-----------------------------------------------------------------------

import sys
import stdio
import percolation
import math
import stdarray
import stddraw
import stdrandom
import stdstats
import gaussian
import percolationio

#-----------------------------------------------------------------------

# Generate a random n-by-n system with site vacancy probability p
# and determine if the system percolates. Repeat t times. Return
# an estimate of the empirical percolation probability of such systems.

def evaluate(n, p, trials):
    count = 0
    for i in range(trials):
        # Generate one random network.
        isOpen = percolationio.random(n, p)
        if (percolation.percolates(isOpen)):
            count += 1
    return count

def exTimes(n,p,trials,t):
    freq = [0 for i in range(trials)]
    for i in range(t):
        heads = evaluate(n,p,trials)
        freq[heads] += 1
    norm = [0 for i in range(trials)]
    for i in range(trials):
        norm[i] = 1.0*freq[i]/t
    return norm

#-----------------------------------------------------------------------

# Accept integer n, float p, and integer trials as command-line
# arguments. Create trials random n-by-n systems with site vacancy
# probability p. Determine the fraction of them that percolate, and
# write that fraction to standard output.

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    t = int(sys.argv[4])
    q = evaluate(n, p, trials)
    stdio.writeln(q)

    norm = exTimes(n,p,trials,t)
    phi = stdarray.create1D(n+1, 0.0)
    stddev = math.sqrt(n)/2.0
    for i in range(n+1):
        phi[i] = gaussian.pdf(i, n/2.0, stddev)

    stddraw.setCanvasSize(1000, 400)
    stddraw.setYscale(0, 1.1 * max(max(norm), max(phi)))
    stdstats.plotBars(norm)
    stdstats.plotLines(phi)
    stddraw.show()


if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------
# python3 estimate.py 20 .59 30 100
