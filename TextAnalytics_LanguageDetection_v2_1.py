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

def language_detection():
    client = authenticateClient()

    try:
        documents = [
            {'id': '1', 'text': 'This is a document written in English.'},
            {'id': '2', 'text': 'Este es un document escrito en Español.'},
            {'id': '3', 'text': '这是一个用中文写的文件'}
        ]
        response = client.detect_language(documents=documents)

        for document in response.documents:
            print("Document Id: ", document.id, ", Language: ",
                  document.detected_languages[0].name)

    except Exception as err:
        print("Encountered exception. {}".format(err))
language_detection()

print("All done")
