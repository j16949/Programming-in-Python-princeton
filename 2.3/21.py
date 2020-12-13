#从排列组合的角度考虑，设s的长度为n，其中k位反转，即从n位中选k位，然后反转Cnk。
#这是一个偷懒一点都不优，利用上一个题目中comb的解法
import sys

def hamming(s,k):
	n = len(s)
	sn =''
	#st =set()
	for i in range(n):
		sn += str(i)
	st = list(comb(sn,k))
	rt = []
	for i in range(len(st)):
		t = s
		for j in st[i]:
			j =eval(j)
			temp = t[j]
			if temp == '0' :
				temp = '1'
			else:
				temp = '0'
			t = t[:j]+temp+t[j+1:]
		rt.append(t)
	return rt

def comb(s,k):
	if len(s) == k : return {s}
	r = set()
	for i in range(len(s)):
		subStrings = comb(s[:i]+s[i+1:],k)
		for subString in subStrings:
			r.add(subString)
	return r

print(hamming('0000',2))
