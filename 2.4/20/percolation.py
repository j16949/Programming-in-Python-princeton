#-----------------------------------------------------------------------
# percolation.py
#-----------------------------------------------------------------------

import stdio
import stdarray
import stddraw
import percolationio

#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# isFull is a partially completed matrix that represents the full sites
# of that system. Update isFull by marking every site of that system
# that is open and reachable from site (i, j).

def _flow(isOpen, isFull, i, j):
    n = len(isFull[0])

    if (i < 0) or (i >= n):
        return
    if (j < 0) or (j >= n):
        return
    if not isOpen[i][j]:
        return
    if isFull[i][j]:
        return
    
    isFull[i][j] = True

    #显示渗透动画    
    # stddraw.setPenColor(stddraw.BLUE)
    # percolationio.draw(isFull,True)
    # stddraw.show(50)
    
    #横线,10条路
    if i % 2 == 0:
        _flow(isOpen, isFull, i+1, 2*j)     #LeftDownLeft
        _flow(isOpen, isFull, i+1, 2*j+1)   #LeftDownRight
        _flow(isOpen, isFull, i+1, (j+1)*2)     #RightDownLeft
        _flow(isOpen, isFull, i+1, (j+1)*2+1)   #RightDownRight
        _flow(isOpen, isFull, i  , j-1) #Left
        _flow(isOpen, isFull, i  , j+1) #Right
        _flow(isOpen, isFull, i-1, 2*j-1)     #LeftUpLeft
        _flow(isOpen, isFull, i-1, 2*j)   #LeftUpRight
        _flow(isOpen, isFull, i-1, (j+1)*2-1)     #RightUpLeft
        _flow(isOpen, isFull, i-1, (j+1)*2)   #RightUpRight
    #斜线，10条路，分为左斜右斜考虑
    else:
        #左斜
        if j % 2 == 0:
            _flow(isOpen, isFull, i+2, j)   #DownLeftDown
            _flow(isOpen, isFull, i+2, j+1)   #DownRightDown
            _flow(isOpen, isFull, i+1, int(j/2)-1)   #DownLeft
            _flow(isOpen, isFull, i+1, int(j/2))   #DownRight
            _flow(isOpen, isFull, i, j-1)   #DownLeftUp
            _flow(isOpen, isFull, i, j+1)   #UpRightDown
            _flow(isOpen, isFull, i-1, int(j/2)-1)   #UpLeft
            _flow(isOpen, isFull, i-1, int(j/2))   #UpRight
            _flow(isOpen, isFull, i-2, j-1)   #UpLeftUp
            _flow(isOpen, isFull, i-2, j)   #UpRightUp
        #右斜
        else:
            _flow(isOpen, isFull, i+2, j+1)   #DownLeftDown
            _flow(isOpen, isFull, i+2, j+2)   #DownRightDown
            _flow(isOpen, isFull, i+1, (j-1)//2)   #DownLeft
            _flow(isOpen, isFull, i+1, (j+1)//2)   #DownRight
            _flow(isOpen, isFull, i, j+1)   #DownRightUp
            _flow(isOpen, isFull, i, j-1)   #UpLeftDown
            _flow(isOpen, isFull, i-1, (j-3)//2)   #UpLeft
            _flow(isOpen, isFull, i-1, (j-1)//2)   #UpRight
            _flow(isOpen, isFull, i-2, j-2)   #UpLeftUp
            _flow(isOpen, isFull, i-2, j-1)   #UpRightUp
#-----------------------------------------------------------------------

# isOpen is a matrix that represents the open sites of a system.
# Compute and return a matrix that represents the full sites of
# that system.

def flow(isOpen):
    n = len(isOpen[0])
    isFull = stdarray.create2D(n, n, False)
    #出于好意，填上第一行，其实并没什么用，从第二行开始算起
    for j in range(n):
        _flow(isOpen, isFull, 0, j)
    #真正的渗透，从第二行开始
    for j in range(n):
        _flow(isOpen, isFull, 1, j)
    return isFull

#-----------------------------------------------------------------------

# isOpen is matrix that represents the open sites of a system. Return
# True if that system percolates, and False otherwise.

def percolates(isOpen):
    
    # Compute the full sites of the system.
    isFull = flow(isOpen)
    
    # If any site in the bottom row is full, then the system
    # percolates.
    n = len(isFull[0])
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

