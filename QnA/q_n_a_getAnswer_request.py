# python -m pip install azure-cognitiveservices-knowledge-qnamaker
# https://www.qnamaker.ai/
# https://github.com/Azure-Samples/cognitive-services-qnamaker-python/blob/master/documentation-samples/quickstarts/get-answer/get-answer-3x.py

import http.client, urllib.parse, json, time, sys
print("starting ")

# Represents the various elements used to create HTTP request URI for QnA Maker operations.
# From Publish Page
# Example: YOUR-RESOURCE-NAME.azurewebsites.net
# CAUTION: This is not the exact value of HOST field
# HOST trimmed to work with http library
host = "xxx.azurewebsites.net"

# Authorization endpoint key From Publish Page
endpoint_key = ""

# Management APIs postpend the version to the route
# From Publish Page
# Example: /knowledgebases/ZZZ15f8c-d01b-4698-a2de-85b0dbf3358c/generateAnswer
# CAUTION: This is not the exact value after POST
# Part of HOST is prepended to route to work with http library
route = "/qnamaker/knowledgebases/xxxx/generateAnswer"
# JSON format for passing question to service
#question = "{'question': 'Is the QnA Maker Service free?','top': 2}"
question = "{'question': 'How do I manage my knowledgebase?','top': 2}"
print (question)
headers = {
    'Authorization': 'EndpointKey ' + endpoint_key,
    'Content-Type': 'application/json'
  }

try:
  conn = http.client.HTTPSConnection(host,port=443)

  conn.request ("POST", route,  question, headers)

  response = conn.getresponse ()

  answer = response.read ()

  print(json.dumps(json.loads(answer), indent=4))

except :
    print ("Unexpected error:", sys.exc_info()[0])
    print ("Unexpected error:", sys.exc_info()[1])


print("Done ")
