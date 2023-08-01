#-----------------------------------------------------------------------
# sketch.py
#-----------------------------------------------------------------------

import sys
import stdio
import stdarray
from vector import Vector
import hashlib

#-----------------------------------------------------------------------

class Sketch:

    # Construct a new Sketch object which is a profile of string
    # text. The profile should consist of a unit vector of dimension
    # d. Element i of the vector should indicate how many k-grams
    # in the file (or web page) hash to i.
    # 改用hasklib使得结果每次运行结果保持一致
    def __init__(self, text, k, d):
        freq = stdarray.create1D(d, 0)
        kg = stdarray.create1D(d, 0)
        for i in range(len(text) - k + 1):
            kgram = text[i:i+k]
            h = hashlib.sha1()
            h.update(kgram.encode())
            h = h.hexdigest()
            #print(h)
            #print(type(h))
            t = eval('0x'+h) % d
            freq[t] += 1
            kg[t]=kgram
        vector = Vector(freq)
        self._sketch = vector.direction()  # Unit vector
        print(kg)
        print(freq)

    # Return the similarity measure between self and Sketch object
    # other as a number between 0 and 1. 0 indicates that the
    # objects are dissimilar; 1 indicates that they are similar.
    def similarTo(self, other):
        return self._sketch.dot(other._sketch)

    # Return a string representation of self.
    def __str__(self):
        return str(self._sketch)

#-----------------------------------------------------------------------

# For testing.
# Accept integers k and d as command-line arguments. Read text from
# standard input, and construct a Sketch object from that text, k, and
# d. Write the Sketch object to standard output.

def main():
    # text = stdio.readAll()
    # k = int(sys.argv[1])
    # d = int(sys.argv[2])
    text = 'ATAGATGCATAGCGCATAGC'
    k = 2
    d = 16
    sketch = Sketch(text, k, d)
    stdio.writeln(sketch)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# more genome20.txt 
# ATAGATGCATAGCGCATAGC

# python sketch.py 2 16 < genome20.txt 
# [0.37210420376762543, 0.37210420376762543, 0.49613893835683387, 
# 0.0, 0.12403473458920847, 0.0, 
# 0.0, 0.0, 0.0, 
# 0.0, 0.24806946917841693, 0.0, 
# 0.12403473458920847, 0.6201736729460423, 0.0, 0.0]

