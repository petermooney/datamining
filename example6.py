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
import matplotlib.pyplot as plt
import numpy as np

# we have to import some of the things we used in the plotting example previous

# we provide the filename to our CSV File
# remember that all the column indices are zero based - so the first column is index 0, second is index 1, etc
# we will just perform a simple formatted print out of the name, category, and country where the UNESCO
# Heritage site is located.
# In this example we want to read in the UNESCO data and we want to print it out to another file - 
# so we specify the input with the parameter filenameIn and the output file location as filenameOut. 

# The aim is to extract only UNESCO heritage sites which have a specific classification/category.
# We will specify the category or classification in the main method below

def extractCategoryFromData(filenameIn):

	# we are going to store the individual category names 
	# in a python dictionary 
	# see here for more details: http://www.tutorialspoint.com/python/python_dictionary.htm
	dictionaryOfCategory = {}
	lineNo = 1
	with open(filenameIn, 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter='\t')
		
		for row in csvreader:
			if lineNo != 1:
				category = row[9] ## this is where the category is placed. 
				
				# we add this element to the dictionary
				if category in dictionaryOfCategory:
					dictionaryOfCategory[category] = dictionaryOfCategory[category] + 1
				else:
					# first time we have seen this category in the data
					dictionaryOfCategory[category] = 1
			lineNo = lineNo + 1
		
	# just for clarity - we will just print out the dictionary. 
	
	pprint(dictionaryOfCategory)
	## pprint will allow python to just print the dictionary
	## line by line. Saves us writing out the dictionary ourselves.
	## We only need the dictionary printed for our own visual review. 
	
	return dictionaryOfCategory
			
			
def drawSampleBarChartPlot(dataLabels,dataValues,outputImageFileName,plotTitle,yLabel):
	
	fig = plt.figure()
	ax = fig.add_subplot(111)

	N = len(dataLabels) # get the number of data values
	
	indices = np.arange(N) # the x locations for the groups of data
	# This is from the numpy library which was imported above. 

	barWidth = 0.45  # the width of the bars

	## the bars themselves are rectangles drawn onto the chart
	rects1 = ax.bar(indices, dataValues, barWidth,color='yellow')

	ax.set_xlim(0,len(indices)) # the limits of the x axis
	ax.set_ylim(0,max(dataValues) + 5)
	# let's set the maximum y value just a little bigger than the maximum 
	# value in the data values which we want to plot. 
	
	ax.set_ylabel(yLabel) # the y axis label
	ax.set_title(plotTitle) # the title of the plot
	
	ax.set_xticks(indices) # the place where the marks will be on the x axis
	xtickNames = ax.set_xticklabels(dataLabels) 
	plt.setp(xtickNames, rotation=50, fontsize=9) # the font and rotation of the labels

	plt.title(plotTitle) # plot title. 
	# We are going to then save the pie chart as a PNG image file (nice for the web)
	plt.savefig(outputImageFileName)
	plt.close()

			
def drawBarChartVisualisation(inputDictionaryOfValues,plotTitle,yAxisLabel):
	
	# our data is in a dictionary
	# we need to break this out into x axis values
	# and then the labels.
	
	# so the dictionary needs to be split into two python lists
	
	categories = inputDictionaryOfValues.keys() # this will be the categories in our example
	values = inputDictionaryOfValues.values() # this will be the number of unesco sites in each category
	
	# we are going to use the method we wrote in the bar chart example
	
	drawSampleBarChartPlot(categories,values,"categories.png",plotTitle,yAxisLabel)			
			
def main():

	# we extract the categories from the unesco heritage data
	categories = extractCategoryFromData("unesco.csv")
	
	# we then call the method to draw the bar-chart for us. 
	# The bar chart is a nice way of visualising the data which we have extracted
	# Maybe for this small piece of data we could have maybe just printed out a 
	# simple table. 
	drawBarChartVisualisation(categories,"UNESCO Heritage Categories","UNESCO Sites per Category")

main()
