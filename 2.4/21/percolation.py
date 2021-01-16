#-----------------------------------------------------------------------
# percolation.py
#-----------------------------------------------------------------------

import stdio
import stdarray

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# isFull is a partially completed matrix that represents the full sites
# of that system. Update isFull by marking every site of that system
# that is open and reachable from site (i, j).

def _flow(isOpen, isFull, i, j, k):
    n = len(isFull)
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= n):
        return
    if (k < 0) or (k >= n):
        return
    if not isOpen[i][j][k]:
        return
    if isFull[i][j][k]:
        return
    isFull[i][j][k] = True
    _flow(isOpen, isFull, i+1, j  ,k)  # Down.
    _flow(isOpen, isFull, i  , j+1,k)  # Right.
    _flow(isOpen, isFull, i  , j-1,k)  # Left.
    _flow(isOpen, isFull, i  , j  ,k+1)  # Forward.
    _flow(isOpen, isFull, i  , j  ,k-1)  # Backward.
    _flow(isOpen, isFull, i-1, j  ,k)  # Up.

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# Compute and return a matrix that represents the full sites of
# that system.

def flow(isOpen):
    n = len(isOpen)
    isFull = [[[False for k in range(n)] for col in range(n)] for row in range(n)]
    for j in range(n):
        for k in range(n):
            _flow(isOpen, isFull, 0, j,k)
    return isFull

#-----------------------------------------------------------------------

# isOpen is matrix that represents the open sites of a system. Return
# True if that system percolates, and False otherwise.

def percolates(isOpen):
    
    # Compute the full sites of the system.
    isFull = flow(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(isFull)
    for j in range(n):
        for k in range(n):
            if isFull[n-1][j][k]:
                return True
    return False

#-----------------------------------------------------------------------

# Read from standard input a boolean matrix that represents the
# open sites of a system. Write to standard output a boolean
# matrix representing the full sites of the system. Then write
# True if the system percolates and False otherwise.

def main():
    isOpen = stdarray.readBool2D()
    stdarray.write2D(flow(isOpen))
    stdio.writeln(percolates(isOpen))

    #isOpen = stdarray.readBool2D()
    #stdarray.write2D(flow(isOpen))
    #draw(isOpen, False)
    #stddraw.setPenColor(stddraw.BLUE)
    #draw(flow(isOpen), True)
    #stdio.writeln(percolates(isOpen))
    #stddraw.show()

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python percolation.py < test5.txt 
# 5 5
# 0 1 1 0 1 
# 0 0 1 1 1 
# 0 0 0 1 1 
# 0 0 0 0 1 
# 0 1 1 1 1 
# True

# python percolation.py < test8.txt 
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

