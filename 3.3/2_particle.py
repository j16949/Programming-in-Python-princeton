from vector import Vector

class Particle:
    
    def __init__(self,p,m,v):
        self.__position = p
        self.__mass = m
        self.__velocity = v

    def kineticEnergy(self):
        return .5*self.__mass*self.__velocity.dot(self.__velocity)

def main():
    p = Vector((1,2,1))
    v = Vector((3,5,2))
    par = Particle(p,10,v)
    print(par.kineticEnergy())

if __name__ == '__main__':
    main()
