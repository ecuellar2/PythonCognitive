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
from azure.cognitiveservices.vision.contentmoderator.models import (
    TermList,
    Terms,
    TermsData,
    RefreshIndex,
    Screen,
    Body
)
from msrest.authentication import CognitiveServicesCredentials

print("starting ")

key = ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/"
client = ContentModeratorClient(endpoint=endpoint_string,credentials=CognitiveServicesCredentials(key))

'''
file_path = "C:/code/images/content_moderator_text_moderation.txt"
# Screen the input text: check for profanity, do autocorrect text, and check for personally identifying information (PII)
with open(file_path , "rb") as text_fd:
    screen = client.text_moderation.screen_text(text_content_type="text/plain",text_content=text_fd,language="eng",autocorrect=True,pii=True)
pprint(screen.as_dict())
'''

# Create list 

#custom_list = client.list_management_term_lists.create(content_type="application/json",body="{""name"": ""Term list name"",""description"": ""Term list description"",}")

body_input = Body(name='Term list name', description='Term list description')
# needs work here !!!
custom_list = client.list_management_term_lists.create(content_type='application/json', body=body_input)
'''
custom_list = client.list_management_term_lists.create(
    content_type="application/json",
    body={
        "name": "Term list name",
        "description": "Term list description",
    }
)
'''

#pprint(custom_list.as_dict())
#list_id = custom_list.id

# Update list 
'''
print("Updating details for list {}".format(list_id))
updated_list = client.list_management_term_lists.update(list_id=list_id, content_type="application/json",
    body={
        "name": "New name",
        "description": "New description"
    }
)
pprint(updated_list.as_dict())
'''

# Add terms to list
'''
print("Adding terms to list {}".format(list_id))
client.list_management_term.add_term(list_id=list_id,term="term1",language="eng")
client.list_management_term.add_term(list_id=list_id,term="term2",language="eng")
'''

# Get all terms ids in list 
'''
print("Getting all term IDs for list {}".format(list_id))
terms = client.list_management_term.get_all_terms(list_id=list_id, language="eng")
terms_data = terms.data
pprint(terms_data.as_dict())
'''
#Whenever you add or remove terms from the list, you must refresh the index before you can use the updated list.
'''
print("\nRefreshing the search index for list {}".format(list_id))
refresh_index = client.list_management_term_lists.refresh_index_method(
    list_id=list_id, language="eng")
pprint(refresh_index.as_dict())
LATENCY_DELAY = 10 # seconds
print("\nWaiting {} minutes to allow the server time to propagate the index changes.".format(LATENCY_DELAY))
time.sleep(LATENCY_DELAY)
'''

# Screen text
#text_folder = "C:/code/images/text_files/content_moderator_term_list.txt"
'''
with open(os.path.join(TEXT_FOLDER, 'content_moderator_term_list.txt'), "rb") as text_fd:
    screen = client.text_moderation.screen_text(
        text_content_type="text/plain",
        text_content=text_fd,
        language="eng",
        autocorrect=False,
        pii=False,
        list_id=list_id
    )
    pprint(screen.as_dict())
'''

print("Done ")
