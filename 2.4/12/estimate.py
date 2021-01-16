#-----------------------------------------------------------------------
# estimate.py
#-----------------------------------------------------------------------

import sys
import stdio
import percolation
import percolationio

#-----------------------------------------------------------------------

# Generate a random n-by-n system with site vacancy probability p
# and determine if the system percolates. Repeat t times. Return
# an estimate of the empirical percolation probability of such systems.

def evaluate(m, n, p, trials):
    count = 0
    for i in range(trials):
        # Generate one random network.
        isOpen = percolationio.random(m, n, p)
        if (percolation.percolates(isOpen)):
            count += 1
    return 1.0 * count / trials

#-----------------------------------------------------------------------

# Accept integer n, float p, and integer trials as command-line
# arguments. Create trials random n-by-n systems with site vacancy
# probability p. Determine the fraction of them that percolate, and
# write that fraction to standard output.

def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    p = float(sys.argv[3])
    trials = int(sys.argv[4])
    q = evaluate(m, n, p, trials)
    stdio.writeln(q)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python2.7 estimate.py 20 .55 100
# 0.25

# python2.7 estimate.py 20 .65 100
# 0.88

# python2.7 estimate.py 20 .65 100
# 0.89

# python2.7 estimate.py 40 .55 1000
# 0.094
