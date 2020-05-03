#python -m pip install -U matplotlib
#python -m pip install -U Pillow
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services/Computer-vision/QuickStarts

import os
import sys
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

print("starting ")

key = ""
endpoint = "https://southcentralus.api.cognitive.microsoft.com/vision/v2.1/analyze?"
image_path = "C:/code/images/cat.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(endpoint, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(analysis)
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
plt.show()
print("done")





