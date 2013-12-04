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
import matplotlib.pyplot as plt

# this is a simple example of how to draw a pie chart using Python and MatplotLib
# You will need matplotlit installed for this to work. 

# this time we are making our code a little more useful - we are going to pass in four different parameters
# we need to pass in the list of dataLabels, the list of data Values for those labels, and the name of the file 
# which we want to save the piechart as, and the plot title

def drawSamplePieChartPlot(dataLabels,dataValues,outputImageFileName,plotTitle):
	
	plt.pie(dataValues, labels=dataLabels,autopct='%1.1f%%',startangle=90)
	plt.axis('equal')
	plt.title(plotTitle)
	# We are going to then save the pie chart as a PNG image file (nice for the web)
	plt.savefig(outputImageFileName)
	plt.close()
	
def main():
	degreeGrantingUniversitiesPerState = ["California","New York","Pennsylvania","Texas","Ohio"]
	
	numberOfUniversities = [399,307,260,208,194]
	
	drawSamplePieChartPlot(degreeGrantingUniversitiesPerState,numberOfUniversities,"universitiesPerState.png","Percentage of Degree Granting Universities per US State (top 5)")
	
	# we can actually draw any number of pie charts now using this approach - using the one script.
	
	teams = ["Team A","Team B","Team C","Team D","Team E","Team F"]
	percentages = [15,30,12,23,10,10]
	drawSamplePieChartPlot(teams,percentages,"pieChart2.png","Simple example of a second pie chart")
	
main()
