#python -m pip install --upgrade azure-cognitiveservices-vision-face
#https://docs.microsoft.com/en-us/azure/cognitive-services/face/quickstarts/client-libraries?pivots=programming-language-python&tabs=windows

import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

print("starting ")

key = ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/"

# Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    return ((left, top), (right, bottom))

face_client = FaceClient(endpoint_string, CognitiveServicesCredentials(key))
# Detect a face in an image that contains a single face
single_face_image_url = 'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'
single_image_name = os.path.basename(single_face_image_url)
detected_faces = face_client.face.detect_with_url(url=single_face_image_url)
# Display the detected face ID in the first single-face image.
# Face IDs are used for comparison to faces (their IDs) detected in other images.
print('Detected face ID from', single_image_name, ':')
for face in detected_faces: print (face.face_id)
print()

# Save this first ID for use in Find Similar
first_image_face_ID = detected_faces[0].face_id

# Detect the faces in an image that contains multiple faces
# Each detected face gets assigned a new ID
multi_face_image_url = "http://www.historyplace.com/kennedy/president-family-portrait-closeup.jpg"
multi_image_name = os.path.basename(multi_face_image_url)
detected_faces2 = face_client.face.detect_with_url(url=multi_face_image_url)

# Search through faces detected in group image for the single face from first image.
# First, create a list of the face IDs found in the second image.
second_image_face_IDs = list(map(lambda x: x.face_id, detected_faces2))
# Next, find similar face IDs like the one detected in the first image.
similar_faces = face_client.face.find_similar(face_id=first_image_face_ID, face_ids=second_image_face_IDs)
response = requests.get(multi_face_image_url)
img = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(img)

print('Similar faces found in', multi_image_name + ':')
# Loop through all the similar faces found in the group image
for face in similar_faces:
    # The face IDs of the single face image and the group image do not need to match, they are only used for identification purposes in each image.
    first_image_face_ID = face.face_id  #1st image in the similar faces found in group image
    # check all the faces in the group images and find the one that matches the face_id
    face_info = next(x for x in detected_faces2 if x.face_id == first_image_face_ID) 
    if face_info:
        print('    Face ID: ', first_image_face_ID)
        print('    Face rectangle:')
        print('    Left: ', str(face_info.face_rectangle.left))
        print('    Top: ', str(face_info.face_rectangle.top))
        print('    Width: ', str(face_info.face_rectangle.width))
        print('    Height: ', str(face_info.face_rectangle.height))
        draw.rectangle(getRectangle(face_info), outline='red')
        img.show()


#######################################################################
'''
#Detect face in image and then display and frame faces
single_face_image_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
single_image_name = os.path.basename(single_face_image_url)
detected_faces = face_client.face.detect_with_url(url=single_face_image_url)

# Download the image from the url
response = requests.get(single_face_image_url)
img = Image.open(BytesIO(response.content))

# For each face returned use the face rectangle and draw a red box.
print('Drawing rectangle around face... see popup for results.')
draw = ImageDraw.Draw(img)
for face in detected_faces:
    draw.rectangle(getRectangle(face), outline='red')

# Display the image in the users default image browser.
img.show()
'''


print("Done ")
