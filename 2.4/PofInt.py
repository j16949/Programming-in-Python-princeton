#判断是否是素数
def prime(a):
	if len(factors(a)) == 2:
		return True
	else:
		return False

#判断是否互质
def relativelyPrime(a,b):
	fa = factors(a)
	if len(fa) > 0:
		fa.remove(1)
	fb = factors(b)
	if len(fb) > 0:
		fb.remove(1)
	for s in fa:
		if s in fb:
			return False
	return True

#求所有因子
def factors(a):
	b = []
	for i in range(1,a+1):
		t = a % i
		if t == 0:
			b.append(i)
	return b

#最大公约数&最小公倍数
def GCdivisorandLCmultiple(a,b):
	return d,m

#欧拉函数
def euler(a):
	return l

def main():
	f = 73
	p = 73
	r1,r2 = 73,71
	print('factors('+str(f)+'):',factors(f))
	print(str(p)+'是否是质数:',prime(p))
	print(str(r1)+'和'+str(r2)+'是否互质:',relativelyPrime(r1,r2))

if __name__ == '__main__':
	main()
