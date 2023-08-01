#Use a string as the only instance variable; implement addCodon() with string concatenation.
#baseAt(i), isPotentialGene() 

class Genome:
    def __init__(self):
        self._s=''

    def addCodon(self,c):
        if c in ['A','C','T','G']:
            self._s+=c
        else:
            raise Exception("非法碱基")

    def baseAt(self,i):
        if i < len(self._s):
            return self._s[i]
        else:
            raise Exception("超出基因片段长度")

    def isPotentialGene(self):
        # number of bases is a multiple of 3
        if (len(self._s) % 3) != 0: return False
        # starts with start codon
        if not self._s.startswith('ATG'): return False
        # no intervening stop codons
        for i in range(len(self._s) - 3):
            if i % 3 == 0:
                if self._s[i:i+3] == 'TAA': return False
                if self._s[i:i+3] == 'TAG': return False
                if self._s[i:i+3] == 'TGA': return False
        # ends with a stop codon
        if self._s.endswith('TAA'): return True
        if self._s.endswith('TAG'): return True
        if self._s.endswith('TGA'): return True
        return False

    def __len__(self):
        return(len(self._s))

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

        
