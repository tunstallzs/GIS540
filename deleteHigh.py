"""
Zach Tunstall
zstunsta
deleteHigh.py
Purpose: copies the input data to 'C:/gispy/scratch/' and
then uses cursor functionality to remove every record of a table where a given
field is higher than a given value. Use three required arguments, the full path file
name of an input file, the name of a numeric field in that file, and a search value.
Usage: C:/gispy/data/ch17/firesCopy2.shp FID 8
"""
import arcpy, sys, traceback, os

# Get file and workspace
arcpy.env.overwriteOutput = 1
incopy = sys.argv[1]

fc = 'C:/gispy/scratch/' + os.path.basename(incopy)
#size = os.path.getsize(fc)


# check for modified file by size and existance
# Copy file if not exist or modified
if  not os.path.exists(fc):
    arcpy.Copy_management(incopy, fc)
    arcpy.GetMessages

# Cursor variables and sql clause
field = sys.argv[2]
val = int(sys.argv[3])
a = ['*']
sql = '{0} > {1}'.format(field, val)

try:
    cursup = arcpy.da.UpdateCursor(fc, a, sql)
    for row in cursup:
        cursup.deleteRow()
        print 'Remove row: [{0}]'.format(row[0])
    del cursup
except:
    print 'An Error Ocurred'
    traceback.print_exc()
    del cursup


