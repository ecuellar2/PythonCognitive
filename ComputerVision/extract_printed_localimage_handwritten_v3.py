#python -m pip install -U matplotlib
#python -m pip install -U Pillow
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services/Computer-vision/QuickStarts
# can save as .ipynb 

import json
import os
import sys
import requests
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO

print("starting ")

key = ""
endpoint = "https://southcentralus.api.cognitive.microsoft.com/vision/v3.0-preview/read/analyze?"
image_path = "C:/code/images/cursive_writing_on_notebook_paper.jpg"
image_data = open(image_path, "rb").read()

# Set the langauge that you want to recognize. The value can be "en" for English, and "es" for Spanish
language = "en"
headers = {'Ocp-Apim-Subscription-Key': key,
           'Content-Type': 'application/octet-stream'}


#data = {'url': image_url}
response = requests.post(endpoint, headers=headers, data=image_data, params={'language': language})
response.raise_for_status()

# Extracting text requires two API calls: One call above to submit the image for processing, the other below to retrieve text found in image.
# Holds the URI used to retrieve the recognized text.
operation_url = response.headers["Operation-Location"]

# The recognized text isn't immediately available, so poll to wait for completion.
analysis = {}
poll = True
while (poll):
    response_final = requests.get(response.headers["Operation-Location"], headers=headers)
    analysis = response_final.json()
    #print(json.dumps(analysis, indent=4))
    time.sleep(1)
    if ("analyzeResult" in analysis):
        poll = False
    if ("status" in analysis and analysis['status'] == 'failed'):
        poll = False

polygons = []
if ("analyzeResult" in analysis):
    # Extract the recognized text, with bounding boxes.
    polygons = [(line["boundingBox"], line["text"])
                for line in analysis["analyzeResult"]["readResults"][0]["lines"]]

# Display the image and overlay it with the extracted text.
image = Image.open(BytesIO(image_data ))

ax = plt.imshow(image)
for polygon in polygons:
    vertices = [(polygon[0][i], polygon[0][i+1])
                for i in range(0, len(polygon[0]), 2)]
    text = polygon[1]
    patch = Polygon(vertices, closed=True, fill=False, linewidth=2, color='y')
    ax.axes.add_patch(patch)
    plt.text(vertices[0][0], vertices[0][1], text, fontsize=20, va="top")
plt.show()

#plt.show()
print("done")

