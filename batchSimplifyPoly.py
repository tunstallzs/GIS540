"""
Zach Tunstall
zstunsta
batchSimplifyPoly.py

C:/gispy/data/ch11/tester.gdb C:/gispy/scratch
"""
import arcpy, sys, os

#set input and worspace
inFeat = sys.argv[1]
outFeat = sys.argv[2]
arcpy.env.workspace = inFeat
arcpy.env.overwriteOutput = 1

#create list of polygon shapefiles in workspace env
list = arcpy.ListFeatureClasses('*', 'polygon')

# loop throu list and simplify polygons, move to new dir
for l in list:
    #set output directory
    outDir = os.path.splitext(l)[0] + 'Simp.shp'
    tool = os.path.join(outFeat, outDir)
    #call tool
    simpPoly = arcpy.SimplifyPolygon_cartography(l, tool, 'POINT_REMOVE', 50)

    print '{0}/{1} created.'.format(tool, l)