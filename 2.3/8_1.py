#coding:utf-8
# mystery()返回结果为a**b
# 仅可在python2中运行,python3会报错递归深度
# 因为在python2中:
# >>> 3.0/2
# 1.5
# >>> 3/2
# 1
# >>> 
# 在python3中：
# >>> 3/2
# 1.5


def mystery(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return mystery(a*a, b/2)
    return mystery(a*a, b/2) * a

print(mystery(2,8))
#print(mystery(3,8))
