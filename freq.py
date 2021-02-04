""" ---Author:    Zachary Tunstall
University ID:    zstunsta  ---
freq.py script to perform a Frequency (Analysis) that
will generate a table of land cover frequencies."""

import arcpy

# set workspace environment
arcpy.env.workspace = 'C:/gispy/data/ch06'

#input shapefile
ntab = 'park.shp'

# field name
fn = 'COVER'

# Create the output in 'C:/gispy/scratch'
otab = 'C:/gispy/scratch/COVER_freq.dbf'

arcpy.Frequency_analysis(ntab, otab, fn)
