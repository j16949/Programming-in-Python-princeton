import stdstats
import stddraw

#a = [1,1,9,3,5,6,8,10]
a = [1] 

print('mean:',stdstats.mean(a))
print('var:',stdstats.var(a))
print('stddev:',stdstats.stddev(a))
print('median:',stdstats.median(a))
stddraw.setYscale(min(a)-2,max(a)+2)
stdstats.plotPoints(a)
stdstats.plotLines(a)
stdstats.plotBars(a)
stddraw.show()
