import stdio

def ex233(n):
	if n<=0 : return 
	stdio.writeln(n)
	ex233(n-2)
	ex233(n-3)
	stdio.writeln(n)

ex233(6)

#642211431136
