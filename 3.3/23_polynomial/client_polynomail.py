from polynomial import Polynomial
import numpy as np

a = [1,2,3,4]
b = [3,2,3,2]
p = Polynomial(len(a),a)
q = Polynomial(len(b),b)
m = p+q
print(m)
c = Polynomial(3,[1,2,3])
d = Polynomial(2,[4,5])
print(c*d)
e = Polynomial(4,[-7,-2,3.5,-1])
print(c*e)
