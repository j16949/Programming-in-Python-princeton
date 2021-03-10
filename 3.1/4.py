import sys
import luminance
import stdstats
import stddraw
from picture import Picture

pic = Picture(sys.argv[1])

freq = [0 for i in range(16)]   #0-255,每16为一个区间,因为256/16=16
norm = [0 for i in range(16)]   #不只用freq是为了除以总数，控制图大小

for col in range(pic.width()):
    for row in range(pic.height()):
        pixel = pic.get(col,row)
        lum = int(round(luminance.luminance(pixel)))
        freq[lum//16] += 1

for i in range(16):
    norm[i] = freq[i]/(pic.width()*pic.height())

stdstats.plotBars(norm)
stddraw.show()

