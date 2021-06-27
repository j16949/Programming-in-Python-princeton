from stopwatch import Stopwatch

def harmonic(n):
    total = 0.0
    for i in range(1, n+1):
        total += 1.0 / float(i)
    return total

def recuHarmonic(n):
    if n == 1:
        return 1
    else:
        return 1/n + recuHarmonic(n-1)


def main():
    n = 777
    w1 = Stopwatch()
    print(harmonic(n))
    print(w1.elapsedTime())
    w2 = Stopwatch()
    print(recuHarmonic(n))
    print(w2.elapsedTime())

if __name__ == '__main__':
    main()
