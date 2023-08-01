import random
import re
import math

class Location:
    
    def __init__(self,latitude,longitude):
        if -90 <= latitude <= 90 and -180 <= longitude <= 180:
            self.__latitude = latitude
            self.__longitude = longitude
        else:
            raise Exception('经度或纬度超出范围。')
    
    def __str__(self):
        return str(self.__latitude)+' N,'+str(self.__longitude)+' W'

    def distance(self,other):
        R = 6378.137    #地球半径，单位千米
        #转换为弧度
        la1 = math.radians(self.__latitude)
        la2 = math.radians(other.__latitude)
        lo1 = math.radians(self.__longitude)
        lo2 = math.radians(other.__longitude)
        return 2*math.asin(math.sqrt(math.sin((la1-la2)/2)**2+
        math.cos(la1)*math.cos(la2)*math.sin((lo1-lo2)/2)**2))*R

def randomLocation():
    #疑惑random.uniform到底是否可以取到上限
    #所以此处使用randint,保留三位小数
    la = random.randint(-90000,90000)/1000
    lo = random.randint(-180000,180000)/1000
    return Location(la,lo)


def parseLocation(s):
    #去掉两端‘，’
    s = s.strip(',')
    #判断s是否合法
    if s.count(',') == 1:
        s1,s2 = s.split(',')
        if s1.count('.') == 1:
            la = re.search('[0-9]+(\.[0-9]*)?',s1)
            if s2.count('.') == 1:
                lo = re.search('[0-9]+(\.[0-9]*)?',s2)
                return Location(eval(la[0]),eval(lo[0]))
    raise Exception('输入不合法!')

def main():
    l = Location(21.99,33.788)
    print(l)
    rl = randomLocation()
    print(rl)
    s = ' 33.2 N,21.0 W,'
    a = parseLocation(s)
    s = '31.222831N,115.883174W'
    b = parseLocation(s)
    print(a.distance(b))

    s = ' 33.2 N,21.0 W,'
    a = parseLocation(s)
    s = '31.222831N,121.95435W'
    b = parseLocation(s)
    print(a.distance(b))
        
if __name__ == '__main__':
    main()
