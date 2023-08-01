#python官方文档time模块写道：
#此模块中定义的大多数函数的实现都是调用其所在平台的C语言库的同名函数。因为这些函数的语义可能因平台而异，所以使用时最好查阅对应平台的相关文档。
#且python或C获取的时间都为运行程序的终端的时间，所以依据题意，想获得当前时间无论如何都得引入系统时间，无论是OS.SYSTEM()还是time。
#python有两个主要处理时间的模块:1.datetime;2.time，其中datetime也可以计算日期。datetime.datetime可以作运算返回datetime.timedelta对象，time.time()则返回float对象
#由于需要创建0点的时间，而time模块中time_struct是只读的，无法创建，方法有二：1.用datetime.datetime创建；2.用striptime格式化。此处采用方法1
#此处使用time,用秒来计算
import datetime
import time as rt   #防止重名

class time:
    def __init__(self):
        a = datetime.datetime.today()
        b = datetime.datetime(a.year,a.month,a.day)
        self._t = rt.time()-b.timestamp()

    def curHour(self):
        return self._t//3600

    def curMinute(self):
        return self._t//60

    def curSecond(self):
        return self._t

    def __str__(self):
        hour = self.curHour()
        minute = self.curMinute()-hour*60
        second = self.curSecond()-hour*60*60-minute*60
        return '当前时间是:'+str(int(hour))+':'+str(int(minute))+':'+str(int(second))

def main():
    t = time()
    print('hour:',t.curHour())
    print('minute:',t.curMinute())
    print('second:',t.curSecond())
    print(t)
    rt.sleep(2)
    print(time())

if __name__ == '__main__':
    main()
