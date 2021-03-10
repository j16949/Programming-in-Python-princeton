import sys

s = 'ACTGACG'
t = 'TGACGAC'

def circularShift(s,t):
    for i in range(len(s)):
        if t == s[i:]+s[:i]:
            return True
    return False

print(circularShift(s,t))
