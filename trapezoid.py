"""
Zach Tunstall
zstunsta
trapezoid.py
Purpose: create functions to define shape name and
calculate area of shapes using variables given.
Usage: No User Arguments
"""

# Create reusable functions for polygons
# Finds Area
def calculateArea(b1, b2, alt):
    Area = float(b1 * alt)
    print "Area = {0}".format(Area)

# Checks equality of base sides
def isParallelogram(b1, b2):
    if b1 == b2:
        x = "True"
    else:
        x = "False"
    print "is Parallelogram? {0}".format(x)

# Checks for 90 degree angles
def isRectangele(b1, b2, angle):
    if angle == 90:
       c = "True"
    else:
        c = "False"
    print "Is rectangle? {0}".format(c)
print ''

#90 degree angles and equal length sides
def isSquare(b1, b2, alt, angle):
    if b1 == b2 and b1 == alt and angle == 90:
        y = "True"
    else:
        y = "False"
    print "Is square? {0}".format(y)


# Quad1: b1 = 4, b2 = 4, alt = 6, angle = 90
b1 = 4
b2 = 4
alt = 6
angle = 90
print 'Quad1: b1 = 4, b2 = 4, alt = 6, angle = 90'
calculateArea(b1, b2, alt)
isParallelogram(b1, b2)
isRectangele(b1, b2, angle)
isSquare(b1, b2, alt, angle)
print ''

# Quad2: b1 = 5, b2 = 5, alt = 5, angle = 30
b1 = 5
b2 = 5
alt = 5
angle = 30

print 'Quad2: b1 = 5, b2 = 5, alt = 5, angle = 30'
calculateArea(b1, b2, alt)
isParallelogram(b1, b2)
isRectangele(b1, b2, angle)
isSquare(b1, b2, alt, angle)
print ''

# Quad3: b1 = 8, b2 = 8, alt = 6, angle = 60
b1 = 8
b2 = 8
alt = 6
angle = 60

print 'Quad3: b1 = 8, b2 = 8, alt = 6, angle = 60'
calculateArea(b1, b2, alt)
isParallelogram(b1, b2)
isRectangele(b1, b2, angle)
isSquare(b1, b2, alt, angle)