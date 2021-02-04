"""
Zach Tunstall
zstunsta
cursorBasics.py
Purpose: copies files from 'C:/gispy/data/ch17/park.shp'' to 'C:/gispy/scratch/' and does A through C tasks for the scratch file
Usage: No Arguments
"""

import arcpy

#copy file to scratch folder and check for previous copy
arcpy.env.overwriteOutput = 1
arcpy.env.workspace =  'C:/gispy/data/ch17/'
inFile = 'park.shp'
outFile =  'C:/gispy/scratch/park.shp'
if outFile == 0:
    arcpy.Copy_management(inFile, outFile)
    print arcpy.GetMessage[2]

#field_names = [f.name for f in arcpy.ListFields(outFile)]
#print field_names

#part A) FID and COVER of FID = 45
fieldNames = ['*']
clause = "FID = 45"
scur = arcpy.da.SearchCursor(outFile, fieldNames, clause)
rowA = scur.next()
print "Row with FID = {0} has cover {1}".format(rowA[0], rowA[2])
del scur

# change COVER of FID = 120 to 'park'
sql = "FID = 120"
ucur = arcpy.da.UpdateCursor(outFile, fieldNames, sql)
rowB = ucur.next()
if rowB[2] == 'woods':
    rowB[2] = 'park'
    ucur.updateRow(rowB)
print "Row with FID = {0} has been updated to use cover: {1}".format(rowB[0], rowB[2])
del ucur

# Delete row with FID = 22 and return number of rows before and after
count = arcpy.GetCount_management(outFile)
print "Count before deletion: {0}".format(count)
santa = "FID = 22"
dcur = arcpy.da.UpdateCursor(outFile, fieldNames, santa)
rowC = dcur.next()
dcur.deleteRow()
print rowC[:]
del dcur
count2 = arcpy.GetCount_management(outFile)
print "Count after deletion: {0}".format(count2)
