import stdio

def readBool2D(filename):
	with open(filename,'r') as Tfile:
		info_line = Tfile.readlines()
		l = len(info_line)
		w = len(info_line[0].split(' '))
		tf = [[False] * w for i in range(l)]
		for i in range(len(info_line)):
			s = info_line[i].strip('\n').split(' ')
			for j in range(len(s)):
				if s[j] == '1':
					tf[i][j] = True
		return tf

print(readBool2D('14.txt'))
