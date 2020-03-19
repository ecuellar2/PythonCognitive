print("starting ")
#Know location such as  C:\Users\xxx\AppData\Local\Programs\Python\Python38-32
#python.exe -m pip install azure-ai-textanalytics
#docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/text-analytics-sdk
#github.com/Azure/azure-sdk-for-python/tree/master/sdk/textanalytics/azure-ai-textanalytics/samples


key = ""
endpoint = ""

from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential

def authenticate_client():
    ta_credential = TextAnalyticsApiKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
    endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def language_detection_example(client):
    try:
        #document = ["Hola como estas hoy? "]
        #response = client.detect_language(inputs = document, country_hint = 'us')[0]
        #print("Language: ", response.primary_language.name)

        documents = [
            "This document is written in English.",
            "Este es un document escrito en Español.",
            "这是一个用中文写的文件",
            "Dies ist ein Dokument in deutsche Sprache.",
            "Detta är ett dokument skrivet på engelska."
        ]

        response = client.detect_language(documents)

        for idx, doc in enumerate(response):
            if not doc.is_error:
                print("Document text: {}".format(documents[idx]))
                print("Language detected: {}".format(doc.primary_language.name))
                print("ISO6391 name: {}".format(doc.primary_language.iso6391_name))
                print("Confidence score: {}\n".format(doc.primary_language.score))
            if doc.is_error:
                print(doc.id, doc.error)
        
    except Exception as err:
        print("Encountered exception. {}".format(err))

language_detection_example(client)

print("All done")
