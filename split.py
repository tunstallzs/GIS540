""" ---Author:    Zachary Tunstall
University ID:    zstunsta  ---
split.py takes an input shapefiles and splits them into seperate shapefiles."""

import arcpy

# set workspace environment
arcpy.env.workspace = 'C:/gispy/data/ch06'

#input variables
nput = 'park.shp'
zones = 'workzones.shp'
out = 'C:/gispy/scratch/'

#split tool
arcpy.Split_analysis(nput, zones, 'ZONE', out)


