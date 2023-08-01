#引用 appointment 和 calendar 来尝试预定约会

import enum
from mycalendar import Calendar
from appointment import Appointment
from datetime import date
import random

#假设想在一月约一个看牙
#假设一月已经约了差不多了，手动往一月填数据
c = Calendar()
#寻找一下一月的第一个星期一
year = 2022
mon = 1
j = 1
while date(year,mon,j).weekday() != 0:
    j += 1

c = Calendar()
for i in range(j,j+14):
    d = date(year,mon,i)
    if d.weekday() !=5 and d.weekday() !=6:
        a = Appointment(d,'test')
        c.addAppointment(a)

print(c._d)

while True:
    r = random.randint(1,31)
    d = date(2022,1,r)
    try:
        a = Appointment(d,'dentist')
        print(a.getDate())
        c.addAppointment(a)
        break
    except:
        print('出错')

for key,value in c._d.items():
    print(key,value)
