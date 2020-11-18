#-----------------------------------------------------------------------
# matrix.py
#-----------------------------------------------------------------------

import sys
import stdarray
import random

# A bare-bones collection of static methods for manipulating matrices.

#-----------------------------------------------------------------------

# Return an m-by-n matrix containing random float values between
# 0 and 1.

def rand(m, n):
    randMatrix = stdarray.create2D(m, n, 0.0)
    for i in range(m):
        for j in range(n):
            randMatrix[i][j] = random.random()
    return randMatrix

#-----------------------------------------------------------------------

# Return an n-by-n identity matrix.

def identity(n):
    identityMatrix = stdarray.create2D(n, n, 0.0)
    for i in range(n):
        identityMatrix[i][i] = 1.0
    return identityMatrix

#-----------------------------------------------------------------------

# Return the number which is the dot product of vectors v1 and v2.

def dot(v1, v2):
    v1Length = len(v1)

    if v1Length != len(v2):
        raise Exception('v1 length must equal v2 length')

    dotProd = 0.0
    for i in range(v1Length):
        dotProd += v1[i] * v2[i]
    return dotProd

#-----------------------------------------------------------------------

# Return the matrix which is the transpose of square matrix m.

def transpose(m):
    rowCount = len(m)
    colCount = len(m[0])

    if rowCount != colCount:
        raise Exception('row count must equal col count')

    transposeMatrix = stdarray.create2D(rowCount, colCount, 0.0)
    for row in range(rowCount):
        for col in range(colCount):
            transposeMatrix[col][row] = m[row][col]
    return transposeMatrix

#-----------------------------------------------------------------------

# Return the matrix which is the sum of matrices m1 and m2.

def add(m1, m2):
    rowCount = len(m1)
    colCount = len(m1[0])

    if rowCount != len(m2):
        raise Exception('m1 row count must equal m2 row count')
    if colCount != len(m2[0]):
        raise Exception('m1 col count must equal m2 col count')

    total = stdarray.create2D(rowCount, colCount, 0.0)
    for row in range(rowCount):
        for col in range(colCount):
            total[row][col] = m1[row][col] + m2[row][col]
    return total

#-----------------------------------------------------------------------

# Return the matrix which is the difference of matrices m1 and m2.

def subtract(m1, m2):
    rowCount = len(m1)
    colCount = len(m1[0])

    if rowCount != len(m2):
        raise Exception('m1 row count must equal m2 row count')
    if colCount != len(m2[0]):
        raise Exception('m1 col count must equal m2 col count')

    diff = stdarray.create2D(rowCount, colCount, 0.0)
    for row in range(rowCount):
        for col in range(colCount):
            diff[row][col] = m1[row][col] - m2[row][col]
    return diff

#-----------------------------------------------------------------------

# Return the matrix which is the product of matrices m1 and m2.

def multiplyMM(m1, m2):

    m1RowCount = len(m1)
    m1ColCount = len(m1[0])
    m2RowCount = len(m2)
    m2ColCount = len(m2[0])

    if m1ColCount != m2RowCount:
        raise Exception('m1 col count must equal m2 row count')

    prod = stdarray.create2D(m1RowCount, m2ColCount, 0.0)
    for i in range(m1RowCount):
        for j in range(m2ColCount):
            for k in range(m1ColCount):
                prod[i][j] += m1[i][k] * m2[k][j]
    return prod

#-----------------------------------------------------------------------

# Return the vector which is the matrix-vector product of matrix m
# and vector v.

def multiplyMV(m, v):
    mRowCount = len(m)
    mColCount = len(m[0])
    vLength = len(v)

    if mColCount != vLength:
        raise Exception('m col count must equal v length')

    prod = stdarray.create1D(mRowCount, 0.0)
    for i in range(mRowCount):
        for j in range(mColCount):
            prod[i] += m[i][j] * v[j]
    return prod

#-----------------------------------------------------------------------

# Return the vector which is the vector-matrix product of vector v
# and matrix m.

def multiplyVM(v, m):
    vLength = len(v)
    mRowCount = len(m)
    mColCount = len(m[0])

    if vLength != mRowCount:
        raise Exception('v length must equal m row count')

    prod = stdarray.create1D(mColCount, 0.0)
    for j in range(mColCount):
        for i in range(mRowCount):
            prod[j] += m[i][j] * v[i]
    return prod

#-----------------------------------------------------------------------

# For testing.

def main():

    import stdio

    stdio.writeln('A')
    stdio.writeln('--------------------')
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    stdarray.write2D(a)
    stdio.writeln()

    stdio.writeln('B')
    stdio.writeln('--------------------')
    b = identity(5)
    stdarray.write2D(b)
    stdio.writeln()

    stdio.writeln('C')
    stdio.writeln('--------------------')
    c = rand(5, 5)
    stdarray.write2D(c)
    stdio.writeln()

    stdio.writeln('A^T')
    stdio.writeln('--------------------')
    at = transpose(a);
    stdarray.write2D(b)
    stdio.writeln()

    stdio.writeln('A + A^T')
    stdio.writeln('--------------------')
    d = add(a, at)
    stdarray.write2D(d)
    stdio.writeln()

    stdio.writeln('A * A^T')
    stdio.writeln('--------------------')
    e = multiplyMM(a, at)
    stdarray.write2D(e)
    stdio.writeln()
    
    # stdio.writeln('--------------------')
    # stdio.writeln('--------------------')

    # moves = int(sys.argv[1])
    # p = stdarray.readFloat2D()
    # ranks = stdarray.create1D(len(p), 0.0)
    # ranks[0] = 1.0
    # for i in range(moves):
    #     ranks = multiplyVM(ranks, p)
    # stdarray.write1D(ranks)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python matrix.py
# A
# --------------------
# 3 3
# 1 2 3 
# 4 5 6 
# 7 8 9 
# 
# B
# --------------------
# 5 5
# 1.0 0.0 0.0 0.0 0.0 
# 0.0 1.0 0.0 0.0 0.0 
# 0.0 0.0 1.0 0.0 0.0 
# 0.0 0.0 0.0 1.0 0.0 
# 0.0 0.0 0.0 0.0 1.0 
# 
# C
# --------------------
# 5 5
# 0.37627444331077653 0.32586357815639067 0.23540064982343156 0.6899813748554937 0.5286982582636341 
# 0.28992687465780576 0.5629957065410093 0.45781423848968006 0.8903057550676357 0.5601631173759734 
# 0.6785301245100017 0.11651814401724558 0.8763789354440634 0.032291377717908465 0.32928407619813105 
# 0.6173798692131891 0.7550840799583114 0.3348102933789717 0.705621812503534 0.09121764056242698 
# 0.1803750228194455 0.5135643692698265 0.09450902697153707 0.5250451696720445 0.7724263231251629 

# A^T
# --------------------
# 5 5
# 1.0 0.0 0.0 0.0 0.0 
# 0.0 1.0 0.0 0.0 0.0 
# 0.0 0.0 1.0 0.0 0.0 
# 0.0 0.0 0.0 1.0 0.0 
# 0.0 0.0 0.0 0.0 1.0 
# 
# A + A^T
# --------------------
# 3 3
# 2 6 10 
# 6 10 14 
# 10 14 18 
# 
# A * A^T
# --------------------
# 3 3
# 14.0 32.0 50.0 
# 32.0 77.0 122.0 
# 50.0 122.0 194.0
#
