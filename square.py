""" ---Author:    Zachary Tunstall
University ID:    zstunsta  ---"""

import arcpy, arcpy.sa

#set arcpy workspace
arcpy.env.overwriteOutput = 1
arcpy.CheckOutExtension('Spatial')
arcpy.env.workspace = 'C:/gispy/data/ch06'

#input and output file names
nrast = 'getty_rast'
output = 'C:/gispy/scratch/squareGetty'

#raster function
orast = arcpy.sa.Square(nrast)
orast.save(output)

#return Spatial Analyst licence
arcpy.CheckInExtension('Spatial')
