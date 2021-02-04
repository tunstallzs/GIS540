"""
Zach Tunstall
zstunsta
insertLine.py
Purpose: finds the centroids (point1 and point2) of the first two records in
'C:/gispy/data/ch17/park.shp' inserts line from point1 to point2 in the polyline shapefile
'C:/gispy/scratch/parkLines.shp' 'LEFT_FID = 50 for this record.
Usage:
"""
import arcpy, os, traceback
#arcpy.env.overwriteOutput = 1
fcPoly = 'C:/gispy/data/ch17/park.shp'
origfcLine = 'C:/gispy/data/ch17/parkLines.shp'
fcLine = 'C:/gispy/scratch/' + os.path.basename(origfcLine)
arcpy.Copy_management(origfcLine, fcLine)

try:
    with arcpy.da.SearchCursor(fcPoly, ['SHAPE@XY']) as sc:
        # Get 2 centroids
        row = sc.next()
        point1 = arcpy.Point(row[0][0], row[0][1])
        print 'Point1: ({0},{1})'.format(row[0][0], row[0][1])
        row = sc.next()
        point2 = arcpy.Point(row[0][0], row[0][1])
        print 'Point2: ({0},{1})'.format(row[0][0], row[0][1])
    del sc
except:
    print 'An error occurred.'
    traceback.print_exc()
    del sc

### Create an array and then a polyline.  Then use an insert cursor.
myArray = arcpy.Array([point1,point2])
myLine = arcpy.Polyline(myArray)
#qclause = "LEFT_FID = '50'"
try:
    with arcpy.da.InsertCursor(fcLine, ['SHAPE@', 'LEFT_FID']) as ic:
        newRow = [myLine, 50]
        ic.insertRow(newRow)
        print 'New Line Inserted.'
        del ic

except:
    print 'an error occured'
    traceback.print_exc()
    del ic