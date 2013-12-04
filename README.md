This is a respository of Python scripts used to support a lecture on using Python for Data Mining. 

USING THE SHAPEFILES

Shapefiles are not just one file. They are a composite collection of four or five files. When you download the 'shapefiles' for either UK and Ireland borders or OpenStreetMap Roads in Greater Dublin please remember that you will need to download all of the files in that folder. Otherwise when you try to load this file into a GIS such as QGIS it will not work. 

Universal Traverse Mercator (UTM)

We use the very useful and simple to use library at https://pypi.python.org/pypi/utm for conversions from Latitude/Longitude to UTM. 

===============================================
<h2>OpenStreetMap Data</h2>

In the examples we make extensive use of the Points of Interest (specificially amenities) from the OpenStreetMap dataset for the United Kingdom and Ireland. I have prepared this dataset and it is available on the repository. The source of the data is OpenStreetMap and http://download.geofabrik.de/europe.html

The data was extracted in mid-November so it will become 'old' quickly. However this is not an issue for our examples as we do not specifically look at the temporal aspect of the data. 

