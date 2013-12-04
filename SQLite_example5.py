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
	restaurantType = "pizza"
	restaurantsResults = findSpecificRestaurants("OSM_BritishIsles_Amenities.sqlite",restaurantType)

	outputCSVFile = open("BritanIreland_Restaurants.csv","w")
	outputCSVFile.write("RestaurantName,Longitude,Latitude\n")
	
	for r in restaurantsResults:
		n = r[0]
		longitude = r[1]
		latitude = r[2]
		# the query returns the Amenity Name and the longitude, latitude
		# notice the index numbers for r[]
		outputCSVFile.write("\"{}\",{},{}\n".format(n,longitude,latitude))
		
	outputCSVFile.close()

# We could write this is a few different ways. For simplicity in terms of the lecture material
# we will simply just change the SQL Lite Query within the method here. As always there are many 
# different ways this method can be written

# The method returns the rows which are the result of the query - they can then be processed after this method
# has been executed and has finished. 

#Query purpose: 
# We are looking specifically for restaurants. So we are going to hard-code this in. 
# We want to do some querying on the restaurantName - so we pass this in as a parameter
# to the method. 
# 

def findSpecificRestaurants(databaseName,restaurantName):
	# We start off with no query results. 
	queryResults = None
	# connect to the sqlite database
	con = sqlite.connect(databaseName)
	con.text_factory = str
	try: 
		with con:
			con.row_factory = sqlite.Row # this will allow us to index by column names from the table 
			cur = con.cursor()
			cur.execute('SELECT AmenityName,Longitude,Latitude from amenities where amenity = "restaurant" and AmenityName LIKE "%" || ? || "%" and length(AmenityName) > 0',(restaurantName,))

			queryResults = cur.fetchall()
			# fetch all of the query results from the database
			# these results shall now be returned to the calling environment method. 
		
	except sqlite.IntegrityError as e:
		print("An error occurred:", e.args[0])

	con.close()
	
	return queryResults	

main()
