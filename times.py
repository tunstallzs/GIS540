# Name: Zachary Tunstall
# ID: zstunsta

# times.py multiplies two numbers given as arguments.

import sys  # Now the script can use the built-in Python system module.

# sys.argv is the system argument vector.
# int changes the input to an integer number.
a = int(sys.argv[1])
b = int(sys.argv[2])

c = a * b
# format(c) substitutes the value of c for {0} in the print statement.
print 'The product is {0}.'.format(c)
