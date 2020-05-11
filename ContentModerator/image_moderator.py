#python -m pip install azure-cognitiveservices-vision-contentmoderator
#pip install --upgrade azure-cognitiveservices-vision-contentmoderator
#https://docs.microsoft.com/en-us/azure/cognitive-services/Content-Moderator/client-libraries?pivots=programming-language-python#use-a-custom-image-list
#https://github.com/Azure-Samples/cognitive-services-content-moderator-samples/blob/master/documentation-samples/python/content_moderator_quickstart.py

import os.path
from pprint import pprint
import time
from io import BytesIO
from random import random
import uuid

from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
from azure.cognitiveservices.vision.contentmoderator.models import (
    TermList,
    Terms,
    TermsData,
    RefreshIndex,
    Screen,
    Body
)
from msrest.authentication import CognitiveServicesCredentials

print("starting ")

key = ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/"
client = ContentModeratorClient(endpoint=endpoint_string,credentials=CognitiveServicesCredentials(key))
'''
IMAGE_LIST = [
    "https://moderatorsampleimages.blob.core.windows.net/samples/sample2.jpg",
    "https://moderatorsampleimages.blob.core.windows.net/samples/sample5.png"
]
#Check for adult/racy content
for image_url in IMAGE_LIST:
    print("\nEvaluate for adult and racy content.")
    evaluation = client.image_moderation.evaluate_url_input(content_type="application/json",cache_image=True,data_representation="URL",value=image_url)
    pprint(evaluation.as_dict())
'''
#Check for visible text
'''
for image_url in IMAGE_LIST:
    print("\nDetect and extract text.")
    evaluation = client.image_moderation.ocr_url_input(language="eng",content_type="application/json",data_representation="URL",value=image_url,cache_image=True,)
    pprint(evaluation.as_dict())
'''
#Check for faces
'''
for image_url in IMAGE_LIST:
    print("\nDetect faces.")
    evaluation = client.image_moderation.find_faces_url_input(content_type="application/json",cache_image=True,data_representation="URL",value=image_url)
    pprint(evaluation.as_dict())
'''
IMAGE_LIST = {
    "Sports": [
        "https://moderatorsampleimages.blob.core.windows.net/samples/sample4.png",
        "https://moderatorsampleimages.blob.core.windows.net/samples/sample6.png",
        "https://moderatorsampleimages.blob.core.windows.net/samples/sample9.png"
    ],
    "Swimsuit": [
        "https://moderatorsampleimages.blob.core.windows.net/samples/sample1.jpg",
        "https://moderatorsampleimages.blob.core.windows.net/samples/sample3.png",
        "https://moderatorsampleimages.blob.core.windows.net/samples/sample4.png",
        "https://moderatorsampleimages.blob.core.windows.net/samples/sample16.png"
    ]
}

IMAGES_TO_MATCH = [
    "https://moderatorsampleimages.blob.core.windows.net/samples/sample1.jpg",
    "https://moderatorsampleimages.blob.core.windows.net/samples/sample4.png",
    "https://moderatorsampleimages.blob.core.windows.net/samples/sample5.png",
    "https://moderatorsampleimages.blob.core.windows.net/samples/sample16.png"
]

def add_images(list_id, image_url, label):
    """Generic add_images from url and label."""
    print("\nAdding image {} to list {} with label {}.".format(image_url, list_id, label))
    added_image = client.list_management_image.add_image_url_input(list_id=list_id,content_type="application/json",data_representation="URL",value=image_url,label=label)
    pprint(added_image.as_dict())
    return added_image
'''
#Create an image list
print("Creating list MyList\n")
custom_list = client.list_management_image_lists.create(
    content_type="application/json",
    body={
        "name": "MyList",
        "description": "A sample list",
        "metadata": {
            "key_one": "Acceptable",
            "key_two": "Potentially racy"
        }
    }
)
print("List created:")
pprint(custom_list.as_dict())
list_id = custom_list.id

print("\nAdding images to list {}".format(list_id))
index = {}  # Keep an index url to id for later removal
for label, urls in IMAGE_LIST.items():
    for url in urls:
        image = add_images(list_id, url, label)
        if image:
            index[url] = image.content_id

'''
print("Done ")
