print("starting ")
#Know location such as  C:\Users\xxx\AppData\Local\Programs\Python\Python38-32
#python.exe -m pip install azure-ai-textanalytics

key = ""
endpoint = ""

from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential

def authenticate_client():
    ta_credential = TextAnalyticsApiKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
    endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def key_phrase_extraction_example(client):

    try:
        document = ["My cat might need to see a veterinarian."]

        response = client.extract_key_phrases(inputs= document)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        
key_phrase_extraction_example(client)


print("All done")
