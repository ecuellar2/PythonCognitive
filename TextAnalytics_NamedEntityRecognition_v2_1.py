print("starting ")
#Know location such as  C:\Users\xxx\AppData\Local\Programs\Python\Python38-32
#python.exe -m pip install azure-cognitiveservices-language-textanalytics
#docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/text-analytics-sdk

subscription_key = ""
endpoint = ""

import os
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

def authenticateClient():
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credentials=credentials)
    return text_analytics_client

def entity_recognition():
    
    client = authenticateClient()

    try:
        documents = [
            {"id": "1", "language": "en", "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, to develop and sell BASIC interpreters for the Altair 8800."},
            {"id": "2", "language": "es",
                "text": "La sede principal de Microsoft se encuentra en la ciudad de Redmond, a 21 kilómetros de Seattle."}
        ]
        response = client.entities(documents=documents)

        for document in response.documents:
            print("Document Id: ", document.id)
            print("\tKey Entities:")
            for entity in document.entities:
                print("\t\t", "NAME: ", entity.name, "\tType: ",
                      entity.type, "\tSub-type: ", entity.sub_type)
                for match in entity.matches:
                    print("\t\t\tOffset: ", match.offset, "\tLength: ", match.length, "\tScore: ",
                          "{:.2f}".format(match.entity_type_score))
#docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/concepts/text-offsets
    except Exception as err:
        print("Encountered exception. {}".format(err))
entity_recognition()

print("All done")
