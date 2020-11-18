def re_s(s):
		rs=s
		if len(s)>1:
			m=s[len(s)//2]
			if m=='L':
				rs=s[:len(s)//2]+'R'+s[len(s)//2+1:]
			elif m=='R':
				rs=s[:len(s)//2]+'L'+s[len(s)//2+1:]
		return rs
	
s='F'
for i in range(5):
		D=s+'L'+re_s(s)
		print(D)
		s=D
