from charge import Charge
import sys

w = eval(sys.argv[1])

c1 = Charge(0.5-w,0.5,1)
c2 = Charge(0.5+w,0.5,1)
c3 = Charge(0.5,0.5-w,1)
c4 = Charge(0.5,0.5+w,1)

v1 = c1.potentialAt(.25,.5)
v2 = c2.potentialAt(.25,.5)
v3 = c3.potentialAt(.25,.5)
v4 = c4.potentialAt(.25,.5)

print('{0:.2e}'.format(v1+v2+v3+v4))
