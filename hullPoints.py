"""
Author:    Zachary Tunstall
University ID:    zstunsta
"""
import arcpy 


#set arcpy workspace
arcpy.env.overwriteOutput = 1
arcpy.env.workspace = 'C:/gispy/data/ch06'

nput = 'data1.shp'
oput = 'C:/gispy/scratch/boundingPoly.shp'
oput2 = 'C:/gispy/scratch/outerPoints'
#set bounds and change corners to points
bound = arcpy.MinimumBoundingGeometry_management(nput, oput)
arcpy.FeatureVerticesToPoints_management(bound, oput2)

print "boundingPoly.shp created in C:/gispy/scratch"
print "outerPoints.shp created in C:/gispy/scratch"