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

import sqlite3 as sqlite
# we need to import sqlite. 
import matplotlib.pyplot as plt
import numpy as np

def main():

	popularAmenities = findMostPopularAmenities("OSM_BritishIsles_Amenities.sqlite")
	
	# we are going to use the method drawSampleBarChartPlot from previous examples
	# We need to setup a list to hold data values (numbers) and data labels (amenity types)
	names = []
	values = []
	for p in popularAmenities:
		# remember what is returned from the query - an amenity type and a number (the quantity)
		amType = p[0]
		amQty = p[1]
		names.append(amType) # add this to the names or data labels list
		values.append(amQty) # add this to the values or data values list
		
	drawSampleBarChartPlot(names,values,"amenitiesUKIreland.png","10 most popular amenities UK and Ireland","Total Quantity")


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
	ax.set_ylim(0,max(dataValues) + 100)
	# let's set the maximum y value just a little bigger than the maximum 
	# value in the data values which we want to plot. 
	
	ax.set_ylabel(yLabel) # the y axis label
	ax.set_title(plotTitle) # the title of the plot
	
	ax.set_xticks(indices) # the place where the marks will be on the x axis
	xtickNames = ax.set_xticklabels(dataLabels) 
	plt.setp(xtickNames, rotation=20, fontsize=9) # the font and rotation of the labels

	plt.title(plotTitle) # plot title. 
	# We are going to then save the pie chart as a PNG image file (nice for the web)
	plt.savefig(outputImageFileName)
	plt.close()


# We could write this is a few different ways. For simplicity in terms of the lecture material
# we will simply just change the SQL Lite Query within the method here. As always there are many 
# different ways this method can be written

# The method returns the rows which are the result of the query - they can then be processed after this method
# has been executed and has finished. 

#Query purpose: 
# This query is reasonably simple - just find the quantity or frequency of each different amenity - ie hospital, pub, school, etc. Just return the 10 most frequently occuring - notice how we limit the number of rows which have been returned from the query
# 

def findMostPopularAmenities(databaseName):
	# We start off with no query results. 
	queryResults = None
	# connect to the sqlite database
	con = sqlite.connect(databaseName)
	con.text_factory = str
	try: 
		with con:
			con.row_factory = sqlite.Row # this will allow us to index by column names from the table 
			cur = con.cursor()
			cur.execute('SELECT Amenity, count(*) as N from amenities group by amenity  order by N desc LIMIT 10')

			queryResults = cur.fetchall()
			# fetch all of the query results from the database
			# these results shall now be returned to the calling environment method. 
		
	except sqlite.IntegrityError as e:
		print("An error occurred:", e.args[0])

	con.close()
	
	return queryResults	

main()
