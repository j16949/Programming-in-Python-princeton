#rawpicture.py的client

import rawpicture as Rp
from picture import Picture

fileName = 'heroes-Peter.jpg'

p = Picture(fileName)
sp = Rp.write(p)

with open('26.txt','w') as f:
    f.write(str(sp[0])+'\n')
    f.write(str(sp[1])+'\n')
    for col in range(sp[0]):
        for raw in range(sp[1]):
            for i in range(3):
                f.write(str(sp[2][raw][col][i])+' ')
        f.write('\n')

