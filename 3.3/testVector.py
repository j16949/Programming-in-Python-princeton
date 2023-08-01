from vectorComplex import Vector

a = [1,2,1]
b = complex(1,1)
a [0] = b
v = Vector(a)
print(v.dot(v))
print(abs(v))


a = [1,2,1]
v = Vector(a)
print(v.dot(v))
print(abs(v))

b = [6,4,3]
vb = Vector(b)
print(vb-v)
