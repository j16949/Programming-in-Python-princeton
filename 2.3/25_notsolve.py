#-----------------------------------------------------------------------
# towersofhanoiVariant（未解决)
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Write to standard output instructions to move n Towers of Hanoi
# disks to the left (if parameter left is True) or to the right (if
# parameter left is False).
# 只处理2n的问题(即偶数个)
# 看为3个部分，1.最左侧的2n-1号盘；2最右侧的2n号盘；3其他盘
# 步骤为：1.将其他盘移动到第2n个上，即最右侧；2.将2n-1号盘右移一格；3.将其他盘移动到2n-1上，即从最右移动到中间;
#         4.将2n号盘右侧移动，即移动到最左侧；5.将其他盘移动到2n上，即最左侧柱子；6.将2n-1号盘右移，即移动到最右侧
#         7.将其他盘按奇数偶数分开

def moves(n, left):
    if n == 0:
        return
    moves(n-1, not left)
    if left:
        stdio.writeln(str(n) + ' left')
    else:
        stdio.writeln(str(n) + ' right')
    moves(n-1, not left)

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard output
# instructions to move n Towers of Hanoi disks to the left.

def main():
    n = int(sys.argv[1])
    moves(n, True)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------
'''
0.一个 1
1l

1.两个 3
1r 2r 1r

2.三个 5
2l 1r 3l 1r 2l

3.四个 11
1l 3r 1r 2l 1r 4r 1r 2l 1r 3r 1l

4.五个 28
2l 1r 3l 1l 2r 1r 5r (1l 2r 1l 3l 1l 2r 1l 4r) (7) 5r 1l 2r 1l 3l 1r 2l
'''

