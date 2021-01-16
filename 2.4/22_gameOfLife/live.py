#-----------------------------------------------------------------------
# live.py
#-----------------------------------------------------------------------

import stdio
import stdarray

#-----------------------------------------------------------------------

# isAlive is a matrix that represents the open sites of a system.
# toAlive is a partially completed matrix that represents the full sites
# of that system. Update toAlive by marking every site of that system
# that is open and reachable from site (i, j).
'''
def _living(isAlive, toAlive, i, j):
    n = len(toAlive)
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= n):
        return
    if not isAlive[i][j]:
        return
    if toAlive[i][j]:
        return
    toAlive[i][j] = True
    _living(isAlive, toAlive, i+1, j  )  # Down.
    _living(isAlive, toAlive, i  , j+1)  # Right.
    _living(isAlive, toAlive, i  , j-1)  # Left.
    _living(isAlive, toAlive, i-1, j  )  # Up.
'''
#-----------------------------------------------------------------------

# isAlive is a matrix that represents the open sites of a system.
# Compute and return a matrix that represents the full sites of
# that system.

def liveNeighbor(isAlive,i,j):
    n = len(isAlive)
    lN = 0
    #upper position
    if (i-1 >= 0):
        #upper left
        if (j-1 >= 0):
            if isAlive[i-1][j-1]:
                lN += 1
        #up
        if isAlive[i-1][j]:
            lN += 1
        #upper right
        if (j+1 < n):
            if isAlive[i-1][j+1]:
                lN += 1
    #lower position
    if (i+1 < n):
        #lower left
        if (j-1 >= 0):
            if isAlive[i+1][j-1]:
                lN += 1
        #down
        if isAlive[i+1][j]:
            lN += 1
        #lower right
        if (j+1 < n):
            if isAlive[i+1][j+1]:
                lN += 1
    #left
    if j-1 >=0:
        if isAlive[i][j-1]:
            lN += 1
    #right
    if j+1 < n:
        if isAlive[i][j+1]:
            lN += 1
            
    return lN

def aliveRule(isAlive,toAlive,i,j):
    lN = liveNeighbor(isAlive,i,j)
    if lN < 2 or lN > 3:
        toAlive[i][j] = False
    else:
        toAlive[i][j] = True
    return toAlive

def deadRule(isAlive,toAlive,i,j):
    lN = liveNeighbor(isAlive,i,j)
    if lN == 3:
        toAlive[i][j] = True
    else:
        toAlive[i][j] = False
    return toAlive

def living(isAlive):
    n = len(isAlive)
    toAlive = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            if isAlive[i][j]:
                aliveRule(isAlive,toAlive,i,j)
            else:
                deadRule(isAlive,toAlive,i,j)
    # for j in range(n):
    #     _living(isAlive, toAlive, 0, j)
    return toAlive

#-----------------------------------------------------------------------

# isAlive is matrix that represents the open sites of a system. Return
# True if that system percolates, and False otherwise.

def percolates(isAlive):
    
    # Compute the full sites of the system.
    toAlive = living(isAlive)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(toAlive)
    for j in range(n):
        if toAlive[n-1][j]:
            return True
    return False

#-----------------------------------------------------------------------

# Read from standard input a boolean matrix that represents the
# open sites of a system. Write to standard output a boolean
# matrix representing the full sites of the system. Then write
# True if the system percolates and False otherwise.

def main():
    isAlive = stdarray.readBool2D()
    stdarray.write2D(living(isAlive))
    stdio.writeln(percolates(isAlive))

    #isAlive = stdarray.readBool2D()
    #stdarray.write2D(living(isAlive))
    #draw(isAlive, False)
    #stddraw.setPenColor(stddraw.BLUE)
    #draw(living(isAlive), True)
    #stdio.writeln(percolates(isAlive))
    #stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python live.py < test5.txt 
# 5 5
# 0 1 1 0 1 
# 0 0 1 1 1 
# 0 0 0 1 1 
# 0 0 0 0 1 
# 0 1 1 1 1 
# True

# python live.py < test8.txt 
# 8 8
# 0 0 1 1 1 0 0 0 
# 0 0 0 1 1 1 1 1 
# 0 0 0 0 0 1 1 0 
# 0 0 0 0 0 1 1 1 
# 0 0 0 0 0 1 1 0 
# 0 0 0 0 0 0 1 1 
# 0 0 0 0 1 1 1 1 
# 0 0 0 0 0 1 0 0 
# True

