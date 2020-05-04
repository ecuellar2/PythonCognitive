#python -m pip install -U matplotlib
#python -m pip install -U Pillow
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services/Computer-vision/QuickStarts
# can save as .ipynb 

import os
import sys
import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO

print("starting ")
'''
Computer Vision's optical character recognition (OCR) API is similar to the Read API,
 but it executes synchronously and is not optimized for large documents. It uses an earlier recognition model but works with
  more languages.

If necessary, OCR corrects the rotation of the recognized text by returning the rotational offset in degrees about the horizontal 
image axis. OCR also provides the frame coordinates of each word.
'''
key = ""
endpoint = "https://southcentralus.api.cognitive.microsoft.com/vision/v2.1/ocr?"
image_path = "C:/code/images/atomist_quote_from_democritus.png"
image_data = open(image_path, "rb").read()

headers = {'Ocp-Apim-Subscription-Key': key, 'Content-Type': 'application/octet-stream'}
params = {'language': 'en', 'detectOrientation': 'true'}
response = requests.post(endpoint, headers=headers, params=params, data = image_data)
response.raise_for_status()

analysis = response.json()
# Extract the word bounding boxes and text.
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
word_infos

# Display the image and overlay it with the extracted text.
plt.figure(figsize=(5, 5))
image = Image.open(BytesIO(image_data ))
ax = plt.imshow(image, alpha=0.5)
for word in word_infos:
    bbox = [int(num) for num in word["boundingBox"].split(",")]
    text = word["text"]
    origin = (bbox[0], bbox[1])
    patch = Rectangle(origin, bbox[2], bbox[3],
                      fill=False, linewidth=2, color='y')
    ax.axes.add_patch(patch)
    plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
plt.show()
plt.axis("off")
print("done")

