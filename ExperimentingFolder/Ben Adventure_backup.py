from geopy.geocoders import Nominatim
from gmplot import gmplot
from geopy import distance
import itertools
import Cities


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

locationList = [locationInfo("Kuala Lumpur","textfile/KualaLumpur.txt"),
                locationInfo("Jakarta","textfile/Jakarta.txt"),
                locationInfo("Bangkok","textfile/Bangkok.txt"),
                locationInfo("Taipei","textfile/Taipei.txt"),
                locationInfo("Hong Kong","textfile/HongKong.txt"),
                locationInfo("Tokyo","textfile/Japan.txt"),
                locationInfo("Beijing","textfile/Beijing.txt"),
                locationInfo("Seoul","textfile/Seoul.txt")
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
        distanceCountry[i][j] = distance.distance(locationList[i].coordinate, locationList[j].coordinate).km
        print("%12.3f km|" % distance.distance(locationList[i].coordinate, locationList[j].coordinate).km, end='')
    print('')

# function of travel salesman person using Held-Karp algorithm
def TSP(location):
    n = len(location)

    # initial value of 0 to all other points
    A = {}
    for i, cost in enumerate(location[0][1:]):  # w[0][1:] = take length start from [0][1 afterward]
        A.update({
            (frozenset([0, i + 1]), i + 1): (cost, [0, i + 1])
        })

    for m in range(2, n):  # n, is the length of matrix
        B = {}

        # At this stage the recursion is used, in addition the 'combinations' module is used, which allows grouping
        # and comparing data.
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, n), m)]:
            for j in S - {0}:  # create set with all the place
                # The least expensive route for the trip is sought, that is, the minimum values ​​are sought.
                B[(S, j)] = min(
                    (A[(S - {j}, k)][0] + location[k][j], A[(S - {j}, k)][1] + [j]) for k in S if k != 0 and k != j)

        A = B  # store B in as as B in the loop only
    # Start path and end path are now added

    res = min((A[d][0] + location[0][d[1]], A[d][1]) for d in iter(A))  # get the minimum from the last set
    # store res in array
    # Once the minimum value is found, the optimal solution is available.

    result = res[0], [(i) for i in res[1]]
    result[1].append(0)

    return result
# End of travel salesman person function

short = TSP(distanceCountry)[1] # get the shortest path
costTPS = TSP(distanceCountry)[0] # get the shortest path cost

print("\nThe shortest path is:")
for i in range(len(short) - 1):
    print(locationList[short[i]].name + " --> ", end="")
print(locationList[short[len(short) - 1]].name)

print("\nwith the total distance: %.3f km" % costTPS)





# 4. Plot Line

# for i in range(len(locationList)):
#     latList = []
#     longList = []
#     for j in range(len(locationList)):
#         latList.append(locationList[i].latitude)
#         longList.append(locationList[i].longitude)
#         latList.append(locationList[j].latitude)
#         longList.append(locationList[j].longitude)
#         gmap.plot(latList, longList, 'cornflowerblue', edge_width=2)

# plot the shortest route line
latShort = []
longShort = []
for j in range(len(short)):
    latShort.append(locationList[short[j]].latitude)
    longShort.append(locationList[short[j]].longitude)
    gmap.plot(latShort, longShort, 'red', edge_width=2)




# 5.draw the map

gmap.draw("Ben_Shortest_Adventure.html")




# =============================================================== PROBLEM 2 =========================================================== #

stopword_DefaultEnglish="textfile/stopwords_DefaultEnglish.txt"
stopword_GoogleHistory="textfile/stopwords_GoogleHistory.txt"
stopword_MySQL="textfile/stopwords_MySQL.txt"
negativeList = "textfile/Negative_Words.txt"
positiveList = "textfile/Positive_Words.txt"

cityNamelist=[]
positiveValuelist=[]
negativeValuelist=[]
neutralValuelist=[]

ListOfCities= []
for i in range(len(locationList)):
    ListOfCities.append(Cities.Cities(locationList[i].article,locationList[i].name))

for city in ListOfCities:
    print("\n\n+ ===== "+str(city.name)+" ===== +")
    city.processCitiesText()
    print("removing stopword from Default English...")
    city.removeStopWords_TRIES(stopword_DefaultEnglish)
    print("removing stopword Google History...")
    city.removeStopWords_TRIES(stopword_GoogleHistory)
    print("removing stopword MySQL...")
    city.removeStopWords_TRIES(stopword_MySQL)
    print("Removing stopwords COMPLETED")

    print("Getting frequencies and generating graph...")
    city.getFrequency()
    GraphName = str(city.name) + "_Word_Frequencies.html"
    city.generateGraphCities(GraphName,city.elementList,city.elementFrequency)

    print("Getting the frequency of positvie, negative and neutral words...")
    city.getPositive_Negative_Neutral_Frequency(positiveList,negativeList)

    print("Generating PNN Graph...")
    GraphName2 = str(city.name) + "_PPN_Frequencies.html"
    city.generateGraphPNN(GraphName2,city.alignmentList,city.alignmentFrequency)

    cityNamelist.append(city.name) #create list of cities name
    positiveValuelist.append(city.alignmentFrequency[0]) #create list of positive freq
    negativeValuelist.append(city.alignmentFrequency[1]) #create list of negative freq
    neutralValuelist.append(city.alignmentFrequency[2]) #create list of neutral freq


ListOfCities[0].generateOverallPNN_Graph(cityNamelist,positiveValuelist,negativeValuelist,neutralValuelist);
SV = ListOfCities[0].calculateSentinelValue(positiveValuelist,negativeValuelist,neutralValuelist)
SV_Path = ListOfCities[0].sentimentValuePath(SV)

# printing SV table AND saving it location list
print("\n\nCities and their SV")
for i in range(len(SV)):
    locationList[i].setSV(SV[i])
    print(str(locationList[i].name)+" = "+str(locationList[i].sv))
print("\n")

# priniting sentiment path
print("\nThe sentinent path is:")
for i in range(len(SV_Path) - 1):
    print(locationList[SV_Path[i]].name + " --> ", end="")
print(locationList[0].name)
print(SV_Path)

# drawing the Sentinal Value Path on html
SV_latList = []
SV_longList = []
for i in SV_Path:
    SV_latList.append(locationList[i].latitude)
    SV_longList.append(locationList[i].longitude)

SV_gmap = gmplot.GoogleMapPlotter(locationList[0].latitude, locationList[0].longitude, 13)
for x in range(len(locationList)):
    SV_gmap.marker(locationList[x].latitude, locationList[x].longitude)
SV_gmap.plot(SV_latList,SV_longList,'cornflowerblue', edge_width=2)
SV_gmap.draw("Sentinent_Value_Path.html")



# ================================================= PROBLEM 3 ======================================================== #

print("\n\n---------------------------------------------------\n\n")
print(short)

# create new city list using the shortest distance
# for ease of understanding and coding
list_of_cities = []
for city in range(len(short)-1):
    list_of_cities.append(locationList[short[city]])
    print("Name=>"+str(list_of_cities[city].name)+" SV value=>"+str(list_of_cities[city].sv))
print("")

# create an array to store the newly optimized route
optimised_list = [0]
# create an array to store the cities that pass the first condition
lessThen40 = []


#starting off the process
currentCity = 0 #set current city as KL(index 0)
# create an array to store info of which cities has been visited (1 for visited)
visited = [1,0,0,0,0,0,0,0]

i = 1
while len(optimised_list)<8:
    print("\n======================================================================================")
    lessThen40 = []
    currentCity = optimised_list[-1] #get last element

    print("Current city is: " + list_of_cities[currentCity].name)
    targetCity = i
    next_to_visit_found=False
    while(next_to_visit_found==False):
        print(i)
        if(visited[targetCity]==1 or targetCity == currentCity): #next target city cannot be self or visited city
            if (targetCity == 7):  # if end of the array, loop back to 1
                i = 1
                targetCity = i
            else:
                i = i+1
                targetCity = i
        else:
            targetCity = i
            next_to_visit_found = True


    print("Target city is: "+list_of_cities[targetCity].name)

    # find all the distance less then 40 from current city to target city
    condition1a = distance.distance(list_of_cities[currentCity].coordinate, list_of_cities[targetCity].coordinate).km
    for j in range(1,8):
        if(visited[j] == 1):
            print("already visited:"+str(list_of_cities[j].name))
        else:
            condition1b = distance.distance(list_of_cities[currentCity].coordinate, list_of_cities[j].coordinate).km
            ans = (condition1b/condition1a)*100-100
            print("Difference of % distance from ["+ str(list_of_cities[currentCity].name) +", "+str(list_of_cities[j].name)+"] is "+str(ans))
            if(ans<40.00 and ans!=0.0):
                # print("-----------")
                # print(str(list_of_cities[j].name)+" - is less then 140% distance")
                # print("-----------")
                lessThen40.append(j)

    #check if there city with >2% of sentiment value
    print("\n++++++++++++++++++++++++++")

    biggestSV=0
    biggestSV_index = targetCity
    for k in range(len(lessThen40)):
        sentimentDiff = list_of_cities[lessThen40[k]].sv - list_of_cities[targetCity].sv
        print("Difference of sentiment from ["+str(list_of_cities[lessThen40[k]].name)+", "+str(list_of_cities[targetCity].name)+"] is "+str(sentimentDiff))
        if(abs(sentimentDiff)>2 and sentimentDiff>0): # 2nd cond is to make sure that the sentiment value is better
            if(biggestSV<sentimentDiff): # if the there are better city
                biggestSV=sentimentDiff
                biggestSV_index = lessThen40[k]
                print("BiggestSV: "+str(biggestSV)+" at "+str(list_of_cities[lessThen40[k]].name)+"("+str(biggestSV_index)+")")

    if(biggestSV == 0):
        print("Original target city is added")
    else:
        print("Better city is located")
    print(str(list_of_cities[biggestSV_index].name))
    targetCity = biggestSV_index
    optimised_list.append(targetCity)
    visited[targetCity] = 1

    i = targetCity

    # if (targetCity == 7):  # if end of the array, loop back to 1
    #     i = 1
    # else:
    #     i = i + 1

    print(lessThen40)
    print(optimised_list)
    print(visited)
    print(i)
    print()





