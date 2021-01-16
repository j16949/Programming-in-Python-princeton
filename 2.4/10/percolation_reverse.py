#-----------------------------------------------------------------------
# percolation.py
#结果显示，如果递归深度不是0，最后标记的网格为初始网格上方网格，即(-1,x)
#-----------------------------------------------------------------------

import stdio
import stdarray
import percolationio
import stddraw

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# isFull is a partially completed matrix that represents the full sites
# of that system. Update isFull by marking every site of that system
# that is open and reachable from site (i, j).

depth = 0
depth_l=[]

def _flow(isOpen, isFull, i, j):
    n = len(isFull)
    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= n):
        return
    if not isOpen[i][j]:
        return
    if isFull[i][j]:
        return
    isFull[i][j] = True
    '''
    stddraw.setPenColor(stddraw.BLUE)
    percolationio.draw(isFull,True)
    stddraw.show(100)
    '''
    global depth
    depth += 1
    _flow(isOpen, isFull, i-1, j  )  # Up.
    _flow(isOpen, isFull, i  , j-1)  # Left.
    _flow(isOpen, isFull, i  , j+1)  # Right.
    _flow(isOpen, isFull, i+1, j  )  # Down.

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# Compute and return a matrix that represents the full sites of
# that system.

def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n, n, False)
    for j in range(n):
        global depth,depth_l
        depth = 0
        _flow(isOpen, isFull, 0, j)
        #print('depth:',depth)
        depth_l.append(depth)
    #print(depth_l)
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

