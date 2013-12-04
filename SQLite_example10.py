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
import utm
# this library is available at https://pypi.python.org/pypi/utm

def main(): 
	# we need to specify our coordinates in UTM. 
	# Let's use a python library for this - because it is easy to work with Lat/Long
	# So we can just put in the lattitude and longitude and let Python do the work. 
	myUTMCoordinate = utm.from_latlon(53.3465404618, -6.29237818)
	myUTMCoordinateX = myUTMCoordinate[0]
	myUTMCoordinateY = myUTMCoordinate[1]
	distanceBufferKM = 2.56 ## remember this is the square of what we want. 
	amenityType = "post_office"
	
	pointsWithinBuffer = findPointsWithinDistanceBuffer("OSM_BritishIsles_Amenities.sqlite",myUTMCoordinateX,myUTMCoordinateY,distanceBufferKM,amenityType)
	
	# let's write the results to a CSV file - 
	outputCSVFile = open("PointsWithinBufferType.csv","w")
	
	outputCSVFile.write("Amenity,AmenityName,Latitude,Longitude\n")
	
	for p in pointsWithinBuffer: # remember our query returned all of the columns 
		# columns are zero-based indices - so latitude is the 5th column
		amenity = p[1]
		amenityName = p[2]
		latitude = p[4]
		longitude = p[3]
		outputCSVFile.write("{},\"{}\",{},{}\n".format(amenity,amenityName,latitude,longitude))
		
	outputCSVFile.close()

# Please note - this is much more efficient within a proper spatial database - but for the size of our dataset (only a few hundred thousand points this type of checking is fine
# We provide 4 variables include the databaseName
# we provide our UTMX coordinate, UTMY coordinate, and the distance squared of our buffer. 
# we must also specify the amenity type (for example amenity=post_box)

def findPointsWithinDistanceBuffer(databaseName,myUTMX, myUTMY, myDistanceSquared,amenityType):
	queryResults = None
	# connect to the sqlite database
	con = sqlite.connect(databaseName)
	con.text_factory = str
	try: 
		with con:
			con.row_factory = sqlite.Row 
			cur = con.cursor()
			# we must be careful to bind the correct variables to the parts of the SQL query
					
			cur.execute('SELECT * FROM amenities where amenity = ? and ( (? -UTMX)*(? -UTMX) + (? - UTMY)* (? - UTMY))/100000 <= ?',(amenityType,myUTMX,myUTMX,myUTMY,myUTMY,myDistanceSquared,))
			
			queryResults = cur.fetchall()

	except sqlite.IntegrityError as e:
		print("An error occurred:", e.args[0])

	con.close()
	
	return queryResults	

main()
