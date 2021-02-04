"""
Author: Zach Tunstall
University ID: zstunsta

Ex.1 0.2 0.4   (in the box)
Ex.2 -0.1 0.5   (Outside the box)
Ex.3 0 0       (in the box)
"""
import sys

# set box boundaries
A = (0, 0)
B = (1, 1)

#call user input arguments
x = float(sys.argv[1])
y = float(sys.argv[2])

# Conditional Statements
if x>= A[0] and x <= B[0] and y >= A[1] and y <= B[1]:
    print 'is inside the box'
else:
    print 'is outside the box'
