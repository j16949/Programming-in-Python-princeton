#使用正则表达式
import re
import sys

def isValidDNA(s):
    s = s.upper()   #改为大写
    r = re.fullmatch('[ACTG]*',s)
    if not r:
        return False
    return True

s = sys.argv[1]
print(isValidDNA(s))
