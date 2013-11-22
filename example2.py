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

# we provide the filename to our CSV File
# remember that all the column indices are zero based - so the first column is index 0, second is index 1, etc
# we will just perform a simple formatted print out of the name, category, and country where the UNESCO
# Heritage site is located.
# In this example we want to read in the UNESCO data and we want to print it out to another file - 
# so we specify the input with the parameter filenameIn and the output file location as filenameOut. 

def readAndPrintContentFromCSVFile(filenameIn,filenameOut):

	outputFile = open(filenameOut,"w") # open the file for the output
	outputFile.write("Name\tCategory\tCountry\n") # this is the header line
	
	with open(filenameIn, 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		for row in csvreader:
			name = row[2]
			category = row[9]
			country = row[10]
			region = row[11]
			# to output data to a file we use WRITE instead of print. 
			# we have a tab separated file - can be opened by Excel etc
			outputFile.write("{}\t{}\t{}\n".format(name,category,country))
		
	outputFile.close() ## make sure to close the output file also. 	
def main():
	# we will read in the CSV file with the list of Unesco Heritage Sites world wide. 
	readAndPrintContentFromCSVFile("unesco.csv","MyUnescoList.csv")
	print ("Processing is now finished ")
main()
