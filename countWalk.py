"""
Zach Tunstall
zstunsta
countWalk.py
C:/gispy/data/ch12/wTest
"""
import sys, os, arcpy

myDir = sys.argv[1]

for root, dirs, files in os.walk(myDir):
    arcpy.env.workspace = root
    fcs = arcpy.ListFeatureClasses()
    for f in fcs:
        d = arcpy.GetCount_management(f)
        #couldn't mange to get dirs from each file into the final answer
        print "{0}/{1} has {2} entries.".format(myDir, f, d)
