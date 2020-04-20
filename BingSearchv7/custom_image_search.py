# python -m pip install azure-cognitiveservices-search-customimagesearch
import os

from azure.cognitiveservices.search.customimagesearch import CustomImageSearchClient
from msrest.authentication import CognitiveServicesCredentials

print("starting ")
subscription_key =  ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/bingcustomsearch/v7.0/search?"
'''
Custom APIs are similar to the non-custom Bing Image Search and Bing Video Search APIs.
But general APIs search the entire web, and do not require the customConfig query parameter.
'''

search_string = "xbox"
client = CustomImageSearchClient(endpoint=endpoint_string,credentials=CognitiveServicesCredentials(subscription_key))
image_results = client.custom_instance.image_search( query=search_string, custom_config=1)
print("Searched for " + search_string )

if image_results.value:
    # find the first web page
    first_image_result = image_results.value[0]
    if first_image_result:
        print("Image result count: {}".format(len(image_results.value)))
        print("First image insights token: {}".format(
        first_image_result.image_insights_token))
        print("First image thumbnail url: {}".format(
        first_image_result.thumbnail_url))
        print("First image content url: {}".format(
        first_image_result.content_url))
