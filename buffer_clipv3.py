# buffer_clipv3.py (soft-coded version)
# Purpose: Buffer a zone and use it to clip another file
# Usage: workspace output_directory file_to_buffer buffer_dist. file_to_clip
# Input example: C:/gispy/data/ch07/ C:/gispy/scratch/ special_regions.shp "1 mile" park.shp

import arcpy, sys, os

arcpy.env.overwriteOutput = 1
arcpy.env.workspace = arcpy.GetParameterAsText(0)
outDir = arcpy.GetParameterAsText(1)

# Set buffer params
fireDamage = arcpy.GetParameterAsText(2)
fireBuffer = outDir + fireDamage[:-4] + 'Buffer1.shp'
bufferDist = arcpy.GetParameterAsText(3)

# Set clip params
park = arcpy.GetParameterAsText(4)
clipOutput = outDir + park[:-4] + 'DamageBuffer.shp'

# Call tools
arcpy.Buffer_analysis(fireDamage, fireBuffer, bufferDist)
print '{0} created.'.format(fireBuffer)
arcpy.Clip_analysis(park, fireBuffer, clipOutput)
print '{0} created.'.format(clipOutput)
