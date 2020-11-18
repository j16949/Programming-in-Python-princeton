def majority(a, b, c):
	return (a and b) or (a and c) or (b and c)

def majority1(a, b, c):
	return (a or b) and (a or c) and (b or c)

a = [None]*8
for i in range(8):
	a[i]=[0]*3

n=0b0
for i in range(8):
	s=format(n,'b').zfill(3)
	for j in range(3):
		a[i][j] = s[j]
	n += 0b1

print('a\tb\tc\tma\tma1\t')
for i in range(8):
	for j in range(3):
		print(a[i][j],end='\t')
	print(majority(a[i][0],a[i][1],a[i][2]),end='\t')
	print(majority1(a[i][0],a[i][1],a[i][2]))
