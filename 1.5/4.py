
import sys
n=eval(sys.argv[1])
ls=[]
for i in range(n):
	t=input('Please input a number:')
	ls.append(eval(t))
avg=sum(ls)/n
suml=0
for t in ls:
	suml+=(t-avg)**2
standDe=suml**0.5/(n-1)
print(avg,standDe)
ls2=[]
for t in ls:
	if t-avg >= 1.5*standDe:
		ls2.append(t)
print(ls2)
