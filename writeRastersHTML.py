"""
Zach Tunstall
zstunsta
writeRastersHTML.py
Purpose:
Usage: C:/gispy/data/ch20/rastTester.gdb C:/gispy/scratch
"""
import arcpy, sys, os

# define funtion to create html list
def python2htmlList(myList, listType, attrs=''):
    '''Convert a Python list to HTML list.
    For example, convert [rast1,rast2] to:
    <ul>
       <li>rast1</li>
       <li>rast2</li>
    </ul>
    '''
    # Wrap items in item tags.
    htmlItems = ['<li>' + str(item) + '</li>' for item in myList]

    # Join the item list into a string with a line break after each item.
    itemsString = '''\n        '''.join(htmlItems)

    # Wrap the string of items in the list tag.
    htmlList = '''
    <{0} {1}>
        {2}
    </{0}>
    '''.format(listType, attrs, itemsString)
    return htmlList

# User Args and workspace setup
imageDir = sys.argv[1]
outDir = sys.argv[2]
arcpy.env.workspace = imageDir
#get list of rasters
rasts = arcpy.ListRasters()
#arg1 basename
iGDB = os.path.basename(imageDir)
#Call user defined function
hList = python2htmlList(rasts, 'rast')

#HTML list of rasters
htmlBody = '''
<body>
    {0}
</body>
'''.format(hList)
#HTML header with database name
htmlHead ='''
<!DOCTYPE html>
<html>
    <body>
        <h1> Rasters in {0}</h1>'''.format(iGDB)


#HTML File name and location
hFile = 'C:/gispy/scratch/rasters.html'
#write HTML file
with open(hFile, 'w') as outf:
    outf.write(htmlHead)
    outf.write(htmlBody)
#Confirmation message
print '{0} created.'.format(hFile)