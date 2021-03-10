#分析道琼斯指数从1928年到2005年股票调整收盘价和成交量的关系
#收盘价从0-20000（目测100-11000）,读文件判断:hPrice,hVolume

import sys
import stddraw
import stdstats

volume = []
price  = []
year   = []
bili   = 20     #控制每多少个数据为一个点
hVolume = []    #根据bili，n个数为一个值
hPrice  = []
bYear   = '1928'
eYear   = '1980'

with open('djia.csv','r') as file:
    for line in file:
        fields = line.split(',')
        year.append(fields[0][-2:])
        volume.append(fields[5])
        price.append(fields[6].strip()) #strip掉'\n'

print(len(volume))
#去掉第一列,第一列为列名
year = year[1:]
volume = volume[1:]
price  = price[1:]
year.reverse()
volume.reverse()
price.reverse()

#控制显示年份,不考虑从2000年以后开始的
begin = 0
end   = len(year)
for i in range(len(year)):
    if year[i] == bYear[-2:]:
        begin = i
    if year[i] == eYear[-2:]:
        end = i

year = year[begin:end]
volume = volume[begin:end]
price = price[begin:end]

t = 0
for i in range(len(volume)):
    volume[i] =eval(volume[i])/ 100000
    t += volume[i]
    if (i+1) % bili == 0 :
        hVolume.append(t/bili)
        t = 0

t = 0
for i in range(len(price)):
    price[i] = eval(price[i])
    t += price[i]
    if (i+1) % bili == 0 :
        hPrice.append(t/bili)
        t = 0


print(len(hVolume))

stddraw.setCanvasSize(1000,500)
stddraw.setYscale(0,1.1*max(max(hVolume),max(hPrice)))
stdstats.plotLines(hVolume)
stddraw.setPenColor(stddraw.BLUE)
stdstats.plotLines(hPrice)
stddraw.show()
