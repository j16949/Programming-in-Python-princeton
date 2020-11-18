import random
n=10000
re,nore=0,0
def reChooes():
	ls=[1,2,3]
	bingo=0					#bingo代表是否成功
	prize=random.randint(1,3)
	ls.remove(prize)
	ts=list(ls)
	firstChoose=random.randint(1,3)
	if firstChoose != prize:
		bingo=1
	return bingo

def noReChoose():
	ls=[1,2,3]
	bingo=0					#bingo代表是否成功
	prize=random.randint(1,3)
	ls.remove(prize)
	ts=list(ls)
	firstChoose=random.randint(1,3)
	if firstChoose == prize:
		bingo=1
	return bingo

for i in range(n):
	re+=reChooes()
	nore+=noReChoose()

print('reChoose:',re/n)
print('noreChoose:',nore/n)
