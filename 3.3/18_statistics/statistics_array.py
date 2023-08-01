#statistics 通过数组保存
import random

class Statistics:

    def __init__(self):
        self._l = []
        self._n = 0
    
    def add(self,a):
        self._l.append(a)
        self._n += 1

    def getNum(self):
        return self._n

    def mean(self):
        return sum(self._l)/self._n

    def stdDev(self):
        return self.variance()**.5

    def variance(self):
        m = self.mean()
        t = 0
        for i in range(self._n):
            t += self._l[i]**2-m**2
        return t/(self._n-1)

def main():
    #l = []
    l = [1,2,3,4,5,6,7,8,9,10]
    s = Statistics()
    for i in range(10):
        #t=(random.randint(0,10))
        #l.append(t)
        s.add(l[i])
    print(s.getNum())
    print('平均数：',s.mean())
    print('标准差:',s.stdDev())
    print('方差：',s.variance())
    print(l)

if __name__ =='__main__':
    main()
