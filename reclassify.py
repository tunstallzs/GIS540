""" ---Author:    Zachary Tunstall
University ID:    zstunsta  ---"""

import arcpy, arcpy.sa


#set arcpy workspace
arcpy.env.overwriteOutput = 1
arcpy.CheckOutExtension('Spatial')
arcpy.env.workspace = 'C:/gispy/data/ch06/'

#input and output files
nRast = 'getty_rast'
outRast = 'C:/gispy/scratch/reclassGetty'

# Remap Values
reTab = ([[1, 100],[2, 200]])
rMap = arcpy.sa.RemapValue(reTab) 

#reclassify raster
rClass = arcpy.sa.Reclassify(nRast, 'VALUE', rMap)

#delete intermidiate data
del rMap

#save new raster file
rClass.save(outRast)


#return Spatial Analyst licence
arcpy.CheckInExtension('Spatial')