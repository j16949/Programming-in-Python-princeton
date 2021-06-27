
class Entry:
    
    def __init__(self,date,openPrice,high,low,closePrice):
        self._date = date
        self._openPrice = openPrice
        self._high = high
        self._low = low
        self._closePrice = closePrice

    def __str__(self):
        return  self._date + ' ' + self._openPrice + ' ' + self._high + ' ' + self._low + ' ' + self._closePrice

def main():
    e = Entry('20210515','100','120','90','101')
    print(e)

if __name__=='__main__':
    main()
