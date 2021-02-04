"""
Zach Tunstall
zstunsta
filterFun.py
Purpose: Prints the index and value of the arguments
Usage: woot -3 C:/gispy/data/ch23/tester.gdb/c1;C:/gispy/data/ch23/tester.gdb/c2 C:/gispy/data/ch23/smallDir/poem.txt C:/gispy/data/ch23/rastTester.gdb/

"""
import sys,arcpy


i = 0
while i < 6:
    #iterate through user arguments and print to script tool or console
    x = "Argument {0}: {1}".format(i, sys.argv[i])
    i += 1
    arcpy.AddMessage(x)
    print x

