"""
Zach Tunstall
zstunsta
"""

# functionPractice.py
# Purpose: Print information separated by fish punctuation art
#          for each polygon feature class in the input workspace.
# Usage: input_workspace
# Example input: C:/gispy/data/ch15/tester.gdb
##Pseudocode:
##IMPORT arcpy
##
##PROC printFish
##    PRINT a fish
##
##PROC printDescription(filename)
##    GET a describe object 
##    PRINT name
##    PRINT type
##    PRINT catalog path
##
##SET the workspace to the user argument
##GET a list of polygon feature classes
##FOR each file in list
##    CALL printfish
##    CALL printDescription with the current file as the argument

import arcpy, sys


# Set Workspace
arcpy.env.workspace = sys.argv[1]
arcpy.env.overwriteOutput = 1

#Get List of FeatureClasses
fctype = 'Polygon'
fcs = arcpy.ListFeatureClasses({'#'}, fctype)


def printFish():
    print "  ,,, "
    print "<')}>)={"
    print " `` "


def printDescription(filename):
    rona = arcpy.Describe(filename)
    typeA = rona.dataType
    Name = rona.name
    Join = rona.catalogPath
    print "Name:        {0}".format(Name)
    print "DataType:        {0}".format(typeA)
    print "CatalogPath:        {0}".format(Join)


# Create FOR loop and iterate over 2 functions
for fc in fcs:
    printFish()
    print ''
    printDescription(fc)
    print ''

#-----------------------------------------
## For example input: C:/gispy/data/ch15/tester.gdb
## Output should look like this:
##  ,,,
##<')}>)={
##  ``
##    
##Name:        park
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/park
##
##  ,,,
##<')}>)={
##  ``
##    
##Name:        regions2
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/regions2
##
##  ,,,
##<')}>)={
##  ``
##    
##Name:        workzones
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/workzones
##
##  ,,,
##<')}>)={
##  ``
##    
##Name:        regions1
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/regions1
##
##  ,,,
##<')}>)={
##  ``
##    
##Name:        smallWoods2
##DataType:        FeatureClass
##CatalogPath:        C:/gispy/data/ch15/tester.gdb/smallWoods2
