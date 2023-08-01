#测试在一个类的构造函数里传入list
import copy

class ListCopy:
    
    def __init__(self,l):
        self._l = l[:]

    def __str__(self):
        return str(self._l)

def main():
    l = [[[0,1],1],2,3]
    lc = ListCopy(l)
    print(lc)
    l.append(4)
    print(lc)
    l[0][0][0] = 'x'
    print(lc)
    print(l)

if __name__ == '__main__':
    main()
