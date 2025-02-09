# import geopy
from geopy.geocoders import Nominatim
from gmplot import gmplot
from geopy import distance
# import tsp
from ExperimentingFolder.DONE import TSPdynamic


# creating a class for location information
class locationInfo:

    def __init__(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setCoor(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.coordinate = (self.latitude, self.longitude)


    def print_location_information(self):
        print(str(self.name) + " - (" + str(self.latitude) + ", " + str(self.longitude) + ")")


# creating an array to insert information class.
locationList = [locationInfo("Kuala Lumpur"),   # 0
                locationInfo("Jakarta"),        # 1
                locationInfo("Bangkok"),        # 2
                locationInfo("Taipei"),         # 3
                locationInfo("Hong Kong"),      # 4
                locationInfo("Tokyo"),          # 5
                locationInfo("Beijing"),        # 6
                locationInfo("Seoul")           # 7
                ]

# search for coordinate using geopy
geolocator = Nominatim(user_agent="Groutmm234234")
for x in range(len(locationList)):
    location = geolocator.geocode(locationList[x].name)
    locationList[x].setAddress(location.address)
    locationList[x].setCoor(location.latitude, location.longitude)
    locationList[x].print_location_information()

# marking location using gmplot
gmap = gmplot.GoogleMapPlotter(locationList[0].latitude, locationList[0].longitude, 13)

# 2. Placing/Mark all points(drop markers)
for x in range(len(locationList)):
    gmap.marker(locationList[x].latitude, locationList[x].longitude)

print("")
# 3. Get Distance
print("The distance of the city(3 decimal place):")
print("%15s|" % (''), end='')
for i in range(len(locationList)):
    print("%15s|" % (locationList[i].name), end='')
print('')

distanceCountry = [[0] * len(locationList) for i in range(len(locationList))]

for i in range(len(locationList)):
    print("%-15s|" % locationList[i].name, end='')
    for j in range(len(locationList)):
        distanceCountry[i][j] = (distance.distance(locationList[i].coordinate, locationList[j].coordinate).km)
        print("%12.3f km|" % (distance.distance(locationList[i].coordinate, locationList[j].coordinate).km), end='')
    print('')

# mat = distanceCountry
short = TSPdynamic.travel(distanceCountry)[1]
costTPS = TSPdynamic.travel(distanceCountry)[0]

print("\nThe shortest path is:")
for i in range(len(short) - 1):
    print(locationList[short[i]].name + " --> ", end="")
print(locationList[short[len(short) - 1]].name)

print("\nwith the total distance: %.3f km" % costTPS)

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

# plot the shortest route line
latShort = []
longShort = []
for j in range(len(short)):
    latShort.append(locationList[short[j]].latitude)
    longShort.append(locationList[short[j]].longitude)
    gmap.plot(latShort, longShort, 'red', edge_width=2)

# 5.draw the map
gmap.draw("Problem1.html")
