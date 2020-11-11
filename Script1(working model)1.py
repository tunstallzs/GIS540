"""
Final Py
Zach Tunstall
Purpose: Writes table data from online database to txt file, Clean Data, Create Map Document, Create GIF, Create html file
Usage: [ Start Date, End Date, File Dir(Relative Dir), Number of {days, weeks , years} Map Document, Confidence Level]
Usage: example: 05/28/2020 06/4/2020 "C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\webtext" 1 "C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\GIFtry2.mxd" 75'
"""
import datetime, urllib2
import arcpy, os, sys, traceback
from PIL import Image # Python Image Library
#import glob
"""
##GUI Test Area##
#mapName2 =  "C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\GIFtry2.mxd"
#arcpy.mapping.ExportToGIF(mapName2, 'takeOne.gif')

# Create Map Document and add shapefiles
arcpy.env.workspace = sys.argv[3]
arcpy.SpatialReference(3857) # Web Mercator
# Map Specified in User Argument
mapName =  "C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\GIFtry1.mxd"
mxd = arcpy.mapping.MapDocument(mapName)
dfs = arcpy.mapping.ListDataFrames(mxd)
df = dfs[0]


for ff in ffc:
    layerObject = arcpy.mapping.Layer(ff)
    arcpy.mapping.AddLayer(df, layerObject)
    print arcpy.GetMessages()
    
mxd.saveACopy('mapcopy.mxd')
del mxd, addLayer

ele = arcpy.mapping.ListLayoutElements(mxd)

# Print a list of layout Elements
for e in ele:
    print e.name
print ele


# Export to GIF.
outGIF = 'C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\TrialByFire2.GIF'
#arcpy.mapping.ExportToJPEG(mxd, outJpeg, df)
#arcpy.mapping.ExportToGIF(mxd, outGIF, df)

# ListPoint FeatureClasses to add to map df
ffc = arcpy.ListFeatureClasses(feature_type='point')
"""


## This is where Functional Code Begins

# Shorten this code with function.

#Change format of start date for file and website iteration
arg1 = sys.argv[1]
argStart = arg1[:10]
startListStr = argStart.split('/')
startListNum = list(map(int, startListStr))
startDay = startListNum[1]
startMonth = startListNum[0]
startYear = startListNum[2]
startDate = datetime.date(startYear, startMonth, startDay)
#startDate1 = datetime.datetime.strptime(argStart,'%m/%d/%Y').strftime('%Y%m%d')

#Change format of end date for file and website iteration
arg2 = sys.argv[2]
argEnd = arg2[:10]
endListStr = argEnd.split('/')
endListNum = list(map(int, endListStr))
endDay = endListNum[1]
endMonth = endListNum[0]
endYear = endListNum[2]
endDate = datetime.date(endYear, endMonth, endDay)
#endDate1 = datetime.datetime.strptime(argEnd,'%m/%d/%Y').strftime('%Y%m%d')

# folder location to write txt files 
txtFileDir = sys.argv[3]

arcpy.AddMessage( " Start- {0} ;  End- {1}".format(arg1, arg2))
##Currently unused statements that may be useful later##

###print dayrange(starDate, endDate)
###dateReplace = startDate.strftime('%Y%m%d')
###siteStart = website.replace('20200930', startDate1) # website[51:59]
###siteEnd = website.replace('20200930', endDate1)
###siteOriginal = 'http://viirsfire.geog.umd.edu/web_data/GLOBAL/NOAA/20200930_NOAA.txt'
###arcpy.AddMessage( " Start- {0} ;  End- {1}".format(startDate, endDate))



website = 'http://viirsfire.geog.umd.edu/web_data/GLOBAL/NOAA/20200930_NOAA.txt'
# empty website list
websiteList = [ ]


# Amount of change in date range by this amount.
# Month, week, or day interval.
mwd = int(sys.argv[4])
delta = datetime.timedelta(days=mwd)


# Loop through dates create list of websites
while startDate <= endDate:
    startDate += delta
    dateReplace = str(startDate.strftime('%Y%m%d'))
    websiteList.append(website.replace(website[51:59], dateReplace))
arcpy.AddMessage("{0}".format(websiteList))

# Parsing list of websites and writing their contents to a folder of text files
for site in websiteList:
    # Write each line of website to a new text file
    newTextFile = os.path.join(txtFileDir, site[-17:])
    with open(newTextFile, 'w') as tout:
        for p in urllib2.urlopen(site):
            tout.write(p)
        arcpy.AddMessage("New file at {0}".format(newTextFile))
        print "New file at {0}".format(newTextFile)


txtFileDir = sys.argv[3]
# Set workspace env
arcpy.env.workspace = txtFileDir
#arcpy.env.overwriteOutput = 1
arcpy.SpatialReference(3857) # Web Mercator
# Get list of txt file in directory.
xFiles = arcpy.ListFiles({'txt'})
# Print status update to tool window.
arcpy.AddMessage('Text Files {0} Created in {1}'.format(xFiles, txtFileDir))


# Geoprocessing Loop Start:
# For each txt file, create xy event table, create layer file, then create point shapefile
# Update Cursor filters fire data with low confidence.
for x in xFiles:
    fLyrName = '{0}FireXY'.format(x[0:8])
    fOutName = os.path.join(txtFileDir,'{0}Fire.lyr'.format(x[0:8]))

    # Change layer name to shapefile name
    shapeFire = os.path.join(txtFileDir,'{0}Fire.shp'.format(x[0:8]))

    arcpy.MakeXYEventLayer_management(x, 'Longitude', 'Latitude', fLyrName)
    arcpy.SaveToLayerFile_management(fLyrName, fOutName)
    arcpy.FeatureToPoint_management(fOutName, shapeFire, 'INSIDE') 
    print arcpy.GetMessages()
    
# # Use Search Cursor to filter false positives (low confidence)
    arcpy.env.workspace = "C:\Users\LENOVO\Desktop\GIS 540 Programming\Final Project\webtext"
    L = arcpy.ListFiles('*.shp')
    Name = '*'
    confidenceLevel = 60 # Set to User Input
    where = "Confidence < {0}".format(confidenceLevel)
    for inTab in L:
        count = 0
        with arcpy.da.UpdateCursor(inTab, fName, where) as upcur:
            for row in upcur:
               count += 1
               upcur.deleteRow()
            print 'deleting row {0}'.format(row[0])
        print "Number of rows deleted {0}".format(count)
    del upcur
##    except RuntimeError:
##        print 'An error occurred.'
##        print arcpy.GetMessages()
##        traceback.print_exc()
##        del upcur
    print arcpy.GetMessages()
    print shapeFire

##     This is where Functional Code Ends
    try       :
        arcpy.OptimizedHotSpotAnalysis_stats(shapeFire, 'FRP(MW)')
        print 'SAUL GOODMAN'
        print arcpy.GetMessages()
        traceback.print_exc()

##    except  ...:
##        print 'Invalid Date'
##        print traceback.print_exc()
    
    except AttributeError:
        print "FAILLLLLLFAILLLLLL"
        print arcpy.GetMessages()
    except NameError:
        print "FAILLLLLL"
        print arcpy.GetMessages()











