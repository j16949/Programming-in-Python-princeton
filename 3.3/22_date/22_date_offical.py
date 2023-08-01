#22. 日期（ Date）。 请 开发 一个 API， 用于 日期（ 年、 月、 日）。 请 包含 比较 两个 日期 的 方法， 包括 计算 两个 日期 之间 的 天数 差， 确定 给定 日期 的 星期， 以及 其他 你 认为 客户 端 可能 需要 的 方法。 设计 好 API 后， 请与 Python 的 datetime. date 数据 类型 进行 比较。
#Dates. Develop an API for dates (year, month, day). Include methods for comparing two dates chronologically, computing the number of days between two dates, determining the day of the week of a given date, and any other operations that you think a client might want. After you have designed your API, look at the Python's datetime.date data type.

import datetime
import calendar
from datetime import date

d = date(2001,11,10)
d1 = date(1900,12,10)
d0 = date(1,1,1)
print(d-d0+datetime.timedelta(days=1))
#print(datetime._ymd2ord(d))
print(calendar.leapdays(d1.year,d.year))
print(d1<d)
print(d1>d)
d0 = d
print(d==d0)
print(d-d1)
print(d.weekday())
print(d1.weekday())
