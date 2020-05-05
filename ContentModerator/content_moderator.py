#python -m pip install azure-cognitiveservices-vision-contentmoderator
#pip install --upgrade azure-cognitiveservices-vision-contentmoderator
#https://docs.microsoft.com/en-us/azure/cognitive-services/Content-Moderator/client-libraries?pivots=programming-language-python#use-a-custom-image-list

import os.path
from pprint import pprint
import time
from io import BytesIO
from random import random
import uuid

from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
import azure.cognitiveservices.vision.contentmoderator.models
from msrest.authentication import CognitiveServicesCredentials

print("starting ")

key = ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/"
client = ContentModeratorClient(endpoint=endpoint_string,credentials=CognitiveServicesCredentials(key))
file_path = "C:/code/images/content_moderator_text_moderation.txt"

# Screen the input text: check for profanity,
# do autocorrect text, and check for personally identifying
# information (PII)
with open(file_path , "rb") as text_fd:
    screen = client.text_moderation.screen_text(
        text_content_type="text/plain",
        text_content=text_fd,
        language="eng",
        autocorrect=True,
        pii=True
    )

pprint(screen.as_dict())
