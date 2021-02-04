"""
Zach Tunstall
zstunsta
loopAggregate.py
Use a for loop to irerate over the aggregate polygons tool using increasing distances
"""
import arcpy

arcpy.env.workspace = 'C:/gispy/data/ch10/'
arcpy.env.overwriteOutput = 1
outEnv = 'C:/gispy/scratch/' 
inFeat = 'park.shp'

for num in range(150, 1051, 100):
    #set output name
    outFeat = outEnv + 'park{0}_agg.shp'.format(num)
    #set aggregate distance
    dist = ' {0} yards'.format(num) 
    arcpy.AggregatePolygons_cartography(inFeat, outFeat, dist)
    print '{0} created'.format(outFeat)

