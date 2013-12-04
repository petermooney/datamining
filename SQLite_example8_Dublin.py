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
	# in here we will specify the coordinates of our bounding box
	# top latitude, left longitude, bottom latitude, right longitude
	pointsWithinGBB = findPointsWithinAGeographicBoundingBox("OSM_BritishIsles_Amenities.sqlite",53.4144,-6.3995,53.2402,-6.0315,"atm")
	
	# let's write the results to a CSV file - we will just write the coordinates
	outputCSVFile = open("PointsWithinGBB_ATM_Dublin.csv","w")
	
	outputCSVFile.write("Latitude,Longitude\n")
	
	for p in pointsWithinGBB: # remember our query returned all of the columns 
		# columns are zero-based indices - so latitude is the 5th column
		latitude = p[4]
		longitude = p[3]
		outputCSVFile.write("{},{}\n".format(latitude,longitude))
		
	outputCSVFile.close()

# Please note - this is much more efficient within a proper spatial database - but for the size of our dataset (only a few hundred thousand points this type of checking is fine
# Notice the order in which we will provide the coordinates of the geographic bounding box
# The query will return all of the rows which have amenities inside our bounding box. 
# The specific type of amenity is provided in the variable amenity_type

def findPointsWithinAGeographicBoundingBox(databaseName,topLat,leftLong,bottomLat,rightLong,amenityType):
	queryResults = None
	# connect to the sqlite database
	con = sqlite.connect(databaseName)
	con.text_factory = str
	try: 
		with con:
			con.row_factory = sqlite.Row 
			cur = con.cursor()
			# we must be careful to bind the correct variables to the parts of the SQL query
			cur.execute('SELECT * FROM amenities where latitude <= ?  and latitude >= ? and longitude >= ? and longitude <= ? and amenity = ?',(topLat,bottomLat,leftLong,rightLong,amenityType,))
			
			queryResults = cur.fetchall()

	except sqlite.IntegrityError as e:
		print("An error occurred:", e.args[0])

	con.close()
	
	return queryResults	

main()
