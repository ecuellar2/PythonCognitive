# python -m pip install azure-cognitiveservices-knowledge-qnamaker
# https://www.qnamaker.ai/
# https://github.com/Azure-Samples/cognitive-services-qnamaker-python/blob/master/documentation-samples/quickstarts/publish-knowledge-base/publish-kb-3x.py

import http.client, urllib.parse, json, time, sys
print("starting ")

try:
    # Represents the various elements used to create HTTP request path for QnA Maker operations.
    knowledge_base_id = ""
    resource_key = ""    #  key of qna Cognitive Services

    host = "westus.api.cognitive.microsoft.com"
    route = "/qnamaker/v4.0/knowledgebases/" + knowledge_base_id
    headers = {
    'Ocp-Apim-Subscription-Key': resource_key
    }
    conn = http.client.HTTPSConnection(host,port=443)
    conn.request ("POST", route, "", headers)
    response = conn.getresponse ()
    print(response.status)
except :
    print ("Unexpected error:", sys.exc_info()[0])
    print ("Unexpected error:", sys.exc_info()[1])


print("Done ")
