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


import matplotlib.pyplot as plt

# this is a simple example of how to draw a pie chart using Python and MatplotLib
# You will need matplotlit installed for this to work. 

def drawSamplePieChartPlot():
	# we have 5 lecturers and we have the number of exam papers which 
	# each of the lecturers have had to mark. 
	lecturers = ['Peter','Laura','James','Jennifer','Patrick']
	examPapersMarked = [14, 37, 22, 16,80]
	colors = ['purple', 'blue', 'green', 'yellow','red']
	
	plt.pie(examPapersMarked, labels=lecturers, colors=colors,autopct='%1.1f%%',startangle=90)
	plt.axis('equal')
	# We are going to then save the pie chart as a PNG image file (nice for the web)
	plt.savefig("PieChartExample.png")
def main():
	drawSamplePieChartPlot()
main()
