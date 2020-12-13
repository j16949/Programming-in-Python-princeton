def ex234(n):
    if n <= 0:
        return ''
    return ex234(n-3) + str(n) + ex234(n-2) + str(n)

print(ex234(6))

#311361142246

