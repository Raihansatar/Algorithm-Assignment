# import geopy
from geopy.geocoders import Nominatim
from gmplot import gmplot
from geopy import distance

# creating a class for location information
class locationInfo:

    def __init__(self,name):
        self.name = name

    def setAddress(self,address):
        self.address = address

    def setCoor(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.coordinate = (self.latitude,self.longitude)

    def print_location_information(self):
        print(str(self.name)+" - ("+str(self.latitude)+", "+str(self.longitude)+")")


# creating an array to insert information class.
locationList = [locationInfo("Kuala Lumpur"),
                locationInfo("Jakarta"),
                locationInfo("Bangkok"),
                locationInfo("Taipei"),
                locationInfo("Hong Kong"),
                locationInfo("Tokyo"),
                locationInfo("Beijing"),
                locationInfo("Seoul")
                ]

# search for coordinate using geopy
geolocator = Nominatim(user_agent="Groutmm234234")
for x in range(len(locationList)):
    location = geolocator.geocode(locationList[x].name)
    locationList[x].setAddress(location.address)
    locationList[x].setCoor(location.latitude,location.longitude)
    locationList[x].print_location_information()


# marking location using gmplot
print(locationList[0].latitude)
print(locationList[0].longitude)

gmap = gmplot.GoogleMapPlotter(locationList[0].latitude,locationList[0].longitude, 13)

# 2. Placing/Mark all points(drop markers)
for x in range(len(locationList)):
    gmap.marker(locationList[x].latitude, locationList[x].longitude)

# 3. Get Distance
print("%15s|" % (''), end='')
for i in range(len(locationList)):
    print("%15s|" % (locationList[i].name), end='')
print('')

for i in range(len(locationList)):
    print("%-15s|" % locationList[i].name, end='')
    for j in range(len(locationList)):
        print("%12.3f km|" %(distance.distance(locationList[i].coordinate,locationList[j].coordinate).km), end = '')
    print('')

# 4. Plot Line

for i in range(len(locationList)):
    latList = []
    longList = []
    for j in range(len(locationList)):
        latList.append(locationList[i].latitude)
        longList.append(locationList[i].longitude)
        latList.append(locationList[j].latitude)
        longList.append(locationList[j].longitude)
        gmap.plot(latList, longList, 'cornflowerblue', edge_width=2)


# 5.draw the map
gmap.draw("Problem1.html")










