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

def main():
	
	chosenAmenityType = "pub"
	pubName = "Queen"
	
	# this time we are going to supply part of the name of the pub we are looking for.
	resultsSpecificAmenityType = doAnSQLiteQuerySpecificAmenityType("OSM_BritishIsles_Amenities.sqlite",chosenAmenityType,pubName)

	outputCSVFile = open("Pubs_BritanIreland_Queen.csv","w")
	outputCSVFile.write("PubName,Longitude,Latitude\n")
	for amenity in resultsSpecificAmenityType:
		# remember there are going to be two columns returned from this
		# the first column is the amenity name, the second is the amenityName
		a = amenity[0]
		n = amenity[1]
		longitude = amenity[2]
		latitude = amenity[3]

		# into the file we want to print the amenity names and the lat long - we don't need the amenity type
		# we already know that this is a pub for this example
		
		outputCSVFile.write("\"{}\",{},{}\n".format(a,longitude,latitude))
		
	outputCSVFile.close()

# We could write this is a few different ways. For simplicity in terms of the lecture material
# we will simply just change the SQL Lite Query within the method here. As always there are many 
# different ways this method can be written

# The method returns the rows which are the result of the query - they can then be processed after this method
# has been executed and has finished. 

#Query purpose: 
# Find all amenities with a specific type - amenityType
# we will also supply part of the name of the amenity we are looking for - in this case the name of a pub
#This query will return every amenity in the database where the name of the amenity (AmenityName)
# is not an empty string - so it has string length > 0 (there are some characters). The AmenityName str
# value must include the contents of the variable pubName in some part of the string. 
# For example if pubName = "head" then an AmenityName could be "The King's Head" or "The Headway Inn"
# We will also return the latitude longitude. 
# 

def doAnSQLiteQuerySpecificAmenityType(databaseName,amenityType,pubName):
	# We start off with no query results. 
	queryResults = None
	# connect to the sqlite database
	con = sqlite.connect(databaseName)
	con.text_factory = str
	try: 
		with con:
			con.row_factory = sqlite.Row # this will allow us to index by column names from the table 
			cur = con.cursor()
			cur.execute('SELECT AmenityName,Amenity,Longitude,Latitude from amenities where amenity = ? and instr(AmenityName,?) and length(AmenityName) > 0',(amenityType,pubName,))

			queryResults = cur.fetchall()
			# fetch all of the query results from the database
			# these results shall now be returned to the calling environment method. 
		
	except sqlite.IntegrityError as e:
		print("An error occurred:", e.args[0])

	con.close()
	
	return queryResults	

main()
