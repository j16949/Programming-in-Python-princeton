

class Element:
    
    def __init__(self, elementName, atomicNumber,symbol,atomicWeight):
        self._elementName = elementName
        self._atomicNumber = atomicNumber
        self._symbol = symbol
        self._atomicWeight = atomicWeight

    def getName(self):
        return self._elementName

    def getNumber(self):
        return self._atomicNumber

    def getSymbol(self):
        return self._symbol

    def getWeight(self):
        return self._atomicWeight
    
    def __str__(self):
        return self.getName()+' '+str(self.getNumber())+' '+self.getSymbol()+' '+str(self.getWeight())


def main():
    e = Element('Hydrogen',1,'H',1.01)
    print(e)
   
if __name__ == '__main__':
    main()

#Element,Number,Symbol,Weight,Boil,Melt,Density Vapour,Fusion,
#Hydrogen,1,H,1.01,20.46,13.96,71,0.45,0.06,

