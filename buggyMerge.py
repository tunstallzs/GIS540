""" Zach Tunstall
     zstunstall
"""
# buggyMerge.py # Purpose: Merge the dBASE tables in a directory # Usage: No arguments needed.
import arcpy, os, shutil  # The lines from here to the overwriteOutput command do NOT need modification.
origDir = 'C:/gispy/data/ch13/trains/'
scratchDir = 'C:/gispy/scratch/trains/'
if not os.path.exists(scratchDir):  # Create a scratch copy of data directory
    shutil.copytree(origDir, scratchDir)
arcpy.env.workspace = scratchDir
# Start here
arcpy.env.overwriteOutput = True
tables = arcpy.ListTables('*', 'dBASE')
output = 'Asummary.dbf'

# If the summary table already
# exists, delete it.
if output in tables:
    # This is my crafty soulution
    tables = tables[1:]
    
arcpy.Merge_management(tables, output)

# This prints a success message,
# when the tool succeeds.
print arcpy.GetMessage(2)