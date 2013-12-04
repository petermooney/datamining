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
import numpy as np

# this is a simple example of how to draw a bar chart using Python and MatplotLib
# you will also need a libary called NUMPY - which allows some fancy numerical calculations to be 
# be performed. 
# You will need matplotlit installed for this to work. 
# You will need to ensure you have numpy installed. 

# As before we will save the output chart as a PNG file. 
# Again we will have our actual data in the list dataValues
# we will have our labels for those data in the list dataLabels
# We need to provide a yLabel for the graph so that we can name that axis properly

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


def main():
	xTickMarks = ["Real M","Paris","Bayern","Atletico","Chelsea","Man. City","Barca","Leverkusen","Napoli"]
	xValues = [14,13,12,12,11,11,9,8,7]
	drawSampleBarChartPlot(xTickMarks,xValues,"championsLeagueGoals.png","Goals scored in Champions League - to Nov 2013","Goals Scored")

main()
