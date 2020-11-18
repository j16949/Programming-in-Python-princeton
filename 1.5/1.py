s=input('Please input numbers(devide by \'\,\':')
ls=s.split(',')
ts=[]
for t in ls:
	ts.append(eval(t))
print('max=',max(ts))
print('min=',min(ts))
