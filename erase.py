"""
Author:    Zachary Tunstall
University ID:    zstunsta
"""

# Create a shapefile showing all
#park regions that did not sustain damage

import arcpy

arcpy.env.workspace = 'C:/gispy/data/ch06'

erase = 'special_regions.shp'
nput = 'park.shp'
output = 'C:/gispy/scratch/no_damage.shp'


arcpy.Erase_analysis(nput, erase, output)



