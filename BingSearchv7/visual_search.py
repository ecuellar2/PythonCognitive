#https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/cognitive-services/bing-visual-search/includes/quickstarts/visual-search-client-library-python.md
#python -m pip install azure-cognitiveservices-search-visualsearch
#https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/blob/master/samples/search/visual_search_samples.py


import http.client, urllib.parse
import json
import os.path
import requests
from azure.cognitiveservices.search.visualsearch import VisualSearchClient
from azure.cognitiveservices.search.visualsearch.models import (
    VisualSearchRequest,
    CropArea,
    ImageInfo,
    Filters,
    KnowledgeRequest,
)
from msrest.authentication import CognitiveServicesCredentials

print("starting ")
def print_json(obj):
    """Print the object as json"""
    print(json.dumps(obj, sort_keys=True, indent=2, separators=(',', ': ')))


subscription_key =  ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?"

PATH = 'C:\\code\\images\\'
image_path = os.path.join(PATH, "cat.jpg")
client = VisualSearchClient(endpoint=endpoint_string, credentials=CognitiveServicesCredentials(subscription_key))
# rb Opens a file in binary format. 
with open(image_path, "rb") as image_fd:
    # You need to pass the serialized form of the model
    # convert into  JSON string by using the json.dumps() method.
    knowledge_request = json.dumps(VisualSearchRequest().serialize())
    print("\r\n ***    Visual search request with binary image   *********  ")
    result = client.images.visual_search(image=image_fd, knowledge_request=knowledge_request)

if not result:
        print("No visual search result data.")
        # Visual Search results
if result.image.image_insights_token:
    print("Uploaded image insights token: {}".format(result.image.image_insights_token))
    insightsToken = result.image.image_insights_token
    formData = '{"imageInfo":{"imageInsightsToken":"' + insightsToken + '"}}'
    file = {'knowledgeRequest': (None, formData)}
    headers = {
    'Ocp-Apim-Subscription-Key': subscription_key
     }
    base_uri ="https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/images/visualsearch?mkt=en-US&safeSearch=Strict&setLang=en"
    response = requests.post(base_uri, headers=headers, files=file)
    response.raise_for_status()
    print_json(response.json())


else:
    print("Couldn't find image insights token!")
# List of tags
if result.tags:
    first_tag = result.tags[0]
    print("Visual search tag count: {}".format(len(result.tags)))
# List of actions in first tag
    if first_tag.actions:
        first_tag_action = first_tag.actions[0]
        print("First tag action count: {}".format(len(first_tag.actions)))
        print("First tag action type: {}".format(first_tag_action.action_type))
    else:
        print("Couldn't find tag actions!")
else:
    print("Couldn't find image tags!")
    
'''
:type set_lang: str :param knowledge_request: The form data is a JSON object that
 identifies the image using an insights token or URL to the image. The  
 object may also include an optional crop area that identifies an area  
 of interest in the image. The insights token and URL are mutually  
 exclusive – do not specify both. You may specify knowledgeRequest form  
 data and image form data in the same request only if knowledgeRequest  
 form data specifies the cropArea field only (it must not include an  
 insights token or URL).  

:type knowledge_request: str :param image: The form data is an image binary. The
 Content-Disposition header's name parameter must be set to "image".  
 You must specify an image binary if you do not use knowledgeRequest  
 form data to specify the image; you may not use both forms to specify  
 an image. You may specify knowledgeRequest form data and image form  
 data in the same request only if knowledgeRequest form data specifies  
 the cropArea field only  (it must not include an insights token or  
 URL).  
'''
