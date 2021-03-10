#判断一个网址的域名类型，如com,edu
#判断方法为判断是否有‘.xxx/'的形式的内容，如果没有，取出最有一个.xxx
#https://introcs.cs.princeton.edu/python/31datatype/
#https://www.runoob.com/python3/python3-inputoutput.html

import sys
import re

def typeOfDomain(s):
    r= re.search('\.(.(?!\.))*/.*',s)   #匹配以.开始，后续字符串不含.的string(包含后续路径)
    if not r:
        r1 = re.search('\.\w*$',s) #匹配直接以.com,.xxx结尾的域名
        return r1[1:-1]
    return re.search('\..*?/',r[0])[0][1:-1]

s1='https://introcs.cs.princeton.edu/python/31datatype/'
s2='https://www.runoob.com/python3/python3-inputoutput.html'
s3='https://zh.wikipedia.org/'

print(typeOfDomain(s1))
print(typeOfDomain(s2))
print(typeOfDomain(s3))
