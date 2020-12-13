import stddraw

def reSquares(n,x,y,r):
	if n == 0 : return
	stddraw.setPenColor(stddraw.GRAY)
	stddraw.filledSquare(x,y,r)
	stddraw.setPenColor()
	stddraw.square(x,y,r)
	reSquares(n-1,x-r,y+r,r/2.2)
	reSquares(n-1,x-r,y-r,r/2.2)
	reSquares(n-1,x+r,y+r,r/2.2)
	reSquares(n-1,x+r,y-r,r/2.2)

	

R = 2
X = 0
Y = 0
stddraw.setXscale(-2*R,2*R+2)
stddraw.setYscale(-2*R,2*R+2)
#stddraw.filledSquare(1,1,1)
#stddraw.square(2,2,1)
reSquares(5,X,Y,R)
stddraw.show()
