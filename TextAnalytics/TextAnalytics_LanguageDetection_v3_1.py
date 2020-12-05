print("starting ")
# Know location such as  C:\Users\xxx\AppData\Local\Programs\Python\Python38-32
# C:\python\python.exe -m pip install azure-ai-textanalytics --pre

key = "xx"
endpoint = "https://x.cognitiveservices.azure.com/"


from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()
'''
In some cases it may be hard to disambiguate languages based on the input. 
You can use the country_hint parameter to specify a 2-letter country code. 
By default the API is using the US as the default countryHint
'''
def language_detection_example(client):
    try:
        documents = ["Ce document est rédigé en Français."]
        response = client.detect_language(documents = documents, country_hint = 'us')[0]
        print("Language: ", response.primary_language.name)

    except Exception as err:
        print("Encountered exception. {}".format(err))
language_detection_example(client)

print("All done")
