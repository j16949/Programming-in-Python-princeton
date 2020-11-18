#Voting machine

import stdrandom

def vote(n,p,w):
	n1 = stdrandom.binomial(n,1-w)	#n次投票，不错误的次数为n1
	na = stdrandom.binomial(n1,p)+stdrandom.binomial(n-n1,1-p)	#正常的N1次p概率投给A；错误的N-N1次，票数记反，相当于A，B概率对调。返回na为A获得的票数
	print('A获得：',na)
	if na > n/2:
		return 'A获胜'
	else:
		return 'A失败'

n = 10000000	#投票次数
p = 0.51		#竞选者A获得票数的概率
w = 0.49		#投票及错误率
print(vote(n,p,w))
