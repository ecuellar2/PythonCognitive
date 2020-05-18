#python -m pip install --upgrade azure-cognitiveservices-vision-face
#https://docs.microsoft.com/en-us/azure/cognitive-services/face/quickstarts/client-libraries?pivots=programming-language-python&tabs=windows
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
target_image_file_names = ['man1-person-group.jpg', 'man2-person-group.jpg']
source_image_file_name1 = 'man3-person-group.jpg'
source_image_file_name2 = 'child1-person-group.jpg'

#detected_faces1 = face_client.face.detect_with_url(IMAGE_BASE_URL + source_image_file_name1)
image_array1 = glob.glob(source_image_file_name1)
image1 = open(image_array1[0], 'r+b')  # r+b mode is open the binary file in read or write mode
# Detect human faces in image 
detected_faces1 = face_client.face.detect_with_stream(image1) # man3-person-group.jpg
source_image1_id = detected_faces1[0].face_id
print('{} face(s) detected from image {}.'.format(len(detected_faces1), source_image_file_name1))
print (source_image1_id)

image_array2 = glob.glob(source_image_file_name2)
image2 = open(image_array2[0], 'r+b')  
# Detect face(s) from source image 2, returns a list[DetectedFaces]
detected_faces2 =  face_client.face.detect_with_stream(image2) # child1-person-group.jpg
# Add the returned face's face ID
source_image2_id = detected_faces2[0].face_id
print('{} face(s) detected from image {}.'.format(len(detected_faces2), source_image_file_name2))
print (source_image2_id)

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


# Verification example for faces of the same person. The higher the confidence, the more identical the faces in the images are.
# Since target faces are the same person, in this example, we can use the 1st ID in the detected_faces_ids list to compare.
# source_image1_id is man3-person-group.jpg
print ('')
verify_result_same = face_client.face.verify_face_to_face(source_image1_id, detected_faces_ids[0])
if (verify_result_same.is_identical):
    print('Faces from {} & {} are of the same person, with confidence: {}'.format(source_image_file_name1, target_image_file_names[0], verify_result_same.confidence))
else:
    print('Faces from {} & {} are of a different person, with confidence: {}'.format(source_image_file_name1, target_image_file_names[0], verify_result_same.confidence))

print ('calling verify_face_to_face again *****')
# source_image2_id is child1-person-group.jpg
verify_result_diff = face_client.face.verify_face_to_face(source_image2_id, detected_faces_ids[0])
if (verify_result_diff.is_identical):
    print('Faces from {} & {} are of the same person, with confidence: {}'.format(source_image_file_name2, target_image_file_names[0], verify_result_diff.confidence))
else:
    print( 'Faces from {} & {} are of a different person, with confidence: {}'.format(source_image_file_name2, target_image_file_names[0], verify_result_diff.confidence))
# By default, isIdentical is set to True if similarity confidence is greater than or equal to 0.5. 

print("Done ")
