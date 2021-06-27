#PeriodicTable
#从.csv文件读入数据，创建一个内容是Element类的list,读入数据，计算如H2O的质量
import re
from element import Element
from decimal import Decimal

class PeriodicTable:

    def __init__(self,f):
        self._l = []
        with open(f,'r') as f:
            l = f.readline()    #去除第一行标题
            l = f.readline().split(',')
            while l != ['']:
                e = Element(l[0],eval(l[1]),l[2],eval(l[3]))
                l = f.readline().split(',')
                self._l.append(e)

    def printf(self):
        for i in range(len(self._l)):
            print(self._l[i])

    #返回分子质量
    #元素的第一个字母都是大写的，第二个都是小写的
    #H2O,SiO2,Na2S，NaCl，C12H10CaO2
    def molecularWeight(self,s):
        l = re.split('([A-Z][a-z]?)',s)   #()表示保留字母
        weight = 0
        i = 0
        while i < len(l):
            if re.findall('[A-Z]',l[i]):
                sym = l[i]
                for j in range(len(self._l)):
                    if sym == self._l[j].getSymbol():
                        aw = self._l[j].getWeight()
                        break
                if l[i+1]:
                    weight += eval(l[i+1]) * aw
                else:
                    weight += aw
                i += 1                
            i += 1
        #print(l)
        w = Decimal(weight).quantize(Decimal("0.01"),rounding = "ROUND_HALF_UP")  #四舍五入，保留小数点后两位
        return w

def main():
    p = PeriodicTable('elements.csv')
    print(p.molecularWeight('H2O'))
    print(p.molecularWeight('Si2O4'))
    print(p.molecularWeight('Na2S'))
    print(p.molecularWeight('NaCl'))
    print(p.molecularWeight('C12H10CO2'))
    
if __name__=='__main__':
    main()
