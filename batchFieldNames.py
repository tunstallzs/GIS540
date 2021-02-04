"""
Zach Tunstall
zstunsta
batchFieldNames.py
C:/gispy/data/ch11/rastTester.gdb COVER
"""
import arcpy, sys

#user input
arg1 = sys.argv[1]
arg2 = '*' + sys.argv[2] + '*'

#arc workspace protocal
arcpy.env.overwriteOutput = 1
arcpy.env.workspace = arg1

#get raster list
rlist = arcpy.ListRasters(arg2)

for r in rlist:
    field = arcpy.ListFields(r)
    print r
    for f in field:
        print "\t{0}".format(f.name)


