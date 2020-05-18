#python -m pip install --upgrade azure-cognitiveservices-vision-face
#https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/Face/FaceQuickstart.py

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

face_client = FaceClient(endpoint_string, CognitiveServicesCredentials(key))

images_path = "C:/code/images/face"
os.chdir(images_path)

# Create a list to hold the target photos of the same person
image_file_names = ['man1-person-group.jpg', 'man2-person-group.jpg', 'man3-person-group.jpg' ]

# Create an empty face list with an assigned ID.
face_list_id = "my-face-list"
print("Creating face list: {}...".format(face_list_id))
face_client.face_list.create(face_list_id=face_list_id, name=face_list_id)

for image_file_name in image_file_names:
    image_array = glob.glob(image_file_name)
    image = open(image_array[0], 'r+b')  
    face_client.face_list.add_face_from_stream(face_list_id=face_list_id, image=image,user_data=image_file_name )
    #face_client.face_list.add_face_from_url(face_list_id=face_list_id,url=IMAGE_BASE_URL + image_file_name, user_data=image_file_name)

the_face_list = face_client.face_list.get(face_list_id)
print('Persisted face ids of images in face list:')
print()
for persisted_face in the_face_list.persisted_faces:
    print(persisted_face.persisted_face_id)


print("Deleting face list: {}...".format(face_list_id))
face_client.face_list.delete(face_list_id=face_list_id)

'''
source_image_file_name1 = 'man3-person-group.jpg'
source_image_file_name2 = 'child1-person-group.jpg'

#detected_faces1 = face_client.face.detect_with_url(IMAGE_BASE_URL + source_image_file_name1)
image_array1 = glob.glob(source_image_file_name1)
image1 = open(image_array1[0], 'r+b')  # r+b mode is open the binary file in read or write mode
# Detect human faces in image 
detected_faces1 = face_client.face.detect_with_stream(image1) # man3-person-group.jpg
source_image1_id = detected_faces1[0].face_id

# List for the target face IDs (uuids)
detected_faces_ids = []
# Detect faces from target image url list, returns a list[DetectedFaces]
print ('started looping through file names *****************')
for image_file_name in target_image_file_names: #  ['man1-person-group.jpg', 'man2-person-group.jpg']
    image_array = glob.glob(image_file_name)
    image = open(image_array[0], 'r+b')  
    detected_faces =  face_client.face.detect_with_stream(image) 
    detected_faces_ids.append(detected_faces[0].face_id) # Add the returned face's face ID
    print (detected_faces[0].face_id)
    print('{} face(s) detected from image {}.'.format(len(detected_faces), image_file_name))

verify_result_same = face_client.face.verify_face_to_face(source_image1_id, detected_faces_ids[0])
if (verify_result_same.is_identical):
    print('Faces from {} & {} are of the same person, with confidence: {}'.format(source_image_file_name1, target_image_file_names[0], verify_result_same.confidence))
else:
    print('Faces from {} & {} are of a different person, with confidence: {}'.format(source_image_file_name1, target_image_file_names[0], verify_result_same.confidence))

'''
print("Done ")
