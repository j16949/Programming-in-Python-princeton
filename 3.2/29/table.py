#目测是1928-2006年的股票
from entry import Entry

class Tabel:

    def __init__(self,file):
        self._l = list()
        with open(file,'r') as f:
            t = f.readline()    #第一行是标题，无用
            for line in f:
                el = line.split(',')
                self._l.append(Entry(el[0],el[1],el[2],el[3],el[4]))
        self._l.reverse()   #年份从小到大
    
    #计算从start到end时间股票的平均值，以收盘价为准
    #start和end的各式以.csv为准，偷懒；'6-Mar-06''17-Mar-06'
    def averages(self,start,end):
        i = 0
        total = 0
        s = -1
        while i < len(self._l):
            if self._l[i]._date == start:
                total += eval(self._l[i]._closePrice)
                s = i
                i += 1
                continue
            if s != -1:
                total += eval(self._l[i]._closePrice)
                if self._l[i]._date == end:
                    break
            i += 1
        return total/(i-s+1)


def main():
    table = Tabel('djia.csv')
    # print(len(table._l))
    # for i in range(len(table._l)):
    #     print(table._l[i])
    print(table.averages("1-Oct-28",'17-Mar-06'))

if __name__=='__main__':
    main()
