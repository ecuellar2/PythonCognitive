# -*- coding: utf-8 -*-
#C:\Python\Python38-32\python.exe -m pip install requests uuid

import os, requests, uuid, json
key = ""
endpoint = "https://api.cognitive.microsofttranslator.com/languages?api-version=3.0"



print("Starting")

headers = {
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

request = requests.get(endpoint, headers=headers)
response = request.json()

print(json.dumps(response, sort_keys=True, indent=4,
                 ensure_ascii=False, separators=(',', ': ')))

print("All done")
