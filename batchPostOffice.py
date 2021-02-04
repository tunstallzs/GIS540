"""
User Name: Zach Tunstall
User ID: zstunsta
batchPostOffice.py

C:/gispy/data/ch11/tester.gdb C:/gispy/scratch
"""
import arcpy, sys, os
# user inputs and workspace
inFeat = sys.argv[1]
outFeat = sys.argv[2]
arcpy.env.workspace = inFeat
arcpy.env.overwriteOutput = 1

# create list of shapefile containing the word data
list = arcpy.ListFeatureClasses('*data*')

for l in list:
    # out Directory
    outDir = os.path.splitext(l)[0] + 'Postal.shp'
    tool = os.path.join(outFeat, outDir)
    # call tool
    createPoly = arcpy.CreateThiessenPolygons_analysis(l, tool)
    tool.replace( '\'', "/")
    print '{0} created'.format(tool)