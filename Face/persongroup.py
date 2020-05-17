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

# Used for the Snapshot and Delete Person Group examples.
#TARGET_PERSON_GROUP_ID = str(uuid.uuid4()) # assign a random ID (or name it anything)

# Used in the Person Group Operations,  Snapshot Operations, and Delete Person Group examples.
# You can call list_person_groups to print a list of preexisting PersonGroups.
# SOURCE_PERSON_GROUP_ID should be all lowercase and alphanumeric. For example, 'mygroupname' (dashes are OK).
PERSON_GROUP_ID = 'my-unique-person-group'

print('Person group:', PERSON_GROUP_ID)
#just create group 1 time unless you delete it when done
face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)

# create3 person objects
woman = face_client.person_group_person.create(PERSON_GROUP_ID, "Woman")
print( 'First personID:', woman.person_id)  
man = face_client.person_group_person.create(PERSON_GROUP_ID, "Man")
print('Second personID:',man.person_id)
child = face_client.person_group_person.create(PERSON_GROUP_ID, "Child")
print('Third personID:',child.person_id) 

## Get images and put in 3 buckets, one bucket for each person
images_path = "C:/code/images/face"
os.chdir(images_path)
# Find all jpeg images of friends in working directory
first_images = [file for file in glob.glob('*.jpg') if file.startswith("woman")]
second_images = [file for file in glob.glob('*.jpg') if file.startswith("man")]
third_images = [file for file in glob.glob('*.jpg') if file.startswith("child")]

# associate image to the right person
for image in first_images:
    w = open(image, 'r+b')
    face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, woman.person_id, w)

for image in second_images:
    m = open(image, 'r+b')
    face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, man.person_id, m)

for image in third_images:
    ch = open(image, 'r+b')
    face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, child.person_id, ch)

#Once you've assigned faces, you must train the PersonGroup so that it can identify the visual features associated with each of its Person objects. 
print('Training the person group...')
# Train the person group
face_client.person_group.train(PERSON_GROUP_ID)
while (True):
    training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
    print("Training status: {}.".format(training_status.status))
    print()
    if (training_status.status is TrainingStatusType.succeeded):
        break
    elif (training_status.status is TrainingStatusType.failed):
        sys.exit('Training the person group has failed.')
    time.sleep(2)

# Now that we have created and trained a large person group, we can retrieve data from it.
# Returns a list[Person] of how many Persons were created/defined in the large person group.
person_list = face_client.person_group_person.list(person_group_id=PERSON_GROUP_ID, start='')

for person in person_list:
    for persisted_face_id in person.persisted_face_ids:
        print('The person {} has an image with ID: {}'.format(person.name, persisted_face_id))


# Use group image for testing
group_photo = 'test-image-person-group.jpg'
test_image_array = glob.glob(group_photo)
image = open(test_image_array[0], 'r+b')  # r+b mode is open the binary file in read or write mode

# Detect human faces in image 
face_ids = []
faces = face_client.face.detect_with_stream(image)
for face in faces:
    face_ids.append(face.face_id)
    print('detected human face ')
    print(face.face_id)

print('identify faces ')
results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
for person in results:
    # Get topmost confidence score
    print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0].confidence)) # Get topmost confidence score
    
# Delete the main person group.
face_client.person_group.delete(person_group_id=PERSON_GROUP_ID)
print("Deleted the person group {} from the source location.".format(PERSON_GROUP_ID))


'''
LARGE_PERSON_GROUP_ID = 'my-unique-large-person-group'
print('Large person group:', LARGE_PERSON_GROUP_ID)
face_client.large_person_group.create(large_person_group_id=LARGE_PERSON_GROUP_ID, name=LARGE_PERSON_GROUP_ID)

# Define woman friend , by creating a large person group person
woman = face_client.large_person_group_person.create(LARGE_PERSON_GROUP_ID, "Woman")
# Define man friend
man = face_client.large_person_group_person.create(LARGE_PERSON_GROUP_ID, "Man")
# Define child friend
child = face_client.large_person_group_person.create(LARGE_PERSON_GROUP_ID, "Child")

images_path = "C:/code/images/face"
os.chdir(images_path)
# Find all jpeg images of friends in working directory
woman_images = [file for file in glob.glob('*.jpg') if file.startswith("woman")]
man_images = [file for file in glob.glob('*.jpg') if file.startswith("man")]
child_images = [file for file in glob.glob('*.jpg') if file.startswith("child")]

# Add to a woman person
for image in woman_images:
    w = open(image, 'r+b')
    face_client.large_person_group_person.add_face_from_stream(LARGE_PERSON_GROUP_ID, woman.person_id, w)

# Add to a man person
for image in man_images:
    m = open(image, 'r+b')
    face_client.large_person_group_person.add_face_from_stream(LARGE_PERSON_GROUP_ID, man.person_id, m)

# Add to a child person
for image in child_images:
    ch = open(image, 'r+b')
    face_client.large_person_group_person.add_face_from_stream(LARGE_PERSON_GROUP_ID, child.person_id, ch)


print('Training the large person group...')
# Train the person group
face_client.large_person_group.train(LARGE_PERSON_GROUP_ID)
# Check training status
while (True):
    training_status = face_client.large_person_group.get_training_status(LARGE_PERSON_GROUP_ID)
    print("Training status: {}.".format(training_status.status))
    print()
    if (training_status.status is TrainingStatusType.succeeded):
        break
    elif (training_status.status is TrainingStatusType.failed):
        sys.exit('Training the large person group has failed.')
    time.sleep(2)

# Now that we have created and trained a large person group, we can retrieve data from it.
# Returns a list[Person] of how many Persons were created/defined in the large person group.
person_list_large = face_client.large_person_group_person.list(large_person_group_id=LARGE_PERSON_GROUP_ID, start='')

print('Persisted Face IDs from {} large person group persons:'.format(len(person_list_large)))
print()
for person_large in person_list_large:
    for persisted_face_id in person_large.persisted_face_ids:
        print('The person {} has an image with ID: {}'.format(person_large.name, persisted_face_id))

face_client.large_person_group.delete(large_person_group_id=LARGE_PERSON_GROUP_ID)
'''
print("Done ")
