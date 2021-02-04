"""
Zach Tunstall
zstunsta

dbf2csv
"""
import arcpy, os
arcpy.env.workspace = "C:/gispy/scratch/trains"
tables = arcpy.ListTables('*', 'dBASE')


for t in tables:
    csvName = os.path.splitext(t)[0] + ".csv"
    arcpy.TableToTable_conversion(t, arcpy.env.workspace, csvName)
    print("{0} converted to {1}".format(t,csvName))
print("All dbf converted to csv.")
