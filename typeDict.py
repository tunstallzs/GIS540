"""
Zach Tunstall
zstunsta
typeDict.py
Purpose: collect file data types and names in a dictionary. (One item for each
data type from Describe object. Each item needs list of files with the key data type
Print resulting dictionary.
Usage: C:/gispy/data/ch18/smallDir
"""
import arcpy, sys



space = sys.argv[1]
arcpy.env.workspace = space
#create dictionary
mydict = { }
#List files in directory
files = arcpy.ListFiles()
for val in files:
    #Use describe method to get keys
    desc = arcpy.Describe(val)
    dt = str(desc.datatype)
    #set first key val pair
    if dt not in mydict:
        mydict[dt] = val
        #convert values to list
        mydict[dt] = [mydict[dt]]
        #if values isnt list, convert
    elif not isinstance(mydict[dt], list):
        mydict[dt] = [mydict[dt]]
        #append list
        mydict[dt].append(val)
    else:
        mydict[dt].append(val)

print "Type dictionary:"
print mydict


