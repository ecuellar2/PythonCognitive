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

def entity_recognition_example(client):

    try:
        document = ["I had a wonderful trip to France last week. I used SSN 123-12-1234 to travel."]
        result = client.recognize_entities(inputs= document)[0]

        print("Named Entities:\n")
        for entity in result.entities:
            print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                    "\n\tConfidence Score: \t", round(entity.score, 2), "\n")


        result2 = client.recognize_pii_entities(inputs= document)[0]
        
        print("Personally Identifiable Information Entities: ")
        for entity in result2.entities:
            print("\tText: ",entity.text,"\tCategory: ", entity.category,"\tSubCategory: ", entity.subcategory)
            print("\tScore: {0:.2f}".format(entity.score), "\n")
        
        result3 = client.recognize_linked_entities(inputs= document)[0]
        
        print("Linked Entities:\n")
        for entity in result3.entities:
            print("\tName: ", entity.name, "\tUrl: ", entity.url,
            "\n\tData Source: ", entity.data_source)
            print("\tMatches:")
            for match in entity.matches:
                print("\t\tText:", match.text)
                print("\t\tScore: {0:.2f}".format(match.score) )
         


    except Exception as err:
        print("Encountered exception. {}".format(err))

entity_recognition_example(client)


print("All done")
