import sys
s=sys.argv[1]
sc = s[9]
if sc == 'x':
    sc = 10
s=s[:9]
sums=0
for i in range(10,1,-1):
    sums+=i*eval(s[10-i])
if (sums + eval(sc))%11 == 0:
    print(True)
else:
    print(False)
'''
for j in range(11):
    if (sums+j)%11==0:
        if j==10:
            s+='x'
        else:    
            s+=str(j)
print(s)
'''

#bai@ubuntu:~/pythonProject/princeton/3.1$ python3 12.py 020131452
#0201314525

