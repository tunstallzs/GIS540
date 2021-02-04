"""
Zach Tunstall
zstunsta
listUniqueValues.py
Purpose: use search cursor to print unique field values from a user defined file
Usage: C:/gispy/data/ch16/park.shp COVER
"""
import os, sys, arcpy

#get function from another script
dir = 'C:/gispy/sample_scripts/ch16/exercises'
spath = os.path.abspath(dir)
relpath = 'listManage'
modpath = os.path.join(spath, relpath)
sys.path.append(modpath)
from listManager2 import uniqueList

# import user values for seach cursor
sf = sys.argv[1]
fn = sys.argv[2]
#create empty list 
L = []
#run search cursor 
sc = arcpy.da.SearchCursor(sf, [fn])
for row in sc:
    #populate list
    L.append(row[0])
del sc
#call imported function
x = uniqueList(L)
print x

