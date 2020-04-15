#https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/cognitive-services/bing-visual-search/includes/quickstarts/visual-search-client-library-python.md
#python -m pip install azure-cognitiveservices-search-visualsearch

import http.client, urllib.parse
import json
import os.path
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
subscription_key =  ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?"
PATH = 'C:\\code\\images\\'
image_path = os.path.join(PATH, "dog.jpg")
client = VisualSearchClient(endpoint=endpoint_string, credentials=CognitiveServicesCredentials(subscription_key))

with open(image_path, "rb") as image_fd:
    # You need to pass the serialized form of the model
    knowledge_request = json.dumps(VisualSearchRequest().serialize())
    print("\r\nSearch visual search request with binary of dog image")
    result = client.images.visual_search(image=image_fd, knowledge_request=knowledge_request)

if not result:
        print("No visual search result data.")
        # Visual Search results
if result.image.image_insights_token:
    print("Uploaded image insights token: {}".format(result.image.image_insights_token))
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
    

