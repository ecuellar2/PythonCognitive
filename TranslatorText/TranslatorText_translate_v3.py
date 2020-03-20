# -*- coding: utf-8 -*-
#C:\Python\Python38-32\python.exe -m pip install requests uuid
# curl -X POST "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=es" -H "Ocp-Apim-Subscription-Key: xxx" -H "Ocp-Apim-Subscription-Region: southcentralus"  -H "Content-Type: application/json" -d "[{'Text':'Hello, what is your name?'}]"


import os, requests, uuid, json
key = ""
endpoint = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=es"

print("Starting")

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': 'southcentralus',
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

body = [{
    'text': ' Hello, what is your name? '
}]

request = requests.post(endpoint, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4,
                 ensure_ascii=False, separators=(',', ': ')))

print("All done")
