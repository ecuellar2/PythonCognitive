#python -m pip install -U matplotlib
#python -m pip install -U Pillow
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services/Computer-vision/QuickStarts
# can save as .ipynb 

import os
import sys
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

print("starting ")

key = ""
endpoint = "https://southcentralus.api.cognitive.microsoft.com/vision/v2.1/models/landmarks/analyze?"
image_url = "https://upload.wikimedia.org/wikipedia/commons/f/f6/Bunker_Hill_Monument_2005.jpg"

headers = {'Ocp-Apim-Subscription-Key': key}
params = {'model': 'landmarks'}
data = {'url': image_url}
response = requests.post(endpoint, headers=headers, params=params, json=data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most relevant landmark for the image is obtained from the 'result' property.
analysis = response.json()
assert analysis["result"]["landmarks"] is not []
print(analysis)
landmark_name = analysis["result"]["landmarks"][0]["name"].capitalize()

# Display the image and overlay it with the landmark name.
image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
_ = plt.title(landmark_name, size="x-large", y=-0.1)
plt.show()
print("done")

