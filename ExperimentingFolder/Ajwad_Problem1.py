# import geopy
from geopy.geocoders import Nominatim;
# import gmplot
from gmplot import gmplot

# creating a class for location information
class locationInfo:
    def __init__(self,name):
        self.name = name;

    def setLongitude(self,longitude):
        self.longitude = longitude;

    def setLatitude(self,latitude):
        self.latitude = latitude;

    def setAddress(self,address):
        self.address = address;

    def print_location_information(self):
        print(str(self.name)+" - ("+str(self.latitude)+", "+str(self.longitude)+")");


# creating an array to insert information class.
locationList = [locationInfo("Kuala Lumpur"),
                locationInfo("Jakarta"),
                locationInfo("Bangkok"),
                locationInfo("Taipei"),
                locationInfo("Hong Kong"),
                locationInfo("Tokyo"),
                locationInfo("Beijing"),
                locationInfo("Seoul")
                ];


# search for coordinate using geopy
geolocator = Nominatim(user_agent="MyGeopy");
for x in range(len(locationList)):
    location = geolocator.geocode(locationList[x].name);
    locationList[x].setAddress(location.address);
    locationList[x].setLongitude(location.longitude);
    locationList[x].setLatitude(location.latitude);
    locationList[x].print_location_information();

# marking location using gmplot
# 1. Placing map(centered at KL)
gmap = gmplot.GoogleMapPlotter(locationList[0].latitude, locationList[0].longitude, 13);

# 2. Placing all points(drop markers)
for x in range(len(locationList)):
    gmap.marker(locationList[x].latitude, locationList[x].longitude)

# 3.draw the map
gmap.draw("mapOflocation.html")

#Getting distance between cities









