"""
Zach Tunstall
zstunsta
MPHzip.py
"""
# input lists
dList = [0.04, 0.05, 0.91, 0.16, 18]
timeList = ['7m:13s', '11m:29s', '16m:48s', '3m:26s', '120m:0s']
# empty lists for seconds, velocity and hours
secList = [ ]
avgList = [ ]
hrList = [ ]
# split time fromat into seconds & print to empty list
for minute in timeList:
    L = minute.split(':')
    for m in L:
        if 'm' in m:
            m = int(m[:-1])*60
        elif 's' in m:
            m = int(m[:-1])
        secList.append(m)

""" Credit for the line 27 goes to hashcode55.
Code found at: https://stackoverflow.com/questions/
42444046/calculate-the-sum-of-every-5-elements-in-a-python-array"""
# sum every to object in list of seconds
seconds = [sum(secList[i:i+2]) for i in range(0, len(secList), 2)]

#convert to hours
for s in seconds:
    s = float(s) / 3600
    hrList.append(s)
    
#create MPH list
for d, h in zip(dList, hrList):
    b = d/h 
    avgList.append(b)
    
#zip lists together and format
for d, t, a in zip(dList, timeList, avgList):
    print "Distance: {0} \t Time: {1} \t Speed: {2:.2f} miles/hr".format(d, t, a)
    
###Hint 1: Inside the 'zip' loop, use several steps to extract the minutes and seconds
###        and then convert to hours.
###Hint 2: To print a float with 2 or less decimal places, put ':.2f' inside the format place holder.
###        Example,
###        >>> speed = 5.1666666666667
###        >>> print 'Speed: {0:.2f} miles/hr'.format(speed)
###        Speed: 5.17 miles/hr
