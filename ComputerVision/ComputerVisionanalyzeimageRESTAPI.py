#python -m pip install -U matplotlib
#python -m pip install -U Pillow
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services/Computer-vision/QuickStarts

import requests
import matplotlib.pyplot as plt
import json
from PIL import Image
from io import BytesIO


print("starting ")

key = ""
endpoint = "https://southcentralus.api.cognitive.microsoft.com/vision/v2.1/analyze?"
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

headers = {'Ocp-Apim-Subscription-Key': key}
params = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}
response = requests.post(endpoint, headers=headers,params=params, json=data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image, most relevant caption for the image is  the 'description' property.
analysis = response.json()
print(json.dumps(response.json()))
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
plt.show()
print("done")





