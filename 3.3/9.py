#Prove that the dot product of two two-dimensional unit-vectors is the cosine of the angle between them.
#证明两个二维单位向量的点积是夹角的余弦值。

from vector2D import Vector2D
import math

a = Vector2D(1,2)
b = Vector2D(5,2)
ua = a.direction()
ub = b.direction()

print(ua)
print(ub)

#证明需要通过余弦定理
#余弦定理 |c|**2=|a|**2+|b|**2-2*|a|*|b|*cos(tha)
#从向量的加减法 c=a-b 所以|c|**2=|a|**2+|b|**2-2*a.dot(b)
#所以 a.dot(b) == |a|*|b|*cos(tha),有因为a,b为单位向量，所以|a|=|b|=1,即a.dot(b)==cos(tha)
#参考https://zhuanlan.zhihu.com/p/66674587

#验证
#即cos(tha)=-(|c|**2-|a|**2-|b|**2)/(2*|a|*|b|)
xc = ua - ub
print('abs(xc):',abs(xc))
print('ua.dot(ub):',ua.dot(ub))
print('cos(tha):',-(xc**2-ua**2-ub**2)/(2*abs(ua)*abs(ub)))

