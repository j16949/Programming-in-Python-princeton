import sys
s=sys.argv[1]
sums=0
for i in range(10,1,-1):
    sums+=i*eval(s[10-i])
for j in range(11):
    if (sums+j)%11==0:
        if j==10:
            s+='x'
        else:    
            s+=str(j)
print(s)
