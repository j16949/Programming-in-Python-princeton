#-----------------------------------------------------------------------
# merge.py,逆向split.py
#-----------------------------------------------------------------------

import sys
import stdarray
from instream import InStream
from outstream import OutStream

#-----------------------------------------------------------------------

# Accept string inFile and integer outFile as command-line
# arguments. Split the file whose name is inFile.csv, by field,
# into outFile+1 files named inFile1.txt, inFile2.txt, etc.

DELIM = ','

inFile = sys.argv[1:len(sys.argv)-1]
outFile = sys.argv[len(sys.argv)-1]


# Read lines from the input stream and write them to the
# output stream.
#创建数组，每个数组保存一个inFile
n = len(sys.argv)-2
l = [[] for i in range(n)]

i = 0
for filename in inFile:
    inStream = InStream(filename)
    while inStream.hasNextLine():
        line = inStream.readLine()
        l[i].append(line)
    i += 1

#写入统一文件
s = ''
outStream = OutStream(outFile)
for i in range(len(l[0])):
    for j in range(n):
        s += l[j][i] + DELIM
    outStream.writeln(s[:-1])
    s = ''
#-----------------------------------------------------------------------

# more djia.csv
# Date,Open,High,Low,Close,Volume,Adj. Close*
# 17-Mar-06,11294.94,11294.94,11253.23,11279.65,2549619968,11279.65
# 16-Mar-06,11210.97,11324.80,11176.07,11253.24,2292179968,11253.24
# 15-Mar-06,11149.76,11258.28,11097.23,11209.77,2292999936,11209.77
# ...

# python split.py djia 3

# more djia0.txt
# Date
# 17-Mar-06
# 16-Mar-06
# 15-Mar-06
# ...

# more djia1.txt
# Open
# 11294.94
# 11210.97
# 11149.76
# ...

# more djia2.txt
# High
# 11294.94
# 11324.80
# 11258.28
# ...

# more djia3.txt
# Low
# 11253.23
# 11176.07
# 11097.23
# ...

