#-----------------------------------------------------------------------
# animated towers of hanoi
#-----------------------------------------------------------------------

import sys
import stdio
import stddraw

#-----------------------------------------------------------------------

# Write to standard output instructions to move n Towers of Hanoi
# disks to the left (if parameter left is True) or to the right (if
# parameter left is False).

r = []

def moves(n, left):
	global r
	if n == 0:
		return
	moves(n-1, not left)
	if left:
		stdio.writeln(str(n) + ' left')
		r.append([n,'l'])
	else:
		stdio.writeln(str(n) + ' right')
		r.append([n,'r'])
	moves(n-1, not left)

def hanoi(n):
	DT = 1000
	t = 1.4
	l = []
	tow = []
	for i in range(3):
		tow.append([])
		for j in range(n):
			tow[i].append(0)
	for i in range(n):
		l.append(t**i)
	stddraw.setXscale(-1,t**n*4)
	stddraw.setYscale(-1,n+2)
	stddraw.line(t**n*0.5,-1,t**n*0.5,n+1)
	stddraw.line(t**n*1.5,-1,t**n*1.5,n+1)
	stddraw.line(t**n*2.5,-1,t**n*2.5,n+1)
	tow[0] = l
	for i in range(n):
		stddraw.line(t**n*0.5-tow[0][i]/2,n-i,t**n*0.5+tow[0][i]/2,n-i)
	stddraw.show(DT)

	global r
	for a in range(len(r)):
		stddraw.clear()

		stddraw.line(t**n/2,-1,t**n/2,n+1)
		stddraw.line(t**n*1.5,-1,t**n*1.5,n+1)
		stddraw.line(t**n*2.5,-1,t**n*2.5,n+1)
		p = r[a][0]
		d = r[a][1]
		for i in range(3):
			flag = 0
			for j in range(n):
				#if j+1 == p:
				if tow[i][j]==t**(p-1):
					flag = 1
					if d == 'l':
						num = (i-1) % 3
					else:
						num = (i+1) % 3
					temp = tow[i][j]
					tow[i][j] = 0
					tt = n-1
					while tow[num][tt] != 0:
						tt -= 1
					tow[num][tt] = temp
				#if flag == 1: break
			if flag == 1 : break
		#print(tow)
		
		for i in range(3):
			for j in range(n):
				if tow[i][j]:
					stddraw.line(t**n*(i+0.5)-tow[i][j]/2,n-j,t**n*(i+0.5)+tow[i][j]/2,n-j)
					#print(i,j,'||||',t**n*(i+0.5)-tow[i][j]/2,n-j,t**n*(i+0.5)+tow[i][j]/2,n-j)
		stddraw.show(DT)
		
	
#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard output
# instructions to move n Towers of Hanoi disks to the left.

def main():
	#n = int(sys.argv[1])
	n = 3
	moves(n, True)
	hanoi(n)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------

# python towersofhanoi.py 1
# 1 left

# python towersofhanoi.py 2
# 1 right
# 2 left
# 1 right

# python towersofhanoi.py 3
# 1 left
# 2 right
# 1 left
# 3 left
# 1 left
# 2 right
# 1 left

# python towersofhanoi.py 4
# 1 right
# 2 left
# 1 right
# 3 right
# 1 right
# 2 left
# 1 right
# 4 left
# 1 right
# 2 left
# 1 right
# 3 right
# 1 right
# 2 left
# 1 right

