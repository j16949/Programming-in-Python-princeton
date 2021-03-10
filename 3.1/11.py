import sys

def complementWC(s):
    s = s.upper()
    r =''
    for t in s:
        if t == 'A':
            r += 'T'
        elif t == 'T':
            r += 'A'
        elif t == 'C':
            r += 'G'
        elif t == 'G':
            r += 'C'
        else:
            r += t
    return r

def palindromeWC(s):
    s = s.upper()
    if s[::-1] == complementWC(s):
        return True
    return False

s = sys.argv[1]
print(palindromeWC(s))
