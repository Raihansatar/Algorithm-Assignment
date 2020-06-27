from itertools import permutations
from geopy import distance
import sys


# using brute force to get the city distance.
def bruteforce(locationList):
    app = list(permutations(range(1, 8)));
    shortestDistance = sys.maxsize;
    index = 0;

    print("\nSolving TSP using permutation and bruteforce\nplease wait...")

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
    print("\nShortest Distance is "+str(round(shortestDistance,3))+" km")
    print("Route to take:\n")
    finalstr = str(locationList[0].name)
    for city in app[index]:
        finalstr = finalstr + str(locationList[city].name) + '-->'
    finalstr = finalstr + str(locationList[0].name)
    print(finalstr)



