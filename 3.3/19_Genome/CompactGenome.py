#use a boolean array, encoding each base with two bits.
#无法实现two bits，因为python的bool类继承自int,这里只能用bool数组模拟
#baseAt(i), isPotentialGene() 

class Genome:
    def __init__(self):
        self._l = []

    def addCodon(self,c):
        if c == 'A':
            self._l.append(False)
            self._l.append(False)
        elif c == 'C':
            self._l.append(False)
            self._l.append(True)
        elif c == 'G':
            self._l.append(True)
            self._l.append(False)
        elif c == 'T':
            self._l.append(True)
            self._l.append(True)
        else:
            raise Exception("非法碱基")

    def baseAt(self,i):
        if 2*i < len(self._l):
            if self._l[2*i] == False:
                if self._l[2*i+1] == False:
                    return 'A'
                elif self._l[2*i+1] == True:
                    return 'C'
            if self._l[2*i] == True:
                if self._l[2*i+1] == False:
                    return 'G'
                elif self._l[2*i+1] == True:
                    return 'T'
        else:
            raise Exception("超出基因片段长度")

    def isPotentialGene(self):
        # number of bases is a multiple of 3
        if (len(self._l)/2 % 3) != 0: return False
        # starts with start codon
        if self._l[:6] != [False,False,True,True,True,False]: return False
        # no intervening stop codons
        for i in range(len(self._l) - 3*2,2):
            if i/2 % 3 == 0:
                #以下三行暂时先不改
                if self._l[i:i+6] == 'TAA': return False
                if self._l[i:i+6] == 'TAG': return False
                if self._l[i:i+6] == 'TGA': return False
        # ends with a stop codon
        if self._l[-6:]==[True,True,False,False,False,False]: return True
        if self._l[-6:]==[True,True,False,False,True,False]: return True
        if self._l[-6:]==[True,True,True,False,False,False]: return True
        return False

    def __len__(self):
        return(len(self._l)//2)

def main():
    g = Genome()
    g.addCodon('A')
    g.addCodon('C')
    g.addCodon('C')
    g.addCodon('A')
    g.addCodon('T')
    g.addCodon('G')
    for i in range(len(g)):
        print(g.baseAt(i),end='')
    print()
    print(g.isPotentialGene())
    g1 = Genome()
    s = 'ATGCGCCTGCGTCTGTACTAG'
    for c in s:
        g1.addCodon(c)
    for i in range(len(g1)):
        print(g1.baseAt(i),end='')
    print()
    print(g1.isPotentialGene())


if __name__ == '__main__':
    main()

        
