#Rumor 用程序告诉你，什么叫一传十，十传百

import random
n=eval(input('请输入参加聚会的总人数:'))
m=10
total=0
for i in range(m):
	s=0
	#False代表不知道谣言，列表第一个代表当事人(Alice),第二个代表谣言制造者(Bob)
	ls=[ False for i in range(n)]
	ls[0],ls[1]=True,True
	#第一次传播
	x=random.randrange(2,n)
	ls[x]=True
	ls[2],ls[x]=ls[x],ls[2]
	while True:
		#第二个位置用于记录此次传播谣言的人,第三个位置记录此次得知谣言并下次进行传播的人
		x=random.randrange(3,n)
		if not ls[x]:
			ls[x]=True
			ls[2],ls[x]=ls[x],ls[2]
		else:
			break
	for t in ls[2:]:
		if t==True:
			s+=1
	if s>=(n-2):
		total+=1
	print('听到谣言人数:',s)

print('所有人都听到的概率',total/m)
