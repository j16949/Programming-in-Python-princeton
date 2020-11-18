#data
array=[0,1,2,3,3,3,2,1,2,2,0,5,5,5,5,6,6,6,6,6,2,1]
ts=[]
start,end,i=0,0,0
while i<len(array)-1:
	if array[i]<array[i+1]:
		i+=1
		start=i
		while array[i]==array[i+1]:
			i+=1
		if array[i]>array[i+1]:
			end=i
			if end-start>len(ts):
				ts=array[start:end+1]
	else:
		i+=1
print(ts)
