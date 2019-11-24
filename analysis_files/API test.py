import requests
import pandas
import os
import json
import math

travel_method="Plane"
traveldict={"Plane":0.266, "Train": 0.046, "Diesel":0.177, "Petrol":0.185}

os.chdir('C:\\Users\\ofekv\\Documents\\Durhack\\Carbon-Bank\\analysis_files')
myarray = pandas.read_csv("airport-extended.csv",usecols=[1,6,7]).values
airportarray=["London Gatwick Airport","Glasgow City Heliport"]
locationarray=[[0,0],[0,0]]
for x in range (0,2):
    i=0
    while myarray[i][0]!=airportarray[x]:
        i=i+1;
    locationarray[x][0]=(myarray[i][1])
    locationarray[x][1]=(myarray[i][2])
##r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins='+locationarray[0][0]+','+locationarray[0][1]+'&destinations='+locationarray[1][0]+','+locationarray[1][1]+'&key=AIzaSyCpnBpFs_Xg2vQKKGxN1kjCM9xDFROMvQo')
r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins='+str(locationarray[0][0])+','+str(locationarray[0][1])+'&destinations='+str(locationarray[1][0])+','+str(locationarray[1][1])+'&key=AIzaSyCpnBpFs_Xg2vQKKGxN1kjCM9xDFROMvQo')

r.status_code
if r.text.find("distance")!=-1:
    distance = r.text[r.text.find("distance")+42:r.text.find("km")-1]
else:
    print("No API route")
    #https://en.wikipedia.org/wiki/Haversine_formula#
    locationarray[0][0]=locationarray[0][0]*math.pi/180
    locationarray[1][0]=locationarray[1][0]*math.pi/180
    locationarray[0][1]=locationarray[0][1]*math.pi/180
    locationarray[1][1]=locationarray[1][1]*math.pi/180
    distance = 2*6378*math.asin(math.sqrt(pow(math.sin((locationarray[1][0]-locationarray[0][0])/2),2) + math.cos(locationarray[1][0]) * math.cos(locationarray[0][0]) * pow(math.sin((locationarray[1][1]-locationarray[0][1])/2),2)))

print("Distance is: " +distance)
print("Carbon footprint for "+travel_method+" is "+ str(float(distance)*traveldict[travel_method]) + "kg of CO2")
