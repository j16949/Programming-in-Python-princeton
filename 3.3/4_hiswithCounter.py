#-----------------------------------------------------------------------
# histogram.py counter.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
import stdrandom
import stdstats
from counter import Counter

#-----------------------------------------------------------------------

class Histogram:

    # Construct self such that it can store n frequency counts.
    # stdarray.create1D是浅拷贝，不能用
    def __init__(self, n, trial):
        # Frequency counts.
        self._freqCounts = list()
        self._n = n
        for i in range(n):
            self._freqCounts.append(Counter(str(i),trial))

    # Add one occurrence of the value i to self.
    def addDataPoint(self, i):
        self._freqCounts[i].increment()

    # Draw self.
    def draw(self):
        counts = []
        for i in range(self._n):
            #print(self._freqCounts[i]._count)
            counts.append(self._freqCounts[i]._count)
        stddraw.setYscale(0, max(counts))
        stdstats.plotBars(counts)
    
    def count(self):
        for i in range(self._n):
            print(self._freqCounts[i]._count)
#-----------------------------------------------------------------------

# Accept integer n, float p, and integer trialCount as command-line
# arguments. Perform trialCount experiments, each of which counts the
# number of heads found when a biased coin (heads with probability p
# and tails with probability 1 - p) is flipped n times. Then, draw
# the results to standard draw.

def main():
    # n = int(sys.argv[1])  # number of biased coin flips per trial
    # p = float(sys.argv[2])  # heads with probability p
    # trialCount = int(sys.argv[3])  # number of trials
    n = 5
    p =.5
    trialCount = 1000
    histogram = Histogram(n + 1,trialCount)
    for trial in range(trialCount):
        heads = stdrandom.binomial(n, p)
        histogram.addDataPoint(heads)
    
    histogram.count()
    histogram._freqCounts[1]._count-=2
    histogram.count()
    stddraw.setCanvasSize(500, 200)
    stddraw.clear(stddraw.LIGHT_GRAY)
    histogram.draw()
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python histogram.py 50 .5 1000000
