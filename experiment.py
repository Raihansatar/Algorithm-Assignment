from geopy.geocoders import Nominatim
from gmplot import gmplot
from geopy import distance
import itertools
import Cities
import BruteForce

# =================================================== PROBLEM 1 ======================================================== #

# creating a class for location information
class locationInfo:

    def __init__(self, name, text_path):
        self.name = name
        self.article = text_path

    def setAddress(self, address):
        self.address = address

    def setSV(self,sentiment_value):
        self.sv = sentiment_value

    def setCoor(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.coordinate = (self.latitude, self.longitude)

    def print_location_information(self):
        print(str(self.name) + " - (" + str(self.latitude) + ", " + str(self.longitude) + ")")


# 1. creating an array to insert information class.

locationList = [locationInfo("Kuala Lumpur","textfile/KualaLumpur.txt"),    #0
                locationInfo("Jakarta","textfile/Jakarta.txt"),             #1
                locationInfo("Bangkok","textfile/Bangkok.txt"),             #2
                locationInfo("Taipei","textfile/Taipei.txt"),               #3
                locationInfo("Hong Kong","textfile/HongKong.txt"),          #4
                locationInfo("Tokyo","textfile/Japan.txt"),                 #5
                locationInfo("Beijing","textfile/Beijing.txt"),             #6
                locationInfo("Seoul","textfile/Seoul.txt")                  #7
                ]

    # search for coordinate using geopy

print("Location - (Latitude, Longitude)")
geolocator = Nominatim(user_agent="Ben")
for x in range(len(locationList)):
    location = geolocator.geocode(locationList[x].name)
    locationList[x].setAddress(location.address)
    locationList[x].setCoor(location.latitude, location.longitude)
    locationList[x].print_location_information()

    # marking location using gmplot
gmap = gmplot.GoogleMapPlotter(locationList[4].latitude, locationList[4].longitude, 3)


# 2. Placing/Mark all points(drop markers)
for x in range(len(locationList)):
    gmap.marker(locationList[x].latitude, locationList[x].longitude)

print("")

print("The distance of the city(3 decimal place):")
print("%15s|" % (''), end='')
for i in range(len(locationList)):
    print("%15s|" % (locationList[i].name), end='')
print('')

distanceCountry = [[0] * len(locationList) for i in range(len(locationList))]

for i in range(len(locationList)):
    print("%-15s|" % locationList[i].name, end='')
    for j in range(len(locationList)):
        distanceCountry[i][j] = distance.distance(locationList[i].coordinate, locationList[j].coordinate).km
        print("%12.3f km|" % distance.distance(locationList[i].coordinate, locationList[j].coordinate).km, end='')
    print('')


# Kuala Lumpur --> Bangkok --> Beijing --> Seoul --> Tokyo --> Taipei --> Hong Kong --> Jakarta --> Kuala Lumpur
# 13930.557 km

# path = [0, 2, 6, 7, 5, 3, 4, 1, 0]
path = [0, 2, 6, 7, 3, 4, 1, 5, 0]
#path = [0, 3, 7, 6, 2, 1, 5, 4, 0]
print(len(path)-1)

def distance(path):
    sum = 0.0
    for y in range (len(path)-1):
        sum = sum + distanceCountry[path[y]][path[y+1]]
    return sum

print("The distance is ", end='')
print(distance(path))

# Kuala Lumpur --> Bangkok --> Beijing --> Seoul --> Taipei --> Hong Kong --> Jakarta --> Tokyo --> Kuala Lumpur
# The distance is 22059.093961229577
# [0, 1, 2, 3, 5, 6, 7, 4, 0]



# Sentiment path
# Kuala Lumpur --> Taipei --> Seoul --> Beijing --> Bangkok --> Jakarta --> Tokyo --> Hong Kong --> Kuala Lumpur
# [0, 3, 7, 6, 2, 1, 5, 4, 0]