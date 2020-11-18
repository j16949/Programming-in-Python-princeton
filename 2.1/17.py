import random
import sys

def choose(deck,n):
	for j in range(eval(n)):
		perm = list(deck)
		for i in range(5):
			r = random.randrange(i,52)
			temp = perm[r]
			perm[r] = perm[i]
			perm[i] = temp
		for i in range(5):
			print(perm[i])
		print()
	return


#初始化52张扑克牌
Suits = ['Clubs','Diamonds','Hearts','Spades']
Ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
deck = []
for rank in Ranks:
	for suit in Suits:
		card = rank + 'of' + suit
		deck += [card]

#输出n手牌
n=sys.argv[1]
choose(deck,n)
