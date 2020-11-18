import stddraw

#设置条形码数组
a = [0]*10
a[0] = [2,2,1,1,1]
a[1] = [1,1,1,2,2]
a[2] = [1,1,2,1,2]
a[3] = [1,1,2,2,1]
a[4] = [1,2,1,1,2]
a[5] = [1,2,1,2,1]
a[6] = [1,2,2,1,1]
a[7] = [2,1,1,1,2]
a[8] = [2,1,1,2,1]
a[9] = [2,1,2,1,1]


#绘制一个条形码
def drawbc(x,l):
	for k in range(len(l)):
		stddraw.filledRectangle(k+x,0,0.5,l[k])

#绘制多个条形码
def drawbcs(p):
	stddraw.setXscale(-1,100)
	stddraw.setYscale(0,5)
	x = 1
	stddraw.filledRectangle(0,0,0.5,2)	#左护栏
	for t in p:
		print(t)
		drawbc(x,t)
		x += 5
	stddraw.filledRectangle(x,0,0.5,2)	#右护栏
	stddraw.show()

#将十进制数字转换为数组
def numtolist(n):
	l = []
	while n // 10 > 0:
		l.append(n%10)
		n = n // 10
	l.append(n)
	l.reverse()
	return l


#将数组对应到a[],即对应到条形码
def ltobarcode(l,a):
	b = []
	for i in range(len(l)):
		for j in range(len(a)):
			if l[i] == j:
				b.append(a[j])
	return b

#添加数组校验位
def stobarcode(l,a):
	print('bl:',l)
	l.append(sum(l) % 10)
	print('al:',l)
	return ltobarcode(l,a)

s = input('请输入条形码数字:')
drawbcs(stobarcode(numtolist(eval(s)),a))

