import datetime

class Appointment:
    
    def __init__(self,date,contact):
        if type(date) != datetime.date:
            raise Exception('输入格式错误')
        self._date = date
        self._contact = contact

    def getDate(self):
        return self._date

def main():
    d1 = datetime.date(2022,6,28)
    a1 = Appointment(d1,'eating')
    print(a1.getDate())

if __name__ == '__main__':
    main()
