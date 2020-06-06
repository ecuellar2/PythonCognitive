# python -m pip install azure-cognitiveservices-vision-customvision
# https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/quickstarts/image-classification?pivots=programming-language-python
# https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/blob/master/samples/vision/custom_vision_training_samples.py
# https://www.customvision.ai

import requests
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

from PIL import Image
from io import BytesIO
import os
import time
print("starting ")
publish_iteration_name = "classifyModel"

#Custom Vision Service has 2 types of endpoints. One for training the model and one for running predictions against the model.
key = ""
endpoint_string = "https://xxx.cognitiveservices.azure.com/"

key_predictor = ""
endpoint_predictor = "https://xxx-prediction.cognitiveservices.azure.com/"

credentials = ApiKeyCredentials(in_headers={"Training-key": key})
trainer = CustomVisionTrainingClient(endpoint_string, credentials)

credentials2 = ApiKeyCredentials(in_headers={"Prediction-key": key_predictor})
predictor = CustomVisionPredictionClient(endpoint_predictor, credentials2)

#project = trainer.create_project("My New Project")
project_id = ""
'''
hemlock_tag = trainer.create_tag(project_id, "Hemlock")
print (hemlock_tag.id)
cherry_tag = trainer.create_tag(project_id, "Japanese Cherry")
print (cherry_tag.id)
'''
hemlock_id = ""
cherry_id  = ""
hemlock_dir = "C:/code/"
for image in os.listdir(hemlock_dir):
    with open(os.path.join(hemlock_dir, image), mode="rb") as img_data:
        print ("first looping")
        #trainer.create_images_from_data(project_id, img_data.read(), [hemlock_id])

cherry_dir = "C:/code/"
for image in os.listdir(cherry_dir):
    with open(os.path.join(cherry_dir, image), mode="rb") as img_data:
        print ("second looping")
        #trainer.create_images_from_data(project_id, img_data.read(), [cherry_id])
        #example below if I had multiple tags 
        #trainer.create_images_from_data(project.id, img_data.read(), [cherry_id, id2])

'''
print("Training shows up as iteration")
iteration = trainer.train_project(project_id)
while (iteration.status == "Training"):
    iteration = trainer.get_iteration(project_id, iteration.id)
    print("Training status: " + iteration.status)
    print (iteration.id)
    time.sleep(2)
'''
iteration_id = ""
#goes to prediction endpoint resourceID
resource_id = "/subscriptions/xx/resourceGroups/cognitive2/providers/Microsoft.CognitiveServices/accounts/xxxx-Prediction"
#trainer.publish_iteration(project_id=project_id, iteration_id=iteration_id, publish_name=publish_iteration_name, prediction_id=resource_id)

cherry_img = "C:/code/japanese_cherry_9.jpg"
with open(cherry_img, mode="rb") as test_data:
    results = predictor.classify_image(project_id, publish_iteration_name, test_data.read())

for prediction in results.predictions:
    print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))

'''
Another approach is using object detection.
When you tag images in object detection projects, you need to specify the region of each tagged object using normalized coordinates.
The regions specify the bounding box in normalized coordinates, and the coordinates are given in the order: left, top, width, height.
fork_1: [ 0.145833328, 0.3509314, 0.5894608, 0.238562092 ]
predictor.detect_image()    use this instead of classify_image() when using region coordinates
'''

print("Done ")
# below for reference only for batching
#base_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-python-sdk-samples/master/samples/vision/"               
#Uploads each image with its corresponding tag. You can upload up to 64 images in a single batch.
'''
for image_num in range(1, 11):
    file_name = "hemlock_{}.jpg".format(image_num)
    full_name = base_image_url + "images/Hemlock/" + file_name
    image = Image.open(BytesIO(requests.get(full_name).content))
    with open(full_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[cherry_id]))
'''
#upload_result = trainer.create_images_from_files(project_id, images=image_list)

