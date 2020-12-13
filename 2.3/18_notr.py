import sys

n = eval(sys.argv[1])
k = eval(sys.argv[2])
l = []	#存储从'a'开始的n个字母
#a的unicode码=acsii码为97
for i in range(97,n+97):
	l.append(chr(i))

#循环的次数因k而定，不好写
	
