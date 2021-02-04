"""
Zach Tunstall
zstunsta
"""

# moduloTry.py
# Purpose: Compute the remainder of dividing two numbers.
# Usage: Two integer values
# Example input1: 25 4
# Example input2: 5 0
# Example input3: woods 3

import sys
try:
    field1 = sys.argv[1]
    field2 = sys.argv[2]
    print "a: {0}   b: {1}".format(field1, field2)
    a = float(field1)
    b = int(field2)
    c = a % b
except ZeroDivisionError:
    print '{0} mod {1} is undefined'.format(a, b)
    #print sys.exc_info()[1:]
except ValueError:
    print "Usage: <numeric value 1> <numeric value 2>"
    print "c: Not Found"
    #print sys.exc_info()[1:]
except IndexError:
    print "Usage: <numeric value 1> <numeric value 2>"
    print "c: Not Found"
    #print sys.exc_info()[1:]
except NameError:
    print "Usage: <numeric value 1> <numeric value 2>"
    print "c: Not Found"
    #print sys.exc_info()[1:]
print "c: {0}".format(c)
