import random
n=3
suits=['Clubs','Diamonds','Hearts','Spades']
ranks=[ str(i) for i in range(2,11) ]+['Jack','Queen','King','Ace']
#init deck
deck=list()
for x in suits:
	for y in ranks:
		deck.append( y+'of'+x )
#print(deck)
random.shuffle(deck)
for j in range(n):
	for i in range(5):
		print(deck.pop(i),end=' ')
	print()
print(len(deck))