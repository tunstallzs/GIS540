""" ---Author:    Zachary Tunstall
University ID:    zstunsta  ---"""

import arcpy 

#set arcpy workspace
arcpy.env.workspace = 'C:/gispy/data/ch06'
arcpy.env.overwriteOutput = 1

nput = 'park.shp'
oput1 = 'C:/gispy/scratch/centroid.shp'
oput2 = 'C:/gispy/scratch/voronoi.shp'

F2P = arcpy.FeatureToPoint_management(nput, oput1)
arcpy.CreateThiessenPolygons_analysis(F2P, oput2)
