s=input('Please input a list:')
ls=s.split(' ')
fs=[]
ts=[]
for i in range(1,len(ls)):
	if ls[i-1]==ls[i]:
		ts.append(ls[i])
	else:
		if len(ts)>len(fs):
			fs=list(ts)
		ts=[]

fs.append(fs[0])		
print(fs)
