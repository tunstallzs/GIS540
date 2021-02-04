"""
Zach Tunstall
zstunsta
removeLines.py
Purpose: reads wheatYield.txt and remove invalid records, write the edited output.
Usage: C:/gispy/data/ch19/wheatYield.txt C:/gispy/scratch/
"""
import sys
infile = sys.argv[1]
outdir = sys.argv[2]
outfile = outdir + infile[19:-4] + '_edited.txt'
# delineate, align columns in text file 
d = '\t'
# Initiate Error count
errors = 0

try:
    with open(infile, 'r') as r:
        with open(outfile, 'w') as w:
            line = r.readline()
            # write header to output
            w.write(line)
            #split line into list format
            for line in r:
                list = line.split()
                for i in list:
                    # remove rows with negative numbers
                    if '-' in i:
                        list.remove(i)
                # remove all rows with missing elements
                if len(list) < 9:
                    errors += 1
                elif len(list) == 9:
                    w.write(line)
except IOError:
    print 'Could not find {0}'.format(infile)

print "Number of records with errors is: {0}".format(errors)
print 'Corrected file is: {0}'.format(outfile)






