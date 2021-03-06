import random
import sys
import stddraw
from rectangle import Rectangle

# n = eval(sys.argv[1])
# lo = eval(sys.argv[2])  #为保持画布大小，lo和hi取值，2，6
# hi = eval(sys.argv[3])

n = 3
lo = 2  #为保持画布大小，lo和hi取值，2，6
hi = 6

stddraw.setCanvasSize(1000,1000)
stddraw.setXscale(-6,6)
stddraw.setYscale(-6,6)

i = 0
r = []
while i < n:
    x = random.randint(-3,3)
    y = random.randint(-3,3)
    width = random.randint(lo,hi)
    height = random.randint(lo,hi)
    r.append(Rectangle(x,y,width,height))
    i += 1

area = 0
per = 0

for t in r:
    area += t.area()
    per += t.perimeter()
    t.draw()

print(area/len(r))
print(per/len(r))

#分别计算，相交是相互的，包含是分主体的
i = 0
inter = 0
l = len(r)
while i < l:
    j = i+1
    while j < l:
        if r[i].intersects(r[j]):
            inter += 1
        j += 1
    i += 1

i = 0
con = 0
while i < l:
    j = 0
    while j < l:
        if j != i:
            if r[i].contains(r[j]):
                con += 1
        j += 1
    i += 1 

print('相交：',inter)
print('包含:',con)
stddraw.show()

