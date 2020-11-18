import stddraw

l = [1,2,1,1,2]
stddraw.setXscale(-1,100)
stddraw.setYscale(0,5)
for k in range(len(l)):
	stddraw.filledRectangle(k,0,0.5,l[k])
stddraw.show()

