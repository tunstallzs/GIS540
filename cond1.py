#cond1.py
# Purpose:  Classify numeric input as small, medium, or large.
# Usage: numeric_value
# Input example:  3
import sys

num = float(sys.argv[1])

if num <= 5:
    print 'small'
elif 5 < num <= 10:
    print 'medium'
else:
    print 'large'
