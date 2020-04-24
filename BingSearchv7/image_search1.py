# python -m pip install azure-cognitiveservices-search-imagesearch
#https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/tree/master/samples/search
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services

import os
from azure.cognitiveservices.search.imagesearch import ImageSearchClient
from msrest.authentication import CognitiveServicesCredentials

print("starting ")
subscription_key =  ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?"

search_term = "slipknot"

"""
Will search images on the web with the Bing Image Search API and print out first image result.
"""
client = ImageSearchClient(endpoint_string, CognitiveServicesCredentials(subscription_key))
image_results = client.images.search(query=search_term)

print("Searching the web for images of: {}".format(search_term))

if image_results.value:
    first_image_result = image_results.value[0]
    print("Total number of images returned: {}".format(len(image_results.value)))
    print("First image thumbnail url: {}".format(
    first_image_result.thumbnail_url))
    print("First image content url: {}".format(first_image_result.content_url))

print(" done  ")
