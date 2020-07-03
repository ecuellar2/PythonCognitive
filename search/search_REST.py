#  https://docs.microsoft.com/en-us/azure/search/search-get-started-python

import json
import requests
from pprint import pprint

print("starting ")

endpoint = "https://xx.search.windows.net/"
api_version = '?api-version=2020-06-30'
headers = {'Content-Type': 'application/json',
        'api-key': "xxx" }

# list indexes 
url = endpoint + "indexes" + api_version + "&$select=name"
response  = requests.get(url, headers=headers)
index_list = response.json()
#pprint(index_list)

searchstring = "&search=hotels wifi&$count=true&$select=HotelId,HotelName"

url = endpoint + "indexes/hotels-sample-index/docs" + api_version + searchstring
response  = requests.get(url, headers=headers, json=searchstring)
query = response.json()
pprint(query)  



print("done")

