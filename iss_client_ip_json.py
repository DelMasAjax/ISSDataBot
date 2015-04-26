import urllib
import os
import json
from TwitterAPI import TwitterAPI
import time
import tokens
from geopy.geocoders import Nominatim

api = TwitterAPI(tokens.consumer_key, tokens.consumer_secret, tokens.access_token_key, tokens.access_token_secret)
lat_iss = 0
lon_iss = 0
speed_iss = 0
alt_iss = 0

lat_cli = 0
lon_cli = 0
counter = 0

geolocator = Nominatim()
print ("\nISS Tracking")
print ("Getting IP from client")
print ("******************")
response_client = json.loads(urllib.urlopen('https://freegeoip.net/json').read())
print("\nThe current ip is: " + response_client['ip'])

#response_iss = json.loads(urllib.urlopen('https://api.wheretheiss.at/v1/satellites/25544').read())

def iss_tracker():
	response_iss = json.loads(urllib.urlopen('https://api.wheretheiss.at/v1/satellites/25544').read())
	lat_iss = response_iss['latitude']
	lon_iss = response_iss['longitude']
	speed_iss = response_iss['velocity']
	alt_iss = response_iss['altitude']
	return(lat_iss,lon_iss,speed_iss,alt_iss)
def cli_tracker():	
	lat_cli = response_client['latitude']
	lon_cli = response_client['longitude']
	return(lat_cli,lon_cli)

#lat_iss,lon_iss = iss_tracker()
lat_cli,lon_cli = cli_tracker()
print ("\nPosition of the client via IP")
print (lat_cli)
print (lon_cli)

while True:
	lat_iss,lon_iss,speed_iss,alt_iss = iss_tracker()
	location = geolocator.reverse([lat_iss,lon_iss])
	print ("\nPosition of the ISS")
	print (lat_iss)
	print (lon_iss)
	###raw_loc = location.raw
	#print(raw_loc)
	string_speed = str(speed_iss)
	string_alt = str(alt_iss)
	speed_short = string_speed[0:7]
	alt_short = string_alt[0:7]
	print (speed_short)
	print (alt_short)
	'''Now, with complete address of the ISS'''
	print("\nPosition in Earth")
	print(location.address)	
	time.sleep(5)
	counter = counter + 1
	print counter
	#if counter == 24:
	if(location.address != None):
		r = api.request('statuses/update', {'status':'Hi there! Now in: '+location.address+', speed: '+speed_short+', altitude: '+alt_short})
		print r.status_code
		counter = 0


