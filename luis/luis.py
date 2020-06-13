# python -m pip install azure-cognitiveservices-language-luis
# https://docs.microsoft.com/en-us/azure/cognitive-services/luis/sdk-authoring?tabs=windows&pivots=programming-language-python
# https://www.luis.ai
print("starting ")
from azure.cognitiveservices.language.luis.authoring import LUISAuthoringClient
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

import datetime, json, os, time

key = "xx"
endpoint_string = "https://westus.api.cognitive.microsoft.com/"
#app_id = "xx"
#endpoint that was published 
#https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/xx

 
# Instantiate a LUIS client
client = LUISAuthoringClient(endpoint_string, CognitiveServicesCredentials(key))
app_version = "0.1"
#create app
'''app_name    = "Contoso {}".format(datetime.datetime.now())
app_desc    = "Flight booking app built with LUIS Python SDK."
app_id = client.apps.add(dict(name=app_name,initial_version_id=app_version,description=app_desc,culture="en-us"))
print("Created LUIS app {}\n    with ID {}".format(app_name, app_id))
'''


#create intent  Intent FindFlights 
#intentId = client.model.add_intent(app_id, app_version, "FindFlights")

#create entities
'''
destinationEntityId = client.model.add_entity(app_id, app_version, name="Destination")
print("destinationEntityId {} added.".format(destinationEntityId))

classEntityId = client.model.add_entity(app_id, app_version, name="Class")
print("classEntityId {} added.".format(classEntityId))

flightEntityId = client.model.add_entity(app_id, app_version, name="Flight")
print("flightEntityId {} added.".format(flightEntityId))
# defaults as machine learned entities 

'''
#create utterances for FindFlights entity
def create_utterance(intent, utterance, *labels):
    '''
    Add an example LUIS utterance from utterance text and a list of labels.  
    Each label is a 2-tuple containing a label name and the text within the utterance that represents that label.
    Label is entity. Utterances have lables/entities. 
    '''
    text = utterance.lower()
    def label(name, value):
        value = value.lower()
        start = text.index(value)
        return dict(entity_name=name, start_char_index=start, end_char_index=start + len(value))

    return dict(text=text, intent_name=intent, entity_labels=[label(n, v) for (n, v) in labels])

utterances = [create_utterance("FindFlights", "find flights in economy to Madrid",
                            ("Flight", "economy to Madrid"),
                            ("Destination", "Madrid"),
                            ("Class", "economy")),
                  create_utterance("FindFlights", "find flights to London in first class",
                            ("Flight", "London in first class"),
                            ("Destination", "London"),
                            ("Class", "first")),
                  create_utterance("FindFlights", "find flights from seattle to London in first class",
                            ("Flight", "flights from seattle to London in first class"),
                            ("Destination", "London"),
                            ("Class", "first"))]

# Add the utterances in batch. 
#client.examples.batch(app_id, app_version, utterances)
#print("{} example utterance(s) added.".format(len(utterances)))

#train model 
'''
response = client.train.train_version(app_id, app_version)
waiting = True
while waiting:
    info = client.train.get_status(app_id, app_version)
    # get_status returns a list of training statuses, one for each model. Loop through them and make sure all are done.
    waiting = any(map(lambda x: 'Queued' == x.details.status or 'InProgress' == x.details.status, info))
    if waiting:
        print ("Waiting 4 seconds for training to complete...")
        time.sleep(4)
'''
'''
#publish endpoint 
responseEndpointInfo = client.apps.publish(app_id, app_version, is_staging=True)
print("Application published. Endpoint URL: " + responseEndpointInfo.endpoint_url)
'''

'''
https://westus.api.cognitive.microsoft.com/luis/prediction/v3.0/apps/app_id/slots/staging/predict?subscription-key=xxxx&verbose=true&show-all-intents=true&log=true&query=find flights business class to austin
https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/xxx?subscription-key=xxxx&q=find flights from seattle to london in first class
'''
request = { "query" : "Find business class flight to Austin" }
# Instantiate a LUIS runtime client
clientRuntime = LUISRuntimeClient(endpoint_string, CognitiveServicesCredentials(key))

# Note be sure to specify, using the slot_name parameter, whether your application is in staging or production.
#botbuilder-ai 4.9.1 has requirement azure-cognitiveservices-language-luis==0.2.0
#have azure-cognitiveservices-language-luis 0.6.0 which is incompatible, need .6 for get_slot_prediction()
#response = clientRuntime.prediction.get_slot_prediction(app_id=app_id, slot_name="staging", prediction_request=request)
request2 = "find flights from seattle to london in first class" 
response = clientRuntime.prediction.resolve(app_id=app_id, query=request2)  #using .2 api
print (response)
'''
#reponse from .6 API
print("Top intent: {}".format(response.prediction.top_intent))
print("Sentiment: {}".format (response.prediction.sentiment))
print("Intents: ")
for intent in response.prediction.intents:
	print("\t{}".format (json.dumps (intent)))
	print("Entities: {}".format (response.prediction.entities))
'''
print("Done ")

