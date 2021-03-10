#返回一个字符串的倒序
import sys

def mystery(s):
    n = len(s)
    if (n <= 1):return s
    a = s[0:n//2]
    b = s[n//2:n]
    return mystery(b)+mystery(a)

s = sys.argv[1]
print(mystery(s))
