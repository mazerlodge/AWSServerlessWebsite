#!/usr/bin/python3

# Usage: KonaCap -e english -h hawaiian 
# Returns added,english,hawaiian or exists,english,hawaiian 

import sys 
from ArgTools import ArgParser

def showUsage():
	print("KonaCap -e english -h hawaiian\n" \
		  "Returns added,english,hawaiian or exists,english,hawaiian ")

# Global Vars 
ap = ArgParser(sys.argv)
capsDataFilename = "./data/KonaCaps.csv" 

# Validate and parse command line 
if (not ap.isInArgs("-e", True) 
	or not ap.isInArgs("-h", True)):
	showUsage()
	exit()

englishWord = ap.getArgValue("-e").encode('utf-8').decode('unicode_escape')
hawaiianWord = ap.getArgValue("-h").encode('utf-8').decode('unicode_escape') 
inLine = hawaiianWord + "," + englishWord

# Get data file and check for matching line
dataFile = open(capsDataFilename, "r") 
dataLines = dataFile.readlines()
dataFile.close() 

bLineFound = False 
for aLine in dataLines: 
	# parse line on comma, line looks like: papa'a la,sunburned
	if (inLine == aLine.strip()): 
		bLineFound = True
		break 

# If line not found add it and close the data file
if (not bLineFound): 
	dataFile = open(capsDataFilename, "a") 
	dataFile.write("\n" + inLine)
	dataFile.flush() 
	dataFile.close() 

# Output result 
if (bLineFound): 
	print("exists," + inLine)
else: 
	print("added," + inLine)
print() 
