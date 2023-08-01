#Polynomials. Develop a data type for univariate polynomials with integer coefficients, such as x3 + 5x2 + 3x + 7. Include methods for standard operations on polynomials such as addition, subtraction, multiplication, degree, evaluation, composition, differentiation, definite integration, and testing equality.
#标准解法请参考https://python-course.eu/oop/polynomial-class.php
#只实现了str,加法，减法，乘法。其他方法次数即为多个乘法，求值理解为__call__(),排列和比较不做，微分和定积分估计可以参考matlab或者sage


class Polynomial:
    
    #数组从小到大对应多项式从n-1次方到0次方
    def __init__(self,n,a):
        self._a = tuple(a)  #tuple防更改
        self._n = n

    '''
    #这个str存在比较运算，在复数情况下无法比较，改用网上学习的办法
    def __str__(self):
        s =''
        for i in range(self._n-1,1,-1):            
            if self._a[i] > 0:
                if self._a[i]!=1:
                    s += '+' + str(self._a[i])+'x'+'^'+str(i)
                else:
                    s += '+' + 'x'+'^'+str(i)
            elif self._a[i] < 0:
                if self._a[i]!=-1:
                    s += str(self._a[i])+'x'+'^'+str(i)
                else:
                    s += '-' + 'x'+'^'+str(i)
        #一次方不加'^‘,即i==1的情况
        if self._n > 1:
            i = 1 
            if self._a[i] > 0:
                if self._a[i]!=1:
                    s += '+' + str(self._a[i])+'x'
                else:
                    s += '+' + 'x'
            elif self._a[i] < 0:
                if self._a[i]!=-1:
                    s += str(self._a[i])+'x'
                else:
                    s += '-' + 'x'
        if self._a[0]!=0:
            if self._a[0]>0:
                s += '+' + str(self._a[0])
            else:
                s += str(self._a[0])
        if s[0] == '+':
            s = s[1:]
        return s  #从大到小输出
    '''

    def __str__(self):

        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^"+str(degree)
            return res

        degree = self._n - 1
        res = ""

        #for i in range(0, degree+1):
        for i in range(degree,-1,-1):
            coeff = self._a[i]
            # nothing has to be done if coeff is 0:
            if abs(coeff) == 1 and i > 0:
                # 1 in front of x shouldn't occur, e.g. x instead of 1x
                # but we need the plus or minus sign:
                res += f"{'+' if coeff>0 else '-'}{x_expr(i)}"  
            elif isinstance(coeff,complex):
                res += f"+({coeff:g}){x_expr(i)}"
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(i)}" 

        return res.lstrip('+')    # removing leading '+'
    
    def __call__(self,x):
        res = 0
        for i in range(self._n):
            res += self._a[i]*x**i
        return res

    def __add__(self,other):
        if self._n < other._n:
            n = self._n
            p = list(other._a)
        else:
            n = other._n
            p = list(self._a)
        for i in range(n):
            p[i] = self._a[i] + other._a[i]
        return Polynomial(len(p),p)

    #减法有顺序，加法没顺序，没法直接用
    def __sub__(self,other):
        if self._n < other._n:
            n = other._n
            ps = list(self._a) + list(0 for i in range(other._n-self._n))  #补齐数组
            po = list(other._a)
        else:
            n = self._n
            ps = list(self._a)
            po = list(other._a) + list(0 for i in range(self._n-other._n))  #补齐数组
        for i in range(n):
            ps[i] -= po[i]
        return Polynomial(len(ps),ps)

    #对齐数组工具方法
    def toSameLen(self,other):
        if self._n < other._n:
            n = other._n
            ps = list(self._a) + list(0 for i in range(other._n-self._n))  #补齐数组
            po = list(other._a)
        else:
            n = self._n
            ps = list(self._a)
            po = list(other._a) + list(0 for i in range(self._n-other._n))  #补齐数组
        return n,ps,po

    #写乘法时发现要对齐数组，其实这部分在加法和减法中可以公用，先写工具方法toSameLen()
    #可以转化为矩阵和向量运算https://zhuanlan.zhihu.com/p/58665745
    #此处还是笨办法，存在一个二维数组里
    #经过尝试，上述方法此处可以实现，因为已经转化为方阵
    def __mul__(self,other):

        #方阵斜相加工具方法：
        def addLine(low,high,p):
            res = 0
            i = low
            j = high
            while i <= high and j >= low:
                res += p[i][j]
                i += 1
                j -= 1
            return res

        #最高次方等于两个多项式最高次项质数相加，此处有本质的错误，万一数组里填写了0呢？
        #而且h这个变量没用，所以取消
        #h = (self._n-1)+(other._n-1)
        n,ps,po = self.toSameLen(other)
        #p为计算过程中的方阵
        p = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                p[i][j]=ps[i]*po[j]
        #pr = [0 for i in range(h+1)]
        #控制方阵斜相加次数h+1
        #for x in range(h+1):
        pr = list()
        #先将第一行斜向下加完
        for i in range(n):
            t = addLine(0,i,p)
            pr.append(t)
        #在将剩余每行最后一个数所处的斜线相加
        for i in range(1,n):
            t = addLine(i,n-1,p)
            pr.append(t)
        #去除最高次位为0,不去除出现系数是0的不合理
        while pr[-1] == 0:
            pr=pr[:-1]
        #测试判断是否次数错误
        #assert h+1 == len(pr)  
        return Polynomial(len(pr),pr)
            
def main():
    a = [1,2,-3,4,10]
    b = [3,2,3,-3]
    p = Polynomial(len(a),a)
    q = Polynomial(len(b),b)
    m = p+q
    print(m)
    n = q-p
    print(n)
    print(p*q)
    print(q(2))
    c = Polynomial(3,[1,1,1])
    d = Polynomial(3,[1,2,0])
    print(c*d)
    
    print('-----------以下是numpy计算结果，用来验证---------------')
    import numpy as np
    #np数组次方为由大到小，相反
    pn = np.poly1d(a[::-1])
    qn = np.poly1d([0,-3,3,2,3]) #b不仅相反，逻辑不同，还得补0
    print(pn+qn)
    print(qn-pn)
    print(pn*qn)
    print(qn(2))
    

if __name__ == '__main__':
    main()

