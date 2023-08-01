from appointment import Appointment
from datetime import date

class Calendar:
    
    def __init__(self):
        self._d = dict()

    def confilct(self,a):
        if a.getDate() in self._d:
            return True
        return False
    
    def addAppointment(self,a):
        if a.getDate().weekday() == 5 or a.getDate().weekday() == 6:
            raise Exception('周六日不约')
            
        if self.confilct(a):
            raise Exception('约会冲突')
            
        self._d[a.getDate()] = a._contact

def main():
    a = Appointment(date.today(),'nihao')
    c = Calendar()
    c.addAppointment(a)
    # c.addAppointment(2)

if __name__=='__main__':
    main()
