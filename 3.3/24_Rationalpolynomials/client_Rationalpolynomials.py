from polynomial import Polynomial
from rational import Rational
from fractions import Fraction

#系数为int
a=[-1,2,3,-4]
p1 = Polynomial(len(a),a)
print(p1)

#系数为float
b=[-1.1,2.9,.3,-4]
p2 = Polynomial(len(b),b)
print(p2)

#系数为complex
c=[complex(1,2),complex(-.5,3),0,complex(1/3,-7)]
p3 = Polynomial(len(c),c)
print(p3)   #print时发现int无法和complex类型比较，回想作者之前在解决complex类型系数的Vector时，用了(int,float,complex).conjugate,即求共轭后再做乘法，此处并不适用
            #补习了一下数学,发现复数在数学意义上无法比较大小，因为没有意义，比较模的大小可以。考虑__str__是否有更好的写法

#系数为自定义的Rational
#d=[Rational(1,2),Rational(-5,10),Rational(.1,3),0] #rationl或者eculid有问题，小数显示有问题
d=[Rational(1,2),Rational(-5,10),Rational(1,3),0]
p4 = Polynomial(len(d),d)
print(p4)   #提示unsupported format string passed to Rational.__format__，在rational中增加__format__方法

#系数为python自带的分数
d1=[Fraction(1,2),Fraction(-5,10),Fraction(1,3),0]
p5 = Polynomial(len(d1),d1)
#print(p5)   #提示unsupported format string passed to Fraction.__format__，看来python自带的分数也没实现__format__,这就不好写了，改写polynomial的__str__()工程量略大
print()

#__call__
print('-----------------__call__---------------------')
print(p1(2))
print(p2(2))
print(p3(2))
print(p4(2))
print(p5(2))
print()

#__add__
print('-----------------__add__---------------------')
print(p1+p2)
print(p1+p3)
print(p4+p1)   #如果改写成p1+p4，则需要实现int和Rational相加的方法,得改写python原生类int的i__add__！！！！
               #不知道如何实现，所以可能自定义的类重写一些基本方法很难与原生类融合
print(p2+p5)
print()

#__sub__
print('-----------------__sub__---------------------')
print(p1-p2)
print(p1-p3)
print(p4-p1)   #如果改写成p1-p4，则需要实现int和Rational相加的方法,得改写python原生类int的i__add__！！！！
               #不知道如何实现，所以可能自定义的类重写一些基本方法很难与原生类融合
print(p2-p5)
print()

#__mul__
print('-----------------__mul__---------------------')
print(p1*p2)
print(p1*p3)
print(p4*p1)   #如果改写成p1*p4，则需要实现int和Rational相加的方法,得改写python原生类int的i__add__！！！！
               #不知道如何实现，所以可能自定义的类重写一些基本方法很难与原生类融合
print(p2*p5)
print()

