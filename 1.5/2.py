
s=input('Please input numbers devide by \'\,\':')
ls=s.split(',')
ts=[]
for t in ls:
	tv=eval(t)
	if tv > 0 and tv%1==0:
		ts.append(tv)
	else:
		print('Please input positive integers')
		break
if len(ts)==len(ls):
	print('max=',max(ts))
	print('min=',min(ts))
