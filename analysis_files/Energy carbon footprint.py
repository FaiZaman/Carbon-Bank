import pandas
import os

myarray = pandas.read_csv("Carbon per energy.csv",usecols=[0,5,6]).values
country="United Kingdom"

i=0
while myarray[i][0]!=country:
    i=i+1;

print("Enter money spent on electricity")
energycost = input()
energyamount=energycost/myarray[i][2]
carbonfootprint=energyamount*myarray[i][1]
print("Carbon footprint is " + carbonfootprint + "kg of CO2")
