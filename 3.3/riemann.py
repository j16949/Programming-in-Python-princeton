import gaussian

def integrate(f, a, b, n=1000):
    total = 0.0
    dt = 1.0 * (b - a) / n
    for i in range(n):
        total += dt * f(a + (i + 0.5) * dt)
    return total

def main():
    r = integrate(gaussian.pdf,-1,1)
    print('riemann:',r)
    c = gaussian.cdf(1)-gaussian.cdf(-1)
    print('gauss:',c)

if __name__ == '__main__':
    main()
