#梭哈(五张牌)___不用类
import stdrandom
import stdstats
import random
import stddraw
from scipy.special import perm,comb 

#定义扑克牌：0-12，红桃；13-25，黑桃；26-38，方块；39-51，梅花。
#由于抽出不放回，将52个数字存入数组
def deck():
	a = []
	for i in range(52):
		a.append(i)
	return a

#抽取n张牌不放回
def popdeck(a,n):
	p = []
	for i in range(n):
		p.append(a.pop(random.randrange(len(a))))
	return p

#返回一张扑克花色，0红桃；1黑桃；2方块；3梅花
def deckColor(d):
	return d//13

#返回一张扑克牌面数值，0-12对应A23...JQK
def deckNum(d):
	return d%13

#返回一组扑克牌面
def numofGroupDeck(p):
	num = []
	for s in p:
		num.append(deckNum(s))
	return num

#返回一组扑克花色
def colorofGroupDeck(p):
	color = []
	for s in p:
		color.append(deckColor(s))
	return color

'''
#返回这组牌中有几对
def pair(p):
	num = numofGroupDeck(p)
	l = len(num)
	num.sort()
	t = 0	#统计有几对相同
	i = 0
	while i < l-1:
		if num[i] == num[i+1]:
			if i+2 < l:
				if num[i+1] != num[i+2]:
					t += 1
					i += 1
				else:
					#3个一样则i+2
					#4个一样则i+3
			else:
				t += 1
				i += 1
		i += 1
	return t
'''

#返回这组牌中有几对
def pair(p):
	num = numofGroupDeck(p)
	l = len(num)
	num.sort()
	rc = []	#rc用来存储对子和三条
	i = 0
	while i < l-1:
		c = 0
		while i < l-1 and num[i] == num[i+1]:
			c += 1
			i += 1
		if c != 0:
			rc.append(c)
		i += 1
	return rc

#判断是否只有一对
def onePair(r):
	if r == [1] :
		return True
	else:
		return False

#判断是否有两对
def twoPair(r):
	if r == [1,1] :
		return True
	else:
		return False

#判断是否属于三条
def threeofAkind(r):
	if r == [2]:
		return True
	else:
		return False

#判断是否满堂红
def fullHouse(r):
	if r == [2,1] or r == [1,2]:
		return True
	else:
		return False

#判断是否同花
def flushColor(c):
	r = 0
	for i in range(len(c)-1):
		if c[i] == c[i+1]:
			r += 1
	if r == 4:
		return True
	else:
		return False

#判断是否顺子
def straight(num):
	l = len(num)
	num.sort()
	r = 0
	for i in range(l-1):
		if num[i] == num[i+1]-1:
			r += 1
	if r == 4:
		return True
	else:
		return False

#判断同花顺
def straightFlush(c,num):
	if straight(num) and flushColor(c):
		return True
	else:
		return False



def main():
	#print(deck())
	a = deck()
	#b = popdeck(a,5)
	b = [16,2,4,1,0]
	r = pair(b)	#获得对数或三条数
	num = numofGroupDeck(b)	#获得牌面数字
	c = colorofGroupDeck(b)	#获得花色
	print('牌:',b)
	print('牌面数字:',num)
	print('花色:',c)
	print('一对:',onePair(r))
	print('两对:',twoPair(r))
	print('三条:',threeofAkind(r))
	print('满堂红:',fullHouse(r))
	print('同花:',flushColor(c))
	print('顺子:',straight(num))
	print('同花顺:',straightFlush(c,num))
	#统计各种情况出现概率
	n = 100000	#试验次数
	p = [0]*7	#记录各种情况结果
	for i in range(n):
		a = deck()
		b = popdeck(a,5)
		r = pair(b)
		num = numofGroupDeck(b)
		c = colorofGroupDeck(b)
		if onePair(r):
			p[0] += 1
		elif twoPair(r):
			p[1] += 1
		elif threeofAkind(r):
			p[2] += 1
		elif fullHouse(r):
			p[3] += 1
		if straightFlush(c,num):
			p[6] += 1
		elif flushColor(c):
			p[4] += 1
		elif straight(num):
			p[5] += 1
	print('p:',p)
	stddraw.setYscale(0,1.1*max(p))
	stdstats.plotBars(p)
	
	#使用数学公式验证,先选牌面数字，再选花色
	q = [0]*7
	q[0] = comb(13,1)*comb(4,2)*comb(12,3)*comb(4,1)**3/(comb(52,5))
	q[1] = comb(13,2)*comb(4,2)**2*comb(11,1)*comb(4,1)/(comb(52,5))
	q[2] = comb(13,1)*comb(4,3)*comb(12,2)*comb(4,1)**2/(comb(52,5))
	q[3] = comb(13,1)*comb(4,3)*comb(12,1)*comb(4,2)/(comb(52,5))
	flush = comb(13,5)*comb(4,1)/(comb(52,5))
	Straight = 9*comb(4,1)**5/(comb(52,5))
	q[6] = flush*Straight
	q[4] = flush-q[6]
	q[5] = Straight-q[6]
	for i in range(len(q)):
		print('q[i]:{:.4f}'.format(q[i]))

	stddraw.show()

if __name__ == '__main__':
    main()


'''
bai@ubuntu:~/pythonProject/princeton/2.2$ python3 24.py
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
牌: [16, 2, 4, 1, 0]
牌面数字: [3, 2, 4, 1, 0]
花色: [1, 0, 0, 0, 0]
一对: False
两对: False
三条: False
满堂红: False
同花: False
顺子: True
同花顺: False
p: [42107, 4702, 2112, 132, 196, 359, 0]
q[i]:0.4226
q[i]:0.0475
q[i]:0.0211
q[i]:0.0014
q[i]:0.0020
q[i]:0.0035
q[i]:0.0000
'''
