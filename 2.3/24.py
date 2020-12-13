#-----------------------------------------------------------------------
# 24.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Write to standard output Beckett's stage instructions to have n
# actors enter (if parameter enter is True) or exit (if parameter
# enter is False) the stage.
#用list l 来表示相应位置的人进入+1，退出-1

def moves(n, enter,l):
    if n == 0:
        return
    moves(n-1, True,l)
    if enter:
        stdio.writeln('enter ' + str(n))
        l[n-1] += 1
        print(l)
    else:
        stdio.writeln('exit  ' + str(n))
        l[n-1] -= 1
        print(l)
    moves(n-1, False,l)
    return l

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard
# output Beckett's stage instructions (the bit positions that change
# in a binary-reflected Gray code) for n actors.

def main():
    n = int(sys.argv[1])
    l = [0] * n
    moves(n, True,l)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python beckett.py 1
# enter 1

# python beckett.py 2
# enter 1
# enter 2
# exit  1

# python beckett.py 3
# enter 1
# enter 2
# exit  1
# enter 3
# enter 1
# exit  2
# exit  1

# python beckett.py 4
# enter 1
# enter 2
# exit  1
# enter 3
# enter 1
# exit  2
# exit  1
# enter 4
# enter 1
# enter 2
# exit  1
# exit  3
# enter 1
# exit  2
# exit  1

