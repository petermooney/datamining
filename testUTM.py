import utm

#simple example of using the UTM converter library
# available https://pypi.python.org/pypi/utm

utmCoords = utm.from_latlon(53.3465404618, -6.29237818)

UTM_X = utmCoords[0]

UTM_Y = utmCoords[1]

print ("The UTM (x,y) coordinates for our specified lat/long are {},{}".format(UTM_X,UTM_Y))
