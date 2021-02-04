"""
Author: Zach Tunstall
University ID: zstunsta
"""
import sys


#get user age from argument
age = int(sys.argv[1])
x = age


if x <= 6:
    print '$30'
elif x > 6 and x < 19:
    print '$319'
elif x >= 19 and x < 30:
    print '$429'
elif x >= 30:
    print '$549'
else:
    print 'Invalid Input'