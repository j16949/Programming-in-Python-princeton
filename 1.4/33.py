import random
import sys

n=eval(sys.argv[1])
trails=eval(sys.argv[2])
deadEnds = 0
walk=0
deadwalk,outwalk=[],[]

for t in range(trials):

    # Create an n-by-n array, with all elements set to False.
	a=[]
	for i in range(n):
		a.append([])
		for j in range(n):
			a[i].append([])
			for p in range(n):
				a[i][j].append([])

    x = n//2
    y = n//2
	z = n//2

    while (x > 0) and (x < n-1) and (y > 0) and (y < n-1) and (z > 0) and (z < n-1):
        # Check for dead end and make a random move.
        a[x][y][z] = True
        if a[x-1][y][z] and a[x+1][y][z] and a[x][y-1][z] and a[x][y+1][z] and a[x][y][z-1] and a[x][y][z+1]:
            deadEnds += 1
            deadwalk.append(walk)
            walk=0
            break
        r = random.randrange(1, 7)
        if   (r == 1) and (not a[x+1][y][z]):
            x += 1
        	walk+=1
        elif (r == 2) and (not a[x-1][y][z]):
            x -= 1
        	walk+=1
        elif (r == 3) and (not a[x][y+1][z]):
            y += 1
        	walk+=1
        elif (r == 4) and (not a[x][y-1][z]):
            y -= 1
        	walk+=1
		elif (r == 5) and (not a[x][y][z+1]):
            z += 1
			walk+=1
		elif (r == 6) and (not a[x][y][z-1]):
            z -= 1
        	walk+=1
    else:
        outwalk.append(walk)
        walk=0

stdio.writeln(str(100*deadEnds//trials) + '% dead ends')
stdio.writeln(str(sum(deadwalk)//len(deadwalk)) + ' average of dead walk')
if sum(outwalk)>0:
    stdio.writeln(str(sum(outwalk)//len(outwalk)) + ' average of out walk')
else:
    stdio.writeln('never walk out')
