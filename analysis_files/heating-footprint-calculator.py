import pandas
import os

myarray = pandas.read_csv("Carbon footprint natural gas.csv",usecols=[0,2,4]).values
country="United Kingdom"

i=0
while myarray[i][0]!=country:
    i=i+1;

print("Enter money spent on natural gas")
naturalgascost = input()
energyamount=float(naturalgascost)/float(myarray[i][1])
carbonfootprint=energyamount*float(myarray[i][2])
print("Carbon footprint is " + str(carbonfootprint) + "kg of CO2")
