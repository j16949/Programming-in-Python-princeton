import sys

def isValidDNA(s):
    s = s.upper()   #改为大写
    for t in s:
        if t !='A' and t!='C' and t!='T' and t!='G':
            return False
    return True

s = sys.argv[1]
print(isValidDNA(s))
