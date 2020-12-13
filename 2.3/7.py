def gcdlike(p, q):
    if q == 0:
        return p == 1
    return gcdlike(q, p % q)

#判断p,q是否互质
