#请 编写 一个 函数 fibonacci()， 带 一个 整数 型 参数 n， 并 计算 第 n 个 斐 波 那 契 数。 请使用 元 组 的 组 包 和解 包 功能。
#fibonacci 1 1 2 3 5 8

import sys

#递归,效率不优，应参考使用动态编程
def fibonacci(n):
    '''
    if n == 1 or n == 2:
        return 1
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#非递归，用list存储
'''
def fibonacciL(n):
    t,t1,t2 = 0,1,1
    l=[0,t1,t2]
    for i in range(3,n+1):
        t = t1+t2
        l.append(t)
        t1 = t2
        t2 = t
    return l[n]
'''
def fibonacciL(n):
    l=[0,1]
    for i in range(2,n+1):
        l.append(l[i-1] + l[i-2])
    return l[n]

#题目是计算第n个fibonacci数，用到tuple组包和解包
def nthofFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n-1):
#            print('before (a,b):',a,b)
            a,b = b,a+b
#            print('after (a,b):',a,b)
        return b

def main():
    n = eval(sys.argv[1])
    # n = 3
    l1 = []
    l2 = []
    for i in range(0,n+1):
        l1.append(fibonacci(i))
        l2.append(fibonacciL(i))
    print(l1)
    print(l2)
    print(nthofFibonacci(n))

if __name__ == '__main__':
    main()
