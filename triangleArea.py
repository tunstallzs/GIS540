"""
Zach Tunstall
zstunsta
triangleArea.py
Purpose: Script for creating a script tool in ArcGIS that calculates area of a triangle based on user inputs/
Usage: 5.6 9
"""
import sys, arcpy

def triArea(b1, h1):
    '''Calculate Area of Triangle'''
    Area = (b1 / 2) * h1
    msg = "The area of the triangle is {0}.".format(Area)
    return msg

#user arguments for height and base
btri = float(sys.argv[1])
htri = float(sys.argv[2])

#call function
x = triArea(btri, htri)

#print to console and as feedback in GUI
print x
arcpy.AddMessage(x)
