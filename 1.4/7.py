n = 10
a = [0, 1]
for i in range(2, n):
    a += [a[i-1] + a[i-2]]
print(a)

