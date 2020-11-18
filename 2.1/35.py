import sys

def leapyear(y):
	if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
		return True
	else:
		return False

def calendar(m,y):
	#计算y年m月1日是周几，用d0表示
	y0 = y-(14-m)//12
	x = y0+y0//4-y0//100+y0//400
	m0 = m+12*((14-m)//12)-2
	d0 = (1+x+31*m0//12)%7
	#输出表头m月y年
	print('{0:^9}{1:^6}'.format(m,y))
	#输出表头周几
	week =['S','M','Tu','W','Th','F','S']
	for i in range(len(week)):
		tplt = '{0['+str(i)+']:^3}'
		print(tplt.format(week),end='')
	print()
	#输出calendar
	day = 31
	if m == 4 or m == 6 or m == 9 or m == 11:
		day = 30
	elif m == 2:
		if leapyear(y):
			day = 29
		else:
			day = 28
	#输出第一周
	print('   '*d0,end='')
	i = 1
	while i <= 7-d0:
		print('{0:^3}'.format(i),end='')
		i += 1
	print()
	#输出其他周
	while i <= day:
		for j in range(7):
			if i > day:
				break
			print('{0:^3}'.format(i),end='')
			i += 1
		print()

m = eval(sys.argv[1])
y = eval(sys.argv[2])
calendar(m,y)
#calendar(2,2000)
