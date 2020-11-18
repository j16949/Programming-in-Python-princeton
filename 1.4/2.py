a=[1,2,3]
b=[2,3,4]
t=0
for i in range(len(a)):
	t+=(a[i]-b[i])**2
print(t**0.5)
