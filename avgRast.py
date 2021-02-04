"""
Author:    Zachary Tunstall
University ID:       zstunsta
"""

import arcpy, arcpy.sa


#set arcpy workspace
arcpy.env.overwriteOutput = 1
arcpy.CheckOutExtension('Spatial')
arcpy.env.workspace = 'C:/gispy/data/ch06/rastSmall.gdb'

#input rasters                      
r1 = 'Out1'
r2 = 'Out2'
r3 = 'Out3'

#raster math to compute avg raster values
radd = arcpy.sa.Plus(r1, r2)
moreRadd = arcpy.sa.Plus(radd, r3)
avgRast = arcpy.sa.Divide(moreRadd, 3)

# save final raster output
avgRast.save('C:/gispy/scratch/avgRast')

#delete intermidiate rasters
del radd
del moreRadd

#return Spatial Analyst licence
arcpy.CheckInExtension('Spatial')