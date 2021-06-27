import estimatev
import data
import stddraw

def main():
    n = 40
    p = .85
    trials = 100
    d = data.Data(n)
    for i in range(n):
        d.addDataPoint(i,estimatev.evaluate(i,p,trials))
    print(d._l)
    
    d.plot()
    d.plotTukey()
    stddraw.show()

if __name__=='__main__':
    main()
