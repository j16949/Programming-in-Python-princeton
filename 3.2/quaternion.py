import math

class Quaternion:
    
    def __init__(self,a = []):
        self._a = [0 for i in range(4)]
        if a:
            for i in range(4):
                self._a[i]=a[i]
    
    def __add__(self,other):
        c = Quaternion()
        for i in range(4):
            c._a[i] = self._a[i] + other._a[i]
        return c

    def __mul__(self,other):
        c = Quaternion()
        c._a[0] = self._a[0] * other._a[0] - self._a[1] * other._a[1] - self._a[2] * other._a[2] - self._a[3] * other._a[3] 
        c._a[1] = self._a[0] * other._a[0] - self._a[1] * other._a[1] + self._a[2] * other._a[2] - self._a[3] * other._a[3] 
        c._a[2] = self._a[0] * other._a[0] - self._a[1] * other._a[1] + self._a[2] * other._a[2] + self._a[3] * other._a[3] 
        c._a[3] = self._a[0] * other._a[0] + self._a[1] * other._a[1] - self._a[2] * other._a[2] + self._a[3] * other._a[3] 
        return c

    def __abs__(self):
        temp = 0
        for i in range(4):
            temp += self._a[i]*self._a[i]
        return math.sqrt(temp)

    def conjugate(self):
        ac = [self._a[0],-self._a[1],-self._a[2],-self._a[3]]
        return Quaternion(ac)
    
    def inverse(self):
        ai = []
        ac = self.conjugate()
        for i in range(4):
            ai.append(ac._a[i]/abs(self))
        return Quaternion(ai)

    def __truediv__(self,other):
        return self*other.inverse()

    def __str__(self):
        return (str(self._a))

def main():
    a = [1,2,3,4]
    qa = Quaternion(a)
    b = [2,3,4,5]
    qb = Quaternion(b)
    qc = qa+qb
    print('add:',qc)
    print('abs:',abs(qa))
    print('conjugate:',qa.conjugate())
    print('inverse:',qa.inverse())
    print('mul:',qa*qb)
    print('div:',qb/qa)

if __name__=='__main__':
    main()
