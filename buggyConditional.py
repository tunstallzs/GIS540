"""
Zach Tunstall
zstunsta
"""
# buggyConditional.py
# Purpose: Calculate the value of a field based on the values of three input parameters.       
# Usage: full_path_featureclass_filename Z_value AF_value T_value output_fieldname
# Example input: C:/gispy/data/ch13/tester.gdb/c1 -2 3 6 veld
import arcpy, os, sys
fcCopy = sys.argv[1]
Z = float(sys.argv[2])
AF = float(sys.argv[3])
T = float(sys.argv[4])
outFieldName = arcpy.GetParameterAsText(4)
copyMan =  'C:/gispy/scratch/' + os.path.basename(fcCopy) +'.shp'
if not arcpy.Exists(copyMan): 
    arcpy.CopyFeatures_management(fcCopy, copyMan) #Assume this line is ok.

# Add output field to the copy, if it doesn't already exist
fields = arcpy.ListFields(fcCopy)  
fieldNames = [field.name for field in fields]
if field.name not in fieldNames:
    arcpy.AddField_management(fcCopy, outFieldName)

if (Z > 0) and (AF > 0):
    value = T + Z + AF # or = sum([T, Z, AF])
elif (Z > 0) and (AF < 0):
    value = T + Z         # or = sum([T, Z ])
elif (Z < 0) and (AF > 0):
    value = T + AF        # or = sum([T, AF])
else:
    value = T

print "Value: {0}".format(value)

# Set the new field to the output value
results = arcpy.CalculateField_management(fcCopy, outFieldName, value)

print results.getMessages()