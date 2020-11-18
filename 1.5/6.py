
s=input('Please input a list:')
ls=s.split(' ')
fs=[]
ts=list(ls)
for i in range(len(ls)-2,-1,-1):
	if ls[i+1]==ls[i]:
		del ls[i]
	'''else:
		if len(ts)>len(fs):
			fs=list(ts)
		ts=[]

fs.append(fs[0])		
print(fs)'''
print(ls)
