from vectorComplex import Vector
import stdio

def main():

    xCoords = [1/3, 3/7, 2/5, 1/11]
    yCoords = [5.0, 2.0, 4.0, 1.0]

    x = Vector(xCoords)
    y = Vector(yCoords)

    stdio.writeln('x        = ' + str(x))
    stdio.writeln('y        = ' + str(y))
    stdio.writeln('x + y    = ' + str(x + y))
    stdio.writeln('10x      = ' + str(x.scale(10.0)))
    stdio.writeln('|x|      = ' + str(abs(x)))
    stdio.writeln('<x, y>   = ' + str(x.dot(y)))
    stdio.writeln('|x - y|  = ' + str(abs(x - y)))

if __name__ == '__main__':
    main()

