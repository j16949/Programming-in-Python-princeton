import datetime

class time:
    def __init__(self):
        self._h = datetime.datetime.now().hour
        self._m = datetime.datetime.now().minute
        self._s = datetime.datetime.now().second

    def curHour(self):
        return self._h

    def curMinute(self):
        return self._m+self._h*60

    def curSecond(self):
        return self.curMinute()*60+self._s

    def __str__(self):
        def str0(t):
            if t < 10:
                return '0'+str(t)
            return str(t)
        return '当前时间是:'+str0(int(self._h))+':'+str0(int(self._m))+':'+str0(int(self._s))

def main():
    t = time()
    print('hour:',t.curHour())
    print('minute:',t.curMinute())
    print('second:',t.curSecond())
    print(t)

if __name__ == '__main__':
    main()
