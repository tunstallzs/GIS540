"""
Zach Tunstall
zstunsta
loopFileSize.py
Tool for returning all files in a directory smaller than a user defined size
example C:/gispy/data/ch10/ 64
"""
import os, sys

#input argument file 
fname = sys.argv[1]

#retrieve basepath
base = os.path.abspath(fname)

#create directory list of files in same folder as input
dir = os.listdir(fname)

#2nd user argument to set byte limit
maxbyte = int(sys.argv[2])

for f in dir:
#create path
    h = base + '/' + f
#return file size in bytes
    g = int(os.path.getsize(h))
#conditional statement to print only files smaller or equal to 2nd user arg
    if g <= maxbyte:
        print '{0} is {1} bytes. '.format(f, g)

