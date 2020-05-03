#python -m pip install azure-cognitiveservices-search-videosearch
#https://docs.microsoft.com/en-us/azure/cognitive-services/bing-spell-check/quickstarts/python
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services

import requests
import json

print("starting ")

key = ""
endpoint = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/SpellCheck?"
 # the text to be spell-checked
example_text = "Hollo, wrld"
data = {'text': example_text}
#Mode is either proof (catches most spelling/grammar errors) or spell (catches most spelling but not as many grammar errors).
params = {
    'mkt':'en-us',
    'mode':'proof'
    }

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Ocp-Apim-Subscription-Key': key,
    }

response = requests.post(endpoint, headers=headers, params=params, data=data)
json_response = response.json()
print(json.dumps(json_response, indent=4))

print("done")

