"""
Zach Tunstall
zstunsta
writeHTML3.py
Purpose: create html page with dynamic content from an image directory
Usage: C:/gispy/data/ch11/pics C:/gispy/scratch/
"""
import os, sys

#input args
imageDir = sys.argv[1]
oDir1 = sys.argv[2]
#add forward slash to arg 2 if not alread there
if oDir1[-1] != '/':
    outDir = oDir1 + '/'
else:
    outDir = oDir1
#Get list of pics in directory
pics = os.listdir(imageDir)
picdir = []
relpath = os.path.relpath(imageDir, outDir)

# create directory of jpegs
for pic in pics:
    if 'jpg' in pic:
        picpath = os.path.join(relpath, pic)
        picdir.append(picpath)
picLength = len(picdir)

#HTML Header
half1 = '''<!DOCTYPE html>
<html>
    <body>
        <h1>Pics </h1>
'''
#HTML Footer
half3 = '''
    </body>
</html>'''
#HTML Insert first 4 photos from directory
half2 = '''
        <img src={0}>
        <img src={1}>
        <img src={2}>
        <img src={3}>'''.format(picdir[0], picdir[1], picdir[2], picdir[3])

#File name and write function
htmlFile = outDir + 'images3.html'
with open(htmlFile,'w') as ht:
    ht.write(half1)
    ht.write(half2)
    
    #If there are more than 4 jpegs in dirctory, print an extra
    if picLength > 4:
        half22 = ''''
        <img src={0}>
        '''.format(picdir[4])
        ht.write(half22)
        
    ht.write(half3)
    
#confirmation message
print '{0} created.'.format(htmlFile)