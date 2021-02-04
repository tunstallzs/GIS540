"""
Zach Tunstall
zstunsta
addRaster.py
Purpose: add raster layer to existing map and save results as a copy in scratch directory
Usage: C:/gispy/data/ch24/maps/testAdd.mxd C:/gispy/data/ch24/otherData/getty_rast
"""
import sys, arcpy

newdoc = 'C:/gispy/scratch/testAdd.mxd' # output map doc file
mapdoc = sys.argv[1] #location of original map doc
rastloc = sys.argv[2] #location of raster layer
#newloc = 'C:/gispy/scratch/testAdd' #location for copy of map doc

#create mapdoc object
mxd = arcpy.mapping.MapDocument(mapdoc)
#create raster layer object
rastlyr = arcpy.mapping.Layer(rastloc)
#list of data frames in map doc
dfs = arcpy.mapping.ListDataFrames(mxd)
#first or only dataframe in map doc
df = dfs[0]
#add raster to map doc data frome
arcpy.mapping.AddLayer(df, rastlyr)
#make copy of map doc and save in scratch dir.
mxd.saveACopy(newdoc)
# delete map doc and release locks
del mxd
print "{0} created.".format(newdoc)