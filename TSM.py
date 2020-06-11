from itertools import permutations
from geopy.geocoders import Nominatim
from geopy import distance
import sys
import time


# for backtracking...
from Problem2 import Tries

# # for testing purposes .....................................................................................................................

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


# # .....................................................................................................................
#
# using brute force to get the city distance.
def bruteforce(locationList):
    app = list(permutations(range(1, 8)));
    shortestDistance = sys.maxsize;
    index = 0;

    print("\nSolving TSP using permutation and bruteforce...\nplease wait...")
    start_time = time.time()


    listOfDistances = []
    for i in range(len(app)):
        currentDistance  = (distance.distance(locationList[0].coordinate, locationList[app[i][0]].coordinate).km)
        for j in range(len(app[i])-1):
            currentDistance = currentDistance + (distance.distance(locationList[app[i][j]].coordinate, locationList[app[i][j+1]].coordinate).km)

        currentDistance = currentDistance + (distance.distance(locationList[app[i][j+1]].coordinate,locationList[0].coordinate).km)
        listOfDistances.append(currentDistance)
        if(currentDistance<shortestDistance):
            shortestDistance = currentDistance;
            index = i;

    print("\nComputation Complete.")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("\nShortest Distance is "+str(shortestDistance))
    print("Route to take:\n")
    print(str(locationList[0].name))
    print("  V   ")
    for city in app[index]:
        print(str(locationList[city].name))
        print("  V   ")
    print(str(locationList[0].name))

bruteforce(locationList)


def createBacktrackingDictionary():

    app = list(permutations(range(1,4))); #1,8
    tree = Tries.Tries()
    for i in app:
        word = "0"
        for j in range(len(i)):
            word = word + str(i[j])
        word += "0"
        tree.addWord(word)
        print(word)
    return tree.root