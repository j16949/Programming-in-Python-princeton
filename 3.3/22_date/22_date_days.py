#22. 日期（ Date）。 请 开发 一个 API， 用于 日期（ 年、 月、 日）。 请 包含 比较 两个 日期 的 方法， 包括 计算 两个 日期 之间 的 天数 差， 确定 给定 日期 的 星期， 以及 其他 你 认为 客户 端 可能 需要 的 方法。 设计 好 API 后， 请与 Python 的 datetime. date 数据 类型 进行 比较。
#Dates. Develop an API for dates (year, month, day). Include methods for comparing two dates chronologically, computing the number of days between two dates, determining the day of the week of a given date, and any other operations that you think a client might want. After you have designed your API, look at the Python's datetime.date data type.
#统一先计算距离公元1年1月1日多少天，再做其他运算，days(),daysInMonth(),daysBeforeMonth();
#未包含输入合法性验证
#python没有考虑1582年10月少10天的问题，因此规定1年1月1日为星期一，而真正应为星期六

_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#判断是否是闰年
def isleap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 ==0:
            return True
    return False

def daysInMonth(year,month):
    if isleap(year):
        if month == 2:
            return 29
    return _DAYS_IN_MONTH[month]

def daysBeforeMonth(year,month):
    days = 0
    for i in range(1,month):
        days += daysInMonth(year,i)
    return days

def days(year,month,day):
    days = (year-1)*365 + leapYears(1,year) + daysBeforeMonth(year,month) + day
    return days

#判断两个年份间闰年的数量
#这个函数想法不对，闰不闰关键在于是否过了二月，过了二月加一天，应该计算leapdays(date1,date2)
#这个函数也可作为工具函数，仅计算从[y1,y2)年（即不包含y2年）间总共多少个闰了多少天
def leapYears(y1,y2):
    y = 0
    if y1 > y2 : y1,y2 = y2,y1
    for i in range(y1,y2):
        if isleap(i):
            y+=1
    return y

class Date:

    #此处year,month,day不该为私有变量 
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    
    #工具类计算天数
    def _days(self):
        return days(self.year,self.month,self.day)

    #判断时间前后顺序，以便计算
    def isEarlier(self,other):
        if self._days() < other._days():
            return True
        return False

    #<
    def __lt__(self,other):
        return self.isEarlier(other)
    #>
    def __gt__(self,other):
        if self != other and not self.isEarlier(other):
            return True
        return False
    # == 
    def __eq__(self,other):
        if self._days() ==  other._days():
            return True
        return False

    #计算两个日期之间的天数，用减法
    def __sub__(self,other):
        return self._days()-other._days() 
    
    #计算今天是周几
    def weekday(self):
        w = self._days() % 7
        return w

def main():
    d = Date(2001,11,10)
    d1 = Date(1900,12,10)
    print(days(d.year,d.month,d.day))
    print(leapYears(d1.year,d.year))
    print(d1<d)
    print(d1>d)
    d0 = d
    print(d==d0)
    print(d-d1)
    print(d.weekday())
    print(d1.weekday())

if __name__=='__main__':
    main()
