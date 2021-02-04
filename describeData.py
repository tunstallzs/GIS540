"""
Zach Tunstall
zstunsta
Tool to determine shapefile or raster data
Example values
"""
import arcpy, sys

# user input
arg = sys.argv[1]

#describe  and datatype methods
dsc = arcpy.Describe(arg)
dType = dsc.dataType

# conditional print statements
if dType == 'ShapeFile':
    print dsc.shapeType
elif dType == 'RasterDataset':
    print 'GIF'
else:
    print dsc.dataType
