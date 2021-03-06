#-----------------------------------------------------------------------
# greatcircle.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

# Accept float command-line arguments x1, y1, x2, and y2: the latitude
# and longitude, in degrees, of two points on the earth. Compute and
# write to standard output the great circle distance (in nautical
# miles) between those two points.

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# The following formulas assume that angles are expressed in radians.
# So convert to radians.

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

# Compute using the law of cosines.

# Great circle distance in radians
angle1 = math.acos(math.sin(x1) * math.sin(x2) \
         + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

# Convert back to degrees.
angle1 = math.degrees(angle1)

# Each degree on a great circle of Earth is 60 nautical miles.
distance1 = 60.0 * angle1

stdio.writeln(str(distance1) + ' nautical miles')

# Compute using the Haversine formula.

a = math.sin((x2-x1)/2.0) ** 2.0 \
    + (math.cos(x1) * math.cos(x2) * (math.sin((y2-y1)/2.0) ** 2.0))

# Great circle distance in radians
angle2 = 2.0 * math.asin(min(1.0, math.sqrt(a)))

# Convert back to degrees.
angle2 = math.degrees(angle2)

# Each degree on a great circle of Earth is 60 nautical miles.
distance2 = 60.0 * angle2

stdio.writeln(str(distance2) + ' nautical miles')

#-----------------------------------------------------------------------

# Leningrad to SF

# python greatcircle.py 59.9 -30.3 37.8 122.4
# 4784.369673474519 nautical miles
# 4784.369673474519 nautical miles
#
# Paris to Austin

# python greatcircle.py 48.87 -2.33 30.27 97.74
# 4423.14075970742 nautical miles
# 4423.140759707421 nautical miles
#
# Nashville airport (BNA) to LAX

# python greatcircle.py 36.12 -86.67 33.94 -118.4
# 1557.505111036951 nautical miles
# 1557.5051110369507 nautical miles
#
# Princeton to Paris

# python greatcircle.py 40.35 74.65 48.87 -2.33
# 3185.1779271158425 nautical miles
# 3185.1779271158416 nautical miles

#bai@ubuntu:~/pythonProject/princeton/1.2$ python3 greatcircle.py 48.87 -2.33 37.8 122.4
#4828.2410149086445 nautical miles
#4828.2410149086445 nautical miles
