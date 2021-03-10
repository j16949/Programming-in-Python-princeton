#反向输出域名如输入www.baidu.com，输出com.baidu.www
#方法：根据'.'split
#https://introcs.cs.princeton.edu/python/31datatype/
#https://www.runoob.com/python3/python3-inputoutput.html

import sys
import re

def noHttp(s):
    r= re.search('//.*?/',s)    #匹配结果类似：“'//www.runoob.com/'”
    return r[0][2:-1]

def reverseDomain(s):
    if s[:8] == 'https://' or s[:7] == 'http://':
        s = noHttp(s)
    ls = s.split('.')
    rs = ''
    for t in ls:
        rs = t +'.'+ rs
    return rs[:-1]

s1='https://introcs.cs.princeton.edu/python/31datatype/'
s2='https://www.runoob.com/python3/python3-inputoutput.html'
s3='https://zh.wikipedia.org/'

print(reverseDomain(s1))
print(reverseDomain(s2))
print(reverseDomain(s3))
