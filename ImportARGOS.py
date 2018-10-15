##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: John.Fay@duke.edu (for ENV859)
##---------------------------------------------------------------------

#Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

#Open the ARGOS data file for reading
inputFileObj = open(inputFile, 'r')

#Get the first line so we can loop
lineString = inputFileObj.readline()
print(lineString)

while lineString:
    #set code to run only if the line contains "Date :"
    if "Date :" in lineString:
        #Split the line string into a list
        lineList = lineString.split()#split by space
        print(lineList)

        #Get attributes from first line
        tagID = lineList[0]
        print(tagID)
        #print(lineString)
        break #So it doesnt keep running
    
    #Get the next line
    lineString = inputFileObj.readline()