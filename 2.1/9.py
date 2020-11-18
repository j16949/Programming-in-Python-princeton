import stdio

def duplicate(s):
	t = s + s
	return t

s='hello'
s=duplicate(s)
t='bye'
t=duplicate(duplicate(duplicate(t)))
stdio.writeln(s+t)

