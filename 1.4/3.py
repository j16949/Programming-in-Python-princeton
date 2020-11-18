ls=[1,2,3,4,5,6]
#ls.reverse()
for i in range(len(ls)//2):
	t=ls[i]
	ls[i]=ls[len(ls)-1-i]
	ls[len(ls)-1-i]=t
	print(ls)
print(ls)
