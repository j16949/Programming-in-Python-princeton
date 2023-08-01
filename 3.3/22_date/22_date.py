#22. 日期（ Date）。 请 开发 一个 API， 用于 日期（ 年、 月、 日）。 请 包含 比较 两个 日期 的 方法， 包括 计算 两个 日期 之间 的 天数 差， 确定 给定 日期 的 星期， 以及 其他 你 认为 客户 端 可能 需要 的 方法。 设计 好 API 后， 请与 Python 的 datetime. date 数据 类型 进行 比较。
#Dates. Develop an API for dates (year, month, day). Include methods for comparing two dates chronologically, computing the number of days between two dates, determining the day of the week of a given date, and any other operations that you think a client might want. After you have designed your API, look at the Python's datetime.date data type.
#如果不参照time，也就是说time以1970-1-1 00:00:00为基准，如果date不以最小单位day为基准进行计算，弊端1：需要设计daysSpent(),daysLeft()
#daysInMonth(),daysBeforeMonth();弊端2：不能直接用两数相减，还得判断大小isEarlier(),用__lt__();

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

#判断两个年份间闰年的数量
#这个函数想法不对，闰不闰关键在于是否过了二月，过了二月加一天，应该计算leapdays(date1,date2)
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
    
    #判断时间前后顺序，以便计算
    def isEarlier(self,other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    #<
    def __lt__(self,other):
        return self.isEarlier(other)

    #计算两个日期之间的天数，用减法
    def __sub__(self,other):
        #弊端3，大小顺序不对，带来额外开销
        if self < other:
            d1 = self
            d2 = other
        else:
            d1 = other
            d2 = self
        days = 0
        #弊端4，判断条件情况复杂,如果是同一年
        if d2.year - d1.year == 0:
            for i in range(d2.month):
                pass
            #太复杂了，月份还得考虑具体情况，还是统一单位，即按日来做比较好，不往下写了
    


def main():
    d = Date(2001,11,10)
    d1 = Date(1900,12,10)
    print(leapYears(d1.year,d.year))
    print(d1<d)

if __name__=='__main__':
    main()
