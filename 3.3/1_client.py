import location

l = location.Location(22.99,33.788)
print(l)
rl = location.randomLocation()
print(rl)
s = '25.344 N, 63.5532 W,'
print(location.parseLocation(s))
print(l.distance(rl))
