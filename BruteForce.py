from itertools import permutations
from geopy import distance
import sys
import time

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


