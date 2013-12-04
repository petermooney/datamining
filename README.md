<h1>Introduction</h1>
This is a respository of Python scripts used to support a lecture on using Python for Data Mining. You can download and use these scripts for learning or teaching purposes. Please provide a link back to this repository if you do use them. 

<strong>The purpose</strong> of this repository is to demonstrate some very simple examples of data mining (data extraction, manipulation/query, visualisation) using Python. The lecture notes provided and the source code should make it reasonably straightforward to get Python up and running and hence these examples. 

The examples do not strive to be the most perfectly efficient pieces of code. Rather their aim is readability and clarity so that those students who do not wish to learn Python can understand the examples without getting confused by various aspects of what is a new programming language to them. 


<h2>Using the Shapefiles</h2>
Shapefiles are not just one file. They are a composite collection of four or five files. When you download the 'shapefiles' for either UK and Ireland borders or OpenStreetMap Roads in Greater Dublin please remember that you will need to download all of the files in that folder. Otherwise when you try to load this file into a GIS such as QGIS it will not work. 

<h4>Universal Traverse Mercator (UTM)</h4>

We use the very useful and simple to use library at https://pypi.python.org/pypi/utm for conversions from Latitude/Longitude to UTM. 

===============================================
<h2>OpenStreetMap Data</h2>

In the examples we make extensive use of the Points of Interest (specificially amenities) from the OpenStreetMap dataset for the United Kingdom and Ireland. I have prepared this dataset and it is available on the repository. The source of the data is OpenStreetMap and http://download.geofabrik.de/europe.html

The data was extracted in mid-November so it will become 'old' quickly. However this is not an issue for our examples as we do not specifically look at the temporal aspect of the data. 

