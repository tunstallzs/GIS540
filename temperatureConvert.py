"""
Zach Tunstall
zstunsta
temperatureConvert.py
Tool to convert between celsius & fahrenheit
"""

import sys
# Conditional to check for user errors
numArg = len(sys.argv)
if numArg == 1:
    print 'Error, no user input'
    print 'Usage: number {unit (C or F)} Example: 32 F'
elif numArg == 2:
    # determine if a number was entered
    if sys.argv[1] < 'a' :
        # assume American user
        print "Since you didn't specify a scale, I'm assuming F to C"
        x = (float(sys.argv[1]) - 32) * 0.56
        print str(x) + ' Fahrenheit is equivalent to ' + str(fcon) \
              + ' Celsius'

    else:
# For crystal clear instructions
        print 'Enter a number followed by a space followed by F or C'


# if no user error
else:
    # temperture input and scale (F or C)
    tempNum = sys.argv[1]
    tempScale = sys.argv[2]


    if tempScale.upper() == 'F':
        fcon = (float(tempNum)-32) * 0.56
        print str(tempNum) + ' Fahrenheit is equivalent to ' + str(fcon) \
              + ' Celsius'
    elif tempScale.upper() == 'C':
        ccon = float(tempNum) * 1.8 + 32
        print str(tempNum) + ' Celsius is equivalent to ' + str(ccon) \
              + ' Fahrenheit'
    else:
        print 'User Error'

