#给定一个长字符串，输出所有以给定字符开始，给定字符结束的子字符串
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
import sys
import stdio
#-----------------------------------------------------------------------
#Return a list that cotains subStrings 
def subStrings(longString,begin,end):
    subs = []
    i = 0
    lb = len(begin)
    le = len(end)
    while i < len(longString):
        if longString[i:i+lb] == begin:
            for j in range(i+lb,len(longString)):
                temp =longString[j:j+le]
                if temp == end:
                    t = longString[i:j+le]
                    subs.append(t)
                    break
            i = j
        i += 1
    return subs
#-----------------------------------------------------------------------
# Accept a DNA sequence as a comand-line argument. Write to 
# True to standard output if the DNA sequence corresponds to a
# potential gene, and False otherwise.
#dna = sys.argv[1]
#longString可拆分为以下
#A
#BAIYUSHI
#SHIGEDASHUAIGE
#BAITIANSHI
#BAISEDESHI
#BUSHI
longString = 'ABAIYUSHISHIGEDASHUAIGEBAITIANSHIBAISEDESHIBUSHI'
begin='BAI'
end='SHI'
stdio.writeln(subStrings(longString,begin,end))
#-----------------------------------------------------------------------
# python potentialgene.py ATGCGCCTGCGTCTGTACTAG
# True
# python potentialgene.py ATGCGCTGCGTCTGTACTAG
# False
