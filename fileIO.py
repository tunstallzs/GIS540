"""
Zach Tunstall
zstunsta
fileIO.py
script to use common file handling operations
"""
# a) Open a file named 'C:/gispy/scratch/test.txt' for writing
ftest = 'C:/gispy/scratch/test.txt'
with open(ftest, 'w') as f:
# b) Write the number 365 on the first line of the file
    f.write('356\n')
# c) Write tab separated week days on the next line of the file.
    f.write('Monday\tTuesday\tWednesday\tThursday\tFriday\n')
# d) Write the numbers 1, 2, and 3 separated by commas on the third line
    f.write('1, 2, 3')
# e) Close the file.
    f.close()
# f) Open the same file for reading.
with open(ftest, 'r') as r:
# g) Read the first line and print the results
    lin = r.readline()
    print lin
# h) Read the second line, split the line on the tabs and print the results one day per line
    lin2 = r.readline()
    listlin = lin2.split('\t')
    for i in listlin:
        print i
# i) Read the third line, split the line on the commas, sum the numbers, and print the results.
    lin3 = r.readline()
    list3 = lin3.split(',')
    sumlist = []
    for x in list3:
        x = int(x)
        sumlist.append(x)
    print "The sum is {0}".format(sum(sumlist))
# j) Close the file.
    r.close()