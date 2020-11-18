import random
import sys

n=eval(sys.argv[1])
m=eval(sys.argv[2])

#初始化二维数组
l=[[0 for i in range(n)] for j in range(n)]

#生成随机数填入数组
for i in range(m):
    a = random.randrange(n)
    b = random.randrange(n)
    while b == a:
           b = random.randrange(n) 
    l[a][b] += 1

#按格式输出
print(n)
for i in range(n):
    for j in range(n):
        for t in range(l[i][j]):
            print(str(i)+' '+str(j),end='  ')
    print()

    
