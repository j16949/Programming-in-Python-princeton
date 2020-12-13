#!/usr/bin/python
# coding=UTF-8
# Calculate ISO 216/ISO 269 paper formats -- Markus Kuhn

from math import floor
format = "%3s = %4d mm × %4d mm"

# A series
width  = floor(1000.0 / 2.0**0.25 + 0.5);
height = floor(2.0**0.25 * 1000.0 + 0.5);
print(format % ("4A0", width * 2, height * 2))
print(format % ("2A0", height, width * 2))
for n in range(11):
    print(format % ("A%d" % n, width, height))
    (width, height) = (floor(height / 2), width)

print("")

# B series
width  = 1000.0;
height = floor(2.0**0.5 * 1000.0 + 0.5);
for n in range(11):
    print(format % ("B%d" % n, width, height))
    (width, height) = (floor(height / 2), width)

print("")

# C series
width  = floor(1000.0 / 2.0**0.125 + 0.5);
height = floor(8.0**0.125 * 1000.0 + 0.5);
for n in range(11):
    print(format % ("C%d" % n, width, height))
    (width, height) = (floor(height / 2), width)
