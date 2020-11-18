import sys
# op=[]
# for i in range(1,4):
# 	op.append(eval(sys.argv[i]))
op=[1,5,2]
print('Please input point,"q" to exit:')
p=[]
t=input().split(' ')
while t[0] != 'q':
	p.append(t)
	t=input().split(' ')
for t in p:
	t[0],t[1],t[2]=eval(t[0]),eval(t[1]),eval(t[2])
l=(p[0][0]-op[0])**2+(p[0][1]-op[1])**2+(p[0][2]-op[2])**2
for q in p:
	t=(q[0]-op[0])**2+(q[1]-op[1])**2+(q[2]-op[2])**2
	if t < l:
		l=t
		res=q
print(res)

