"""
Final Py
Zach Tunstall
** Start Date must be after Febuary 4 2020
Purpose: Writes table data from online database to txt file, Clean Data, Create Map Document, Create GIF, Create html file
Usage: [ Start Date, End Date, File Dir, Number of {days} Map Document, Confidence Level ]
Usage: example: 05/28/2020 06/4/2020 "C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\webtext" 3 "C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\GIFtry2.mxd" 75
"""
import datetime, urllib2
import arcpy, os, sys, traceback
from PIL import Image # Python Image Library
import glob


def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)
    arcpy.SetProgressorLabel(message)

def printArgs():
    '''Print user arguments.'''
    printArc('Number of arguments = {0}'.format(len(sys.argv)))
    for index, arg in enumerate(sys.argv):
        printArc('Argument {0}: {1}'.format(index, arg))
        
def calArgs(date):
    '''Reformat calandar dates to datetime'''
    date = date[:10]
    datestr = date.split('/')
    dateListNum = list(map(int, datestr))
    listDay = dateListNum[1]
    dateDay = dateListNum[1]
    dateMonth = dateListNum[0]
    dateYear = dateListNum[2]
    dateDate = datetime.date(dateYear, dateMonth, dateDay)
    return dateDate



# Initialize Progress Bar
arcpy.SetProgressor('step', 'Preparing Script', 0, 100, 1)
arcpy.SetProgressorPosition(0)
txtFileDir = sys.argv[3]
# Set workspace env
arcpy.env.workspace = txtFileDir
arcpy.env.overwriteOutput = 1
arcpy.SpatialReference(3857) # Web Mercator

# Call Calendar function on Start and End Date Arguments
arg2 = sys.argv[2]
arg1 = sys.argv[1]
startDate = calArgs(arg1)
endDate = calArgs(arg2)


#Move Progress Bar
arcpy.SetProgressorLabel('Creating List of Websites')
arcpy.SetProgressorPosition(0)
print arcpy.AddMessage( " Start- {0} ;  End- {1}".format(arg1, arg2))


# Text File Data Source
website = 'http://viirsfire.geog.umd.edu/web_data/GLOBAL/NOAA/20200930_NOAA.txt'
print website
# empty  list for websites
websiteList = [ ]

# Amount of change in date range by this amount.
# Day interval.
mwd = int(sys.argv[4])
delta = datetime.timedelta(days=mwd)

# folder location to write txt files 
txtFileDir = sys.argv[3]
# Confidence Interval to filter by
confidenceLevel = sys.argv[6]

# Prepare List for listing .txt files.
xFiles  = []

## CREATE WEBSITE LIST
# Uses start, end and time delta to create list of URL File locations
apos= 10 # Gui Position
while startDate <= endDate:
    startDate += delta
    # Citations Here##########################
    dateReplace = str(startDate.strftime('%Y%m%d')) # Variable name = startDate
    websiteList.append(website.replace(website[51:59], dateReplace)) # Adds Website to Website List
    #Progress Bar
    apos += 1
    arcpy.SetProgressorPosition(20)
#Update GUI Messages
arcpy.AddMessage("Data Obtained From {0}".format(website))
#Move Progress Bar
arcpy.SetProgressorLabel('Creating Cutom Website URL')
arcpy.SetProgressorPosition(20)



## WRUTE FILE IO
#Move Progress Bar
arcpy.SetProgressorLabel('Writing Website to File in Directory')
arcpy.SetProgressorPosition(30)
posx = 31 # GUI Position
# Parsing list of websites and writing their contents to a folder of text files
for site in websiteList:
    # Write each line of website to a new text file
    newTextFile = os.path.join(txtFileDir, site[-17:])
    with open(newTextFile, 'w') as tout:
        for p in urllib2.urlopen(site):
            tout.write(p)
        arcpy.AddMessage("New file at {0}".format(newTextFile))
        print "New file at {0}".format(newTextFile)
    # Increment Progress Bar
    posx += 1
    arcpy.SetProgressorPosition(posx)
    xFiles = arcpy.ListFiles({'*.txt'})
# Print status update to tool window.
arcpy.AddMessage('Text Files {0} Created in {1}'.format(xFiles, txtFileDir))

    #Move Progress Bar
arcpy.SetProgressorLabel('Converting Text to Shape Files')
arcpy.SetProgressorPosition(50)

# Geoprocessing Loop Start:
# For each txt file, create xy event table, create layer file, then create point shapefile
# Update Cursor filters fire data with low confidence.
xListLen = len(websiteList)
for x in xFiles[:xListLen]: # This block creates output names for shapefiles
    fLyrName = '{0}FireXY'.format(x[0:8])
    fOutName = os.path.join(txtFileDir,'{0} Fire.lyr'.format(x[0:8]))
    # Change layer name to shapefile name
    shapeFire = os.path.join(txtFileDir,'{0}Fire.shp'.format(x[0:8]))
    try:
        if  fLyrName not in txtFileDir:
                arcpy.MakeXYEventLayer_management(x, 'Longitude', 'Latitude', fLyrName)  
                print fLyrName
                arcpy.SaveToLayerFile_management(fLyrName, fOutName)
                arcpy.FeatureToPoint_management(fOutName, shapeFire, 'INSIDE')
                print arcpy.GetMessages() # Still Getting Locked Files Here
        else:
            pass
    except:
        print 'Layer Exists, & XY Layer Tool Broke'
        print arcpy.GetMessages()
        pass

    #  Use Search Cursor to filter false positives (low confidence)
    L = arcpy.ListFiles('*.shp')
    fName = '*'
     # Confidence level from User Input 6
    where = "Confidence < {0}".format(confidenceLevel)

    for inTab in L:
        try:
            count = 0
            with arcpy.da.UpdateCursor(inTab, fName, where) as upcur:
                for row in upcur:
                   count += 1
                   upcur.deleteRow()
                   print 'deleting row {0}'.format(row[0])
                print "Number of rows deleted {0}".format(count)
            del upcur
        except:
            print 'Cursor Failure'
            del upcur
            pass
    print arcpy.GetMessages()
    print shapeFire


print "Cursor and Geoprocessing Loop Closed"
arcpy.SetProgressorLabel('Creating GIF Animation')
arcpy.SetProgressorPosition(90)



# Create Map Document and add shapefiles
arcpy.env.workspace = sys.argv[3][:-8] # Go up a folder

# Map Specified in User Argument
mapName =  sys.argv[5]
mxd = arcpy.mapping.MapDocument(mapName)
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0]

# ListPoint FeatureClasses to add to map df
arcpy.env.workspace = sys.argv[3]
ffc = arcpy.ListFeatureClasses(feature_type='point')
j = 1

for ff in ffc:
        gname = 'mapgif{0}.gif'.format(j)
        layerObject = arcpy.mapping.Layer(ff)
        print layerObject.name
        arcpy.mapping.AddLayer(df, layerObject)
        arcpy.mapping.ExportToGIF(mxd, gname, df)
        arcpy.mapping.RemoveLayer(df, layerObject)
        print arcpy.GetMessages()
        j += 1
        print arcpy.GetMessages()
        #del mxd
mxd.saveACopy('mapcopy.mxd')
del mxd


##CREATE GIF ANIMATION

arcpy.env.workspace = txtFileDir[:-8]
# Thanks to pythoninformer for help generating this code block, similar code can be found at:
# https://www.pythoninformer.com/python-libraries/pillow/creating-animated-gif/

if not 'Final.gif' == 0:
    fp_out = "Final.gif"
else:
    fp_out = "Final{0}.gif".format(2)

gFrames = []
# Cluster Like Files 
fp_in =glob.glob(txtFileDir +'/' + "mapgif*.gif")

#Open all the GIFs
for f in fp_in:
    new_g = Image.open(f)
    gFrames.append(new_g)

# Save all GIFs as an animated GIF
gFrames[0].save(fp_out, format='GIF',
                append_images=gFrames[0:],
                save_all=True,
                optimize=False,
                duration=750, loop=0) 
# End of code block used from pythoninformer.

## WRITE HTML FILE
HTMLHead = '''<!DOCTYPE html>
<html>
<h1>{0}</h1>'''.format('Global Fire Detection Custom GIF Animation')

HTML = middle = '''
<body>{0}</body>
<img src='{1}' >\n'''.format('Course Final Project', fp_out)

HTMLEnd = '''
This is the where writeups go
</html>
'''

htmlfile = 'C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\output2.html'
with open(htmlfile,'w') as outf:
    outf.write(HTMLHead)
    outf.write(HTML)
    outf.write(HTMLEnd)
print '{0} created.'.format(htmlfile)



#Move Progress Bar
arcpy.SetProgressorLabel('Writing HTML File')
arcpy.SetProgressorPosition(100)




