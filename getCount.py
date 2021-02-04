""" ---Author:    Zachary Tunstall
University ID:    zstunsta  ---"""

import arcpy 

#set arcpy workspace
arcpy.env.workspace = 'C:/gispy/data/ch06'

# shapefile
park = 'park.shp'

# returns number of elements (polygons)
count = arcpy.GetCount_management(park)

print count

