"""
GlobalFires.Py
Zach Tunstall
** Start Date must be after Febuary 4 2020
Purpose: Writes table data from online database to txt file, Clean Data, Create Map Document, Create GIF, Create html file
Usage: [ Start Date, End Date, File Dir, Number of {days} Map Document, Confidence Level ]
Usage: example: 05/30/2020 06/4/2020 "..\Data\webtext\" 3 "..\..\Data\GIFtry2.mxd" 75
"""

import datetime, urllib2
import arcpy, os, sys
from PIL import Image # Python Image Library not a default package "pip install pillow"
import glob # Unix path patern expansion, not included as default package

def printArc(message):
    '''Print message for script tool and standard output.'''
    print message
    arcpy.AddMessage(message)
    arcpy.SetProgressorLabel(message)

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

def clearGIFs(folder1, fltype='gif'):
    '''Deletes files from indicated folder'''
    for root, dirs, files in os.walk(folder1):
        os.chdir(root)
        for f in files:
            if f.endswith(fltype):
                os.remove(f)
                print 'removed {0}'.format(f)

def gifMaker(continent):
    '''Select GIFs based on Name and combine them into an animated GIF'''
    cGif = continent + 'Out.gif'
    gifFrames = []
    
# Thanks to pythoninformer for help generating this function, example code can be found at:
# https://www.pythoninformer.com/python-libraries/pillow/creating-animated-gif/
    inGif = glob.glob(continent+'*.gif')
    for G in inGif:
        newGif = Image.open(G)
        gifFrames.append(newGif)
    gifFrames[0].save(cGif, format='GIF',
                      append_images=gifFrames[0:],
                      save_all=True,
                      optimize=False,
                      duration=750, loop=0)
# End of Code from pythoninformer.com **
    gifFrames = []
    return os.path.join('Data',cGif)

# Remove Gifs From Previous runs.
try:
    clearGIFs('../Data')
except:
    mess = 'Close the script or script tool and re run'
    printArc(mess)
    pass


## SET ENVIRONMENT ##
# Initialize Progress Bar
arcpy.SetProgressor('step', 'Preparing Script', 0, 100, 1)
arcpy.SetProgressorPosition(0)
txtFileDir = sys.argv[3]
# Set workspace env
arcpy.env.workspace = txtFileDir
arcpy.env.overwriteOutput = 1
arcpy.SpatialReference(3857) # Web Mercator

## SET VARIABLES ##
# Call Calendar function on Start and End Date Arguments
arg2 = sys.argv[2]
arg1 = sys.argv[1]
startDate = calArgs(arg1)
endDate = calArgs(arg2)

# Text File Data Source
website = 'http://viirsfire.geog.umd.edu/web_data/GLOBAL/NOAA/20200930_NOAA.txt'
# empty  list for websites
websiteList = [ ]
# Day interval.
mwd = int(sys.argv[4])
# Amount of change in date range by this amount.
delta = datetime.timedelta(days=mwd)
# Confidence Interval to filter by
confidenceLevel = sys.argv[6]
# Prepare List for listing .txt files.
xFiles  = []
# Prepare List to append single GIFs
gFrames = []
# Time variable for alt name Final GIF
t = time.clock()
# Get Legend 
Leg = "C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\Data\Legend.JPG"
#Move Progress Bar
arcpy.SetProgressorLabel('Creating List of Websites')
arcpy.SetProgressorPosition(10)
Message = " Start- {0} ;  End- {1}".format(arg1, arg2)
printArc(Message)


## CREATE WEBSITE LIST ##
# Uses start, end and time delta to create list of URL File locations
apos= 10 # Gui Position
while startDate <= endDate:
    startDate += delta
    # Thanks to Peter Mortensen at https://stackoverflow.com/questions/8906926/formatting-timedelta-objects for this code block
    dateReplace = str(startDate.strftime('%Y%m%d')) # Variable name = startDate
    websiteList.append(website.replace(website[51:59], dateReplace)) # Adds Website to Website List
    #Progress Bar
    apos += 1
    arcpy.SetProgressorPosition(apos)
#Update GUI Messages
Message = "Data Obtained From {0}".format(website)
printArc(Message)
#Move Progress Bar
arcpy.SetProgressorLabel('Creating Cutom Website URL')
arcpy.SetProgressorPosition(20)


## WRUTE FILE IO ##
#Move Progress Bar
arcpy.SetProgressorLabel('Writing Website to File in Directory')
arcpy.SetProgressorPosition(30)
posx = 31 # GUI Position
# Parsing list of websites and writing their contents to a folder of text files.

for site in websiteList:
    # Write each line of website to a new text file.
    newTextFile = site[-17:]
    with open(newTextFile, 'w') as tout:
        for p in urllib2.urlopen(site):
            tout.write(p)
        arcpy.AddMessage("New file at {0}".format(newTextFile))
        print "New file at {0}".format(newTextFile)
        tout.close()
        # Increment Progress Bar
    posx += 1
    arcpy.SetProgressorPosition(posx)
    # Print status update to tool window.
arcpy.AddMessage('Text Files Created in {0}'.format(txtFileDir))
# Move Progress Bar.
arcpy.SetProgressorLabel('Converting Text to Shape Files (this might take a while)')
arcpy.SetProgressorPosition(50)


## GEOPROCESSING LOOP ##
# Get List of Text Files for Iteration.
arcpy.env.workspace = '../../Data/webtext'
xFiles = arcpy.ListFiles("*.txt")
# For each txt file, create xy event table, create layer file, then create point shapefile.
# Update Cursor filters fire data with low confidence.
xListLen = len(websiteList)

# This block creates output names for shapefiles
for x in xFiles[:xListLen]: 
    fLyrName = '{0}FireXY'.format(x[0:8])
    fOutName = '{0} Fire.lyr'.format(x[0:8])
    # Change layer name to shapefile name
    shapeFire = '{0}.shp'.format(x[0:8])
    try:
        # Write new file layers in the webtext folder if not done already.
        if  fLyrName not in txtFileDir:
                arcpy.MakeXYEventLayer_management(x, 'Longitude', 'Latitude', fLyrName)  
                arcpy.SaveToLayerFile_management(fLyrName, fOutName)
                arcpy.FeatureToPoint_management(fOutName, shapeFire, 'INSIDE')
                print arcpy.GetMessages() 
        else:
            pass
    except:
        print 'File Lock Issue Caused Tool to Behave Unexpectedly'
        print arcpy.GetMessages()
        pass

    #  Use Search Cursor to filter false positives (low confidence).
    L = arcpy.ListFiles('*.shp')
    fName = '*'
     # Confidence level from User Input 6
    where = "Confidence < {0}".format(confidenceLevel)

    for inTab in L:
        try:
            count = 0
            # Update Cursor Uses deletes rows with confidence level below user input.
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
Mess =  "Cursor and Geoprocessing Loop Closed Successfully"
printArc(Mess)


# Move Progress Bar
arcpy.SetProgressorLabel('Exporting Data Frames To GIF Format')
arcpy.SetProgressorPosition(75)

# Find Map Document and add shapefiles
# Set Directory and workspace

newDir = sys.argv[3]
arcpy.env.workspace = newDir

# Map Specified in User Argument
mapName = "C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\Data\GIFtry2.mxd"

mxd = arcpy.mapping.MapDocument(mapName)
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0]

# ListPoint FeatureClasses to add to map df
arcpy.env.workspace = './webtext'
ffc = arcpy.ListFeatureClasses(feature_type='point')
arcpy.env.workspace = newDir
j = 0
# For Fire Feature in Fire Feature Class initalize Map Layer.
try:
    for ff in ffc: 
        layerObject = arcpy.mapping.Layer(ff)
    # For Every Dataframe in the Map Document Add Layer, Add Symbology, Export as GIF
        for df in dfs:
            k = df.name
            arcpy.ApplySymbologyFromLayer_management(layerObject, 'fire2.lyr')
            arcpy.mapping.AddLayer(df, layerObject)
            gname = '{0}{1}.gif'.format(k, j)
            arcpy.mapping.ExportToGIF(mxd, gname, df)
        j += 1
        Mess = 'Symbology Created'.format(k)
        printArc(Mess) 
    del mxd
except:
    messy = 'Error Adding Symbology'
    printArc(messy)
    del mxd
    pass

# Move Progress Bar
arcpy.SetProgressorLabel('Creating GIF Animation')
arcpy.SetProgressorPosition(90)
# Move up one level in Directory
##arcpy.env.workspace =newDir 


## CREATE GIF ANIMATION ##

# Set Directory to search GIFS
os.chdir('C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\Data')

World = gifMaker('World')
NAmerica = gifMaker('NAmerica')
SAmerica = gifMaker('SAmerica')
Europe = gifMaker('Europe')
Africa = gifMaker('Africa')
Australia = gifMaker('Australia')
Asia = gifMaker('Asia')


## WRITE HTML FILE
HTMLHead = '''<!DOCTYPE html>
<html>
<h1>Global Fire Detection From {0} to {1} with {2} Day Intervals</h1>'''.format(arg1, arg2, sys.argv[4])

HTML = middle = '''
<img src='{0}' >\n
<img src='{1}' >\n
<img src='{2}' >\n
<img src='{3}' >\n
<img src='{4}' >\n
<img src='{5}' >\n
<img src='{6}' >\n
<img src='{7}' >
'''.format(World, NAmerica, SAmerica, Europe, Africa, Australia, Asia, Leg)

HTMLEnd = '''
<body>Disclaimer: Neither The Content Creator nor NC State University shall not
be held liable for improper or incorrect use of the data described and/or contained
herein. These data and related graphics are not legal documents and are not
intended to be used as such. The information contained in these data is dynamic and
may change over time. The data are not better than the original sources from which
they were derived.  It is the responsibility of the data user to use the data appropriately
and consistent within the limitations of geospatial data in general and these data in
particular. The related graphics are intended to aid the data user in acquiring relevant
data; it is not appropriate to use the related graphics as data. NC State and the
Content Creator give no warranty, expressed or implied, as to the accuracy, reliability,
or completeness of these data. It is strongly recommended that the data is directly
acquired from an NC State University server and not indirectly through other sources
which may have changed the data in some way.  Although these data have been
processed successfully on a computer system associated with NC State University,
no warranty expressed or implied is made regarding the utility of the data on another
system or for general or scientific purposes, nor shall the act of distribution constitute
any such warranty. This disclaimer applies both to individual use of the data and
aggregate use with other data.</body>
</html>'''

htmlfile = '..\output2.html'
with open(htmlfile,'w') as outf:
    outf.write(HTMLHead)
    outf.write(HTML)
    outf.write(HTMLEnd)
print '{0} created.'.format(htmlfile)



#Move Progress Bar
arcpy.SetProgressorLabel('Writing HTML File')
arcpy.SetProgressorPosition(100)


