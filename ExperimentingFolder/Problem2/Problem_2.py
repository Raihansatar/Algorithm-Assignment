import Cities
import time

# ======================#
#                       #
#   0 - Bangkok         #
#   1 - Beijing         #
#   2 - Hong Kong       #
#   3 - Jakarta         #
#   4 - Japan           #
#   5 - Kuala Lumpur    #
#   6 - Seoul           #
#   7 - Taipei          #
#                       #
# ======================#

ListOfCities= []
ListOfCities.append(Cities.Cities("../../textfile/KualaLumpur.txt", "Kuala Lumpur"))
ListOfCities.append(Cities.Cities("../../textfile/Bangkok.txt", "Bangkok"))
ListOfCities.append(Cities.Cities("../../textfile/Beijing.txt", "Beijing"))
ListOfCities.append(Cities.Cities("../../textfile/HongKong.txt", "Hong Kong"))
ListOfCities.append(Cities.Cities("../../textfile/Jakarta.txt", "Jakarta"))
ListOfCities.append(Cities.Cities("../../textfile/Japan.txt", "Japan"))
ListOfCities.append(Cities.Cities("../../textfile/Seoul.txt", "Seoul"))
ListOfCities.append(Cities.Cities("../../textfile/Taipei.txt", "Taipei"))

stopword1="../textfile/stopwords_DefaultEnglish.txt"
stopword2="../textfile/stopwords_GoogleHistory.txt"
stopword3="../textfile/stopwords_MySQL.txt"
negativeList = "../textfile/Negative_Words.txt"
positiveList = "../textfile/Positive_Words.txt"

Clist=[]
Plist=[]
Nlist=[]
nlist=[]

for city in ListOfCities:
    print("\n\n+ ===== "+str(city.name)+"===== +")
    city.processCitiesText()

    start_time = time.time()
    print("removing stopword 1...")
    city.removeStopWords_TRIES(stopword1)

    print("removing stopword 2...")
    city.removeStopWords_TRIES(stopword2)

    print("removing stopword 3...")
    city.removeStopWords_TRIES(stopword3)

    print("Removing stopwords COMPLETED")
    print("--- %s seconds ---" % (time.time() - start_time))

    print("Getting frequencies and generating graph...")
    city.getFrequency()
    GraphName = str(city.name) + "_Word_Frequencies.html"
    city.generateGraphCities(GraphName,city.elementList,city.elementFrequency)

    print("Getting the frequency of positvie, negative and neutral words...")
    city.getPositive_Negative_Neutral_Frequency(positiveList,negativeList)

    # print("Generating PNN Graph...")
    # GraphName2 = str(city.name) + "_PPN_Frequencies.html"
    # city.generateGraphPNN(GraphName2,city.alignmentList,city.alignmentFrequency)

    Clist.append(city.name) #create list of cities name
    Plist.append(city.alignmentFrequency[0]) #create list of positive freq
    Nlist.append(city.alignmentFrequency[1]) #create list of negative freq
    nlist.append(city.alignmentFrequency[2]) #create list of neutral freq

ListOfCities[0].generateOverallPNN_Graph(Clist,Plist,Nlist,nlist);
SV = ListOfCities[0].calculateSentinelValue(Plist,Nlist,nlist)
ListOfCities[0].sentimentValuePath(SV)
print(SV)