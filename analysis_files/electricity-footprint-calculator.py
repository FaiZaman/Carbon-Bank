import pandas
import os

myarray = pandas.read_csv("Carbon per energy.csv",usecols=[0,5,7]).values
country="United Kingdom"

i=0
while myarray[i][0]!=country:
    i=i+1;

print("Enter money spent on electricity")
energycost = input()
energyamount=float(energycost)/float(myarray[i][2])
carbonfootprint=energyamount*float(myarray[i][1])
print("Carbon footprint is " + str(carbonfootprint) + "kg of CO2")
