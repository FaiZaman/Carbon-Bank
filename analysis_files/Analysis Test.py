import requests

LitreFuelCost=1.189
fuel_costs=[]
fuel_amounts=[]
carbon_footprint_amount=[]

while True:
    print("Enter you fuel cost: \n")
    cost_input=input()
    fuel_costs.append(cost_input)
    fuel_amounts.append(fuel_costs[len(fuel_costs)-1])
    
    
