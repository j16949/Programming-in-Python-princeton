#statistics 通过number,sum1,sum2,即总数，所有数字的和，所有数平方和
import random

class Statistics:

    def __init__(self):
        self._number = 0
        self._sum1 = 0
        self._sum2 = 0
    
    def add(self,a):
        self._number += 1
        self._sum1 += a
        self._sum2 += a**2

    def getNum(self):
        return self._number

    def mean(self):
        return self._sum1/self._number

    def stdDev(self):
        return self.variance()**.5

    def variance(self):
        return (self._number*self._sum2-self._sum1**2)/(self._number*(self._number-1))

def main():
  #  l = []
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = Statistics()
    for i in range(10):
   #     t=(random.randint(0,10))
    #    l.append(t)
        s.add(l[i])
    print(s.getNum())
    print('平均数：',s.mean())
    print('标准差:',s.stdDev())
    print('方差：',s.variance())
    print(l)

if __name__ =='__main__':
    main()
