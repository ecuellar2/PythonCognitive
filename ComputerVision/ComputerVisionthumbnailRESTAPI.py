#python -m pip install -U matplotlib
#python -m pip install -U Pillow
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services/Computer-vision/QuickStarts
#https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/cognitive-services/Computer-vision/QuickStarts/python-thumb.md
# can save as .ipynb 

import os
import sys
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

print("starting ")

key = ""
endpoint = "https://southcentralus.api.cognitive.microsoft.com/vision/v2.1/generateThumbnail?"
image_url = "https://upload.wikimedia.org/wikipedia/commons/9/94/Bloodhound_Puppy.jpg"


headers = {'Ocp-Apim-Subscription-Key': key}
params = {'width': '50', 'height': '50', 'smartCropping': 'true'}
data = {'url': image_url}
response = requests.post(endpoint , headers=headers,params=params, json=data)
response.raise_for_status() # raises error if occurred 
thumbnail = Image.open(BytesIO(response.content))

# Display the thumbnail.
plt.imshow(thumbnail)

plt.axis("off")
print("Thumbnail is {0}-by-{1}".format(*thumbnail.size))

print("done")

