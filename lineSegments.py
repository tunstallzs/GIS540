# Zach Tunstall
# zstunsta
#lineSegments.py
# Purpose: Define a LineSegment class
# Usage: 1 2 4 3

import math, sys


class LineSegment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculateLength(self):
        '''Calculate the length of this line segment'''
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

    def calculateSlope(self):
        '''Calculate the slope of this line segment.'''
        run = self.x2 - self.x1
        if run == 0:
            return "undefined"
        else:
            return (self.y2 - self.y1)/float(run)

    def translateY(self, yShift):
        '''Translate the line vertically by yShift
        (Shifts the line segment up or down.)'''
        self.y1 = self.y1 + yShift
        self.y2 = self.y2 + yShift

    def printSegment (self):
        '''Print values of endpoints of line'''
        return "Endpoint 1:( {0}, {1} )\nEndpoint 2: ( {2}, {3} )".format(self.x1, self.y1, self.x2, self.y2)


X1 = float(sys.argv[1])
Y1 = float(sys.argv[2])
X2 = float(sys.argv[3])
Y2 = float(sys.argv[4])

ls = LineSegment(X1, Y1, X2, Y2)
print ls.printSegment()
cs = round(ls.calculateSlope(), 1)
print "Slope: {0}".format(cs)
cl = round(ls.calculateLength(),1)
print "Length: {0}".format(cl)
ls.translateY(-3)
print ls.printSegment()
