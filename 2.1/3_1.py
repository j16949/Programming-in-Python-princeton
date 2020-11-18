import stdarray
import sys

def majority(a, b, c):
    while a and b:
        return True
    while a and c:
        return True
    while b and c:
        return True
    return False


#把[0，1，0，1，1]输入转化为[False,True.....]
def trans(b=[]):
    c = stdarray.create1D(len(b))
    for i in range(len(b)):
        if b[i] == '1':
            c[i] = True
        else:
            c[i] = False
    return c

l = []
for t in sys.argv:
    l.append(t)
l.pop(0)
ll=trans(l)
#print(ll)
print(majority(ll[0],ll[1],ll[2]))

