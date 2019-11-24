import requests
r = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=54.7798,-1.5815,238&destinations=51.5309,-0.1233&key=AIzaSyCpnBpFs_Xg2vQKKGxN1kjCM9xDFROMvQo') 
r.status_code
print(r.text)
