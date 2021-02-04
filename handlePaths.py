"""
Author: Zach Tunstall
University ID : zstunsta
"""
# Example files "C:\Users\LENOVO\Desktop\GIS 540 Programming\HWscripts"  "C:\Users\LENOVO\Desktop\resumes"
# Example Py4gis files C:/gispy/data/ch07/park.shp xy1.txt

import os, sys 


p = sys.argv[1]
q = sys.argv[2]

#A basename of fist file
pBase = os.path.basename(p)
print "The first file is: " + pBase

#B extension of first file,
#    if file has no extension, print file name
tup = os.path.splitext(p)
if len(tup) >= 1:
    print 'The first file extension is: ' + tup[-1]
else:
    print tup
    
#C full path file name of second file
qPath = os.path.dirname(p) 
qBase = os.path.basename(q)
qFull = os.path.join(qPath, qBase)
print 'The full name of the second file is: ' + qFull

#D size of second file
qSize = os.path.getsize(qFull)
print 'The size of the second file is: ' + str(qSize)

#E list of files in directory
directory = os.listdir(qPath)
print q + 'contains the following files: ' + str(directory)
