Title: Global Fire Hotspot Detection
Name: Zach Tunstall
Syopsis: The Suomi-NPP satellite contains the sensor named VIIRS
(Visible Infrared Imaging Radiometer Suite). The University of Maryland 
uses this sensor and a fire detection algorithm, based on NASA's MODIS 
mission, that detects fires based on location, strength, and confidence
of a correct detection.  This script tool retrieves this information from 
the online server at UMD and converts the information to a series of shapefiles.
The tool then creates a series of Gifs and creates an html file report.
Each GIF, and report are unique to the selected user inputs.
*********
Keywords: Fire Detection, Remote Sensing, VIIRS, MODIS, NASA, GIF, Animation, Hotspot
*********

In order to run this script you will need to install two python packages.
The First is pillow. This is also called PIL for python image library.  
PIL is responsible for combining and animating GIFs.

The second package is 'glob'. Some python environments already have glob installed.
In this script tool, glob creates lists of files with a similar name, or file type.
