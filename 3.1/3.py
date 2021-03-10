#-----------------------------------------------------------------------
# alberssquares.py
#-----------------------------------------------------------------------

import sys
import stddraw
from color import Color
from itertools import permutations

#-----------------------------------------------------------------------

# Accept integers r1, g1, b1, r2, g2, and b2 as command-line arguments.
# Draw to standard draw Albers squares using colors (r1, g1, b1) and
# (r2, g2, b2).

'''
r1 = int(sys.argv[1])
g1 = int(sys.argv[2])
b1 = int(sys.argv[3])
c1 = Color(r1, g1, b1)

r2 = int(sys.argv[4])
g2 = int(sys.argv[5])
b2 = int(sys.argv[6])
c2 = Color(r2, g2, b2)

r3 = int(sys.argv[7])
g3 = int(sys.argv[8])
b3 = int(sys.argv[9])
c3 = Color(r3, g3, b3)
'''

c1 = Color(255,0,0)
c2 = Color(0,255,0)
c3 = Color(0,0,255)
cs = [c1,c2,c3]
#stddraw.setCanvasSize(512, 256)
#stddraw.setYscale(.25*2, .75*2)
stddraw.setYscale(-1,7)
stddraw.setXscale(-4,27*2)

'''
stddraw.setPenColor(c1)
stddraw.filledSquare(.25, .5, .3)

stddraw.setPenColor(c2)
stddraw.filledSquare(.25, .5, .2)

stddraw.setPenColor(c3)
stddraw.filledSquare(.25, .5, .1)
'''
f = list(permutations('012',3))

for i in range(6):
    stddraw.setPenColor(cs[eval(f[i][0])])
    stddraw.filledSquare(i*3*2+i, 3, 3)
    stddraw.setPenColor(cs[eval(f[i][1])])
    stddraw.filledSquare(i*3*2+i, 3, 2)
    stddraw.setPenColor(cs[eval(f[i][2])])
    stddraw.filledSquare(i*3*2+i, 3, 1)
stddraw.show()

#-----------------------------------------------------------------------

# python alberssquares.py 9 90 166 100 100 100
    
# python alberssquares.py 0 174 239 147 149 252

