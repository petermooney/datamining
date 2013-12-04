### This is source code used for an invited lecture on Data Mining using Python for 
### the Institute of Technology at Blanchardstown, Dublin, Ireland
### Lecturer and presenter: Dr. Peter Mooney
### email: peter.mooney@nuim.ie
### Date: November 2013
###
### The purpose of this lecture is to provide students with an easily accessible overview, with working 
### examples of how Python can be used as a tool for data mining. 
### For those using these notes and sample code: This code is provided as a means of showing some basic ideas around 
### data extraction, data manipulation, and data visualisation with Python. 
### The code provided could be written in many different ways as is the Python way. However I have tried to keep things simple and practical so that students can get an understanding of the process of data mining rather than this being a programming course in Python. 
###
### If you use this code - please give me a little citation with a link back to the GitHub Repo where you found this piece of code: https://github.com/petermooney/datamining

import csv
from pprint import pprint
# we provide the filename to our CSV File
# remember that all the column indices are zero based - so the first column is index 0, second is index 1, etc
# we will just perform a simple formatted print out of the name, category, and country where the UNESCO
# Heritage site is located.
# In this example we want to read in the UNESCO data and we want to print it out to another file - 
# so we specify the input with the parameter filenameIn and the output file location as filenameOut. 

# The aim is to extract only UNESCO heritage sites which have a specific classification/category.
# We will specify the category or classification in the main method below

def extractContinentsFromData(filenameIn):
	# we are going to store the individual continent names in a python dictionary 
	# see here for more details: http://www.tutorialspoint.com/python/python_dictionary.htm
	dictionaryOfContents = {}
	lineNo = 1
	with open(filenameIn, 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter='\t')
		
		for row in csvreader:
			if lineNo != 1:
				continent = row[11]
				
				# we add this element to the dictionary
				if continent in dictionaryOfContents:
					dictionaryOfContents[continent] = dictionaryOfContents[continent] + 1
				else:
					# first time we have seen this continent in the data
					dictionaryOfContents[continent] = 1
			lineNo = lineNo + 1
	# just for clarity - we will just print out the dictionary. 
	pprint(dictionaryOfContents)
	## pprint will allow python to just print the dictionary
	## line by line. Saves us writing out the dictionary ourselves.
	## We only need the dictionary printed for our own visual review. 
	
	return dictionaryOfContents
			
def main():

	continents = extractContinentsFromData("unesco.csv")

main()
