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

s = sys.argv[1]
print(complementWC(s))
