"""
Zach Tunstall
zstunsta
"""

# listComprehension.py
import os

# Create a list of all uppercase field names
fieldNames = ['FID', 'Shape', 'COVER', 'RECNO']
fieldNames2 = [i.upper() for i in fieldNames]
print '1. All cap field names:', fieldNames2

# Create a list of float values rounded to the nearest whole number
strList = ['3.34', '1.07', '4.21', '4.56', '4.5']
intList = [round(float(j)) for j in strList]   ### modify this
print '2. Rounded float values:', intList

# Create a list of reciprocal values (the reciprocal of a number n is defined as 1/n)
values = [8.0, 4.0, 4.0, 1.0, 5.0, 4.0, 4.0, 2.0]
reciprocal = [1/k for k in values]  ### modify this
print '3. The reciprocal values:', reciprocal

# Create a list in which all the slash marks ('/') are replaced with underscores ('_').
fieldNames = ['FireType/Protection-Type', 'Time/Date', 'Condition/Status/Role']
fieldNames2 = [l.replace('/', '_') for l in fieldNames]  ### modify this
print '4. No slashes:', fieldNames2

# Create a list of output file names (with the word 'out' inserted before the extension).
inputFiles = os.listdir('C:/gispy/data/ch12/comp')
outputFiles = [m.replace(m[-4], 'out.')for m in inputFiles]  ### modify this
print '5. Output files:', outputFiles

# Create a list file extensions.
inputFiles = os.listdir('C:/gispy/data/ch12/comp')
extensions = [n.replace(n, n[-4:]) for n in inputFiles]  ### modify this
print '6. File extensions:', extensions


# Output in Interactive Window should look like this:
##1. All cap field names: ['FID', 'SHAPE', 'COVER', 'RECNO']
##2. Rounded float values: [3.0, 1.0, 4.0, 5.0, 5.0]
##3. The reciprocal values: [0.125, 0.25, 0.25, 1.0, 0.2, 0.25, 0.25, 0.5]
##4. No slashes: ['FireType_Protection-Type', 'Time_Date', 'Condition_Status_Role']
##5. Output files: ['Jackout.jpg', 'site1out.dbf', 'xy1out.txt']
##6. File extensions: ['.jpg', '.dbf', '.txt']
