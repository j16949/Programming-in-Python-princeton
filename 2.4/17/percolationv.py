#-----------------------------------------------------------------------
# percolationv.py
#-----------------------------------------------------------------------

import stdarray
import stdio
import stddraw
import percolationio

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system. 
# Compute and return a matrix that represents the full sites of
# that system. For now, consider only vertical percolation.

def horizontal(isOpen,isFull,i):
    n = len(isOpen)

    def leftRight(isOpen,isFull,i,j):
        t = j
        #向左一直找空的
        while 1 <= t and isOpen[i][t-1]:
            isFull[i][t-1] = True
            t -= 1
            percolationio.draw(isFull, True)
            stddraw.show(50.0)
        t = j
        #向右一直找空的
        while t < n-1 and isOpen[i][t+1]:
            isFull[i][t+1] = True
            t += 1
            percolationio.draw(isFull, True)
            stddraw.show(50.0)
        return isFull

    subisFull = []
    for j in range(n):
        if isFull[i][j]:
            subisFull.append([i,j])

    for x in subisFull:
        i,j = x
        isFull = leftRight(isOpen,isFull,i,j)

    return isFull
    
def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n, n, False)
    stddraw.setPenColor(stddraw.BLUE)
    for j in range(n):
        isFull[0][j] = isOpen[0][j]
        percolationio.draw(isFull, True)
        stddraw.show(50.0)
    for i in range(1, n):
        for j in range(n):
            if isOpen[i][j] and isFull[i-1][j]:
                isFull[i][j] = True
                percolationio.draw(isFull, True)
                stddraw.show(50.0)
        # for j in range(n):
        #     if isOpen[i][j]:
        #         if 1 <= j and j < n-1:
        #             if isFull[i][j-1] or isFull[i][j+1]:
        #                 isFull[i][j] = True
        #                 percolationio.draw(isFull, True)
        #                 stddraw.show(50.0)
        isFull = horizontal(isOpen,isFull,i)
    return isFull

#-----------------------------------------------------------------------

# open is matrix that represents the open sites of a system. Return
# True if that system percolates, and False otherwise.

def percolates(isOpen):
    
    # Compute the full sites of the system.
    isFull = flow(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(isFull)
    for j in range(n):
        if isFull[n-1][j]:
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
    
if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python percolationv.py < test5.txt
# 5 5
# 0 1 1 0 1 
# 0 0 1 0 1 
# 0 0 0 0 1 
# 0 0 0 0 1 
# 0 0 0 0 1 
# True

# python percolationv.py < test8.txt
# 8 8
# 0 0 1 1 1 0 0 0 
# 0 0 0 1 1 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# False

