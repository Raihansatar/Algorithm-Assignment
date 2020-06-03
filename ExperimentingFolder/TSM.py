from itertools import permutations
from geopy.geocoders import Nominatim
from geopy import distance
import sys

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
    locationList[x].setCoor(location.latitude, location.longitude)
    locationList[x].print_location_information()




# using brute force to get the city distance.
def bruteforce(locationList):
    app = list(permutations(range(1, 8)));
    shortestDistance = sys.maxsize;
    index = 0;
    print(shortestDistance)
    listOfDistances = []
    for i in range(len(app)):
        currentDistance  = (distance.distance(locationList[0].coordinate, locationList[app[i][0]].coordinate).km)
        for j in range(len(app[i])-1):
            currentDistance = currentDistance + (distance.distance(locationList[app[i][j]].coordinate, locationList[app[i][j+1]].coordinate).km)

        currentDistance = currentDistance + (distance.distance(locationList[app[i][j+1]].coordinate,locationList[0].coordinate).km)
        print(currentDistance)
        listOfDistances.append(currentDistance)
        if(currentDistance<shortestDistance):
            shortestDistance = currentDistance;
            index = i;

    listOfDistances.sort();
    print(listOfDistances)
    print(index)
    print(app[index])

bruteforce(locationList);