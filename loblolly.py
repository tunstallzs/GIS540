"""
Zach Tunstall
zstunsta
loblolly.py
Purpose: read tab delimited data and write a modified version that contains field names and print user feedback
Usage: No arguments needed
"""
def getIndex(delimString, delimiter, name):
    '''Get position of item in a delimited string'''
    delimString = delimString.strip()
    lineList = delimString.split(delimiter)
    index = lineList.index(name)
    return index

infile = 'C:/gispy/data/ch19/RDUforest.txt'
outfile = 'C:/gispy/scratch/loblollyPine.txt'
# set count to zero
numlines = 0
# delimiter
d = '\t'
print "Reading file {0}...".format(infile)
try:
    with open(infile, 'r') as r:
        with open(outfile, 'w') as w:
            line = r.readline()
            dex = getIndex(line, d, 'SPECIES')
            # Return/ write the column names
            w.write(line)
            r.next()
            for line in r:
                lineList = line.split(d)
                lob = lineList[dex]
                # return lines with LP as species, add 1 to count 
                if lob == 'LP':
                    w.write(line)
                    numlines += 1
            print "{0} records with SPECIES 'LP' written to {1}".format(numlines, outfile)
except IOError:
    print '{0} does not exist'.format(infile)








