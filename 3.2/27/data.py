import math
import stdstats 
import stddraw
import tukey

class Data:

    def __init__(self,n):
        self._l = [ 0 for i in range(n)]

    def addDataPoint(self,i,x):
        self._l[i] = x
    
    #题目没明确要求，此处绘制点图+折线图
    def plot(self):
        #stddraw.setPenColor('GRAY')
        stdstats.plotPoints(self._l)
        stdstats.plotLines(self._l)

    def plotTukey(self):
        tukey.TP(self._l)
    
    #返回最大数，以便绘图时设置Y轴
    def maxData(self):
        return max(self._l)
    
    def minData(self):
        return min(self._l)
def main():
    d = Data(10)
    for i in range(10):
        d.addDataPoint(i,i)
    stddraw.setYscale(d.minData(),1.1*d.maxData())
    d.plotTukey()
    d.plot()
    stddraw.show()

if __name__ == '__main__':
    main()
