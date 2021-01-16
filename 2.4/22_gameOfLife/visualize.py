#-----------------------------------------------------------------------
# visualize.py
#-----------------------------------------------------------------------

import sys
import stddraw
import live
import lifeio
import GosperGliderGun

#-----------------------------------------------------------------------

# Accept integer n, float p, and integer t as command-line arguments.
# Generate a n-by-n random system with site vacancy probability p.
# Compute the directed live living, and draw result to standard
# draw. Repeat t times.

def move(isAlive):
    alive = live.living(isAlive)
    lifeio.draw(alive, True)
    stddraw.show(50.0)
    return alive

def main():
    #n = int(sys.argv[1])
    #p = float(sys.argv[2])
    #trials = int(sys.argv[3])
    n = 50
    trials = 1
    moveStep = 999
    for i in range(trials):
        #isAlive = lifeio.random(n, p)

        #滑翔机
        isAlive = [[False] * 2*n for i in range(2*n)]
        isAlive[10][20] = True
        isAlive[11][21] = True
        isAlive[12][19] = True
        isAlive[12][20] = True
        isAlive[12][21] = True
        #isAlive[10][21] = True
        '''
        #高斯帕滑翔机枪
        isAlive = GosperGliderGun.gun
        '''
        stddraw.clear()
        stddraw.setPenColor(stddraw.BLACK)
        lifeio.draw(isAlive, True)
        stddraw.show(1000)
        for j in range(moveStep):
            stddraw.clear()
            alive = move(isAlive)
            isAlive = alive
        
    stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python visualize.py 20 .65 3

# python visualize.py 20 .60 1

# python visualize.py 20 .55 1

