#from time_seconds_global import time
from time_hhmmss import time
import time as rt

t = time()
print('hour:',t.curHour())
print('minute:',t.curMinute())
print('second:',t.curSecond())
print(t)
rt.sleep(2)
t1 = time()
print(t1)