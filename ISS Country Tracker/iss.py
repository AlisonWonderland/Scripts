#! /usr/bin/env python

import requests

#Add abreviation to full name script

response = requests.get("http://api.open-notify.org/iss-now.json")

info_dict = response.json()
latitude = info_dict["iss_position"]["latitude"]
longitude = info_dict["iss_position"]["longitude"]

payload = {'key': 'Insert your key here', 'location': latitude + ',' + longitude}
response2 = requests.get("http://www.mapquestapi.com/geocoding/v1/reverse?includeRoadMetadata=true&includeNearestIntersection=true", params=payload)
response2_json = response2.json()

country = response2_json['results'][0]['locations'][0]['adminArea5']
if(country == ''):
    print('Most likely over the ocean')
else:
    print(country)
