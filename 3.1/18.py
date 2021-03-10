#查找一个很长的DNA中包含的潜在基因，即以启动子到终止子标记一个基因。然后增加一个参数，控制潜在基因最小长度
#写完函数后发现并没有使用isPotentialGene(),- -,minLen用于限制基因最小长度
#-----------------------------------------------------------------------
# potentialgene.py
#-----------------------------------------------------------------------

import sys
import stdio

#-----------------------------------------------------------------------

# Return True if string dna corresponds to a potential gene, that is,
# if its length is a multiple of 3, it starts with the start codon
# (ATG), it ends with a stop codon (TAA or TAG or TGA), and it has
# no intervening stop codons. Otherwise return FALSE.

def isPotentialGene(dna):
    # number of bases is a multiple of 3
    if (len(dna) % 3) != 0: return False
    # starts with start codon
    if not dna.startswith('ATG'): return False
    # no intervening stop codons
    for i in range(len(dna) - 3):
        if i % 3 == 0:
            if dna[i:i+3] == 'TAA': return False
            if dna[i:i+3] == 'TAG': return False
            if dna[i:i+3] == 'TGA': return False
    # ends with a stop codon
    if dna.endswith('TAA'): return True
    if dna.endswith('TAG'): return True
    if dna.endswith('TGA'): return True
    return False

#-----------------------------------------------------------------------

#Return a list that cotains genes 

def PotentialGenes(longDNA,minLen):
    genes = []
    i = 0
    while i < len(longDNA):
        if longDNA[i:i+3] == 'ATG':
            j = i+3
            while j < len(longDNA):
            #for j in range(i+3,len(longDNA)):
                if (j-i-3) % 3 == 0:    #以i+3到最后为一个字符串，所以除以3要从新字符串算起
                    temp =longDNA[j:j+3]
                    if temp == 'TAA' or temp == 'TAG' or temp == 'TGA':
                        t = longDNA[i:j+3]
                        # if isPotentialGene(t):
                        #     genes.append(t)
                        if len(t) >= minLen:
                            genes.append(t)
                        break   #跳出上层WHILE循环，重新寻找子字符串
                    elif temp == 'ATG': #如果子字符串包含‘ATG’则，重新开始计算子字符串
                        i = j   #重新计算此子字符串开头
                j += 1
            i = j
        i += 1
    return genes

#-----------------------------------------------------------------------
# Accept a DNA sequence as a comand-line argument. Write to 
# True to standard output if the DNA sequence corresponds to a
# potential gene, and False otherwise.

#dna = sys.argv[1]
#longDNA可拆分为以下
#AATG
#ATGCGCCTGCGTCTGTACTAG
#ACCA
#ATGACGTAA
#CTC
#ATGAAACCCTTTGGGTGA
#AATGACGATAA
longDNA = 'AATGATGCGCCTGCGTCTGTACTAGACCAATGACGTAACTCATGAAACCCTTTGGGTGAAATGACGATAA'
minLen = 0
stdio.writeln(PotentialGenes(longDNA,minLen))

#-----------------------------------------------------------------------

# python potentialgene.py ATGCGCCTGCGTCTGTACTAG
# True

# python potentialgene.py ATGCGCTGCGTCTGTACTAG
# False

