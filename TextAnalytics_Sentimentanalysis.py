print("starting ")
#Know location such as  C:\Users\xxx\AppData\Local\Programs\Python\Python38-32
#python.exe -m pip install azure-ai-textanalytics
#references
#https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/text-analytics-sdk?tabs=version-3&pivots=programming-language-python
#https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-sentiment-analysis?tabs=version-3

key = "xx"
endpoint = "xx"

from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential

def authenticate_client():
    ta_credential = TextAnalyticsApiKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
    endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def sentiment_analysis_example(client):

    document = ["I had the best day of my life. I wish you were there with me."]
    response = client.analyze_sentiment(inputs=document)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.3f}; neutral={1:.3f}; negative={2:.3f} \n".format(
        response.sentiment_scores.positive,
        response.sentiment_scores.neutral,
        response.sentiment_scores.negative,
    ))

    #for idx, sentence in enumerate(response.sentences):
    #    print("[Offset: {}, Length: {}]".format(sentence.offset, sentence.length))
    #    print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
    #    print("Sentence score:\nPositive={0:.3f}\nNeutral={1:.3f}\nNegative={2:.3f}\n".format(
    #        sentence.sentiment_scores.positive,
    #        sentence.sentiment_scores.neutral,
    #        sentence.sentiment_scores.negative,
    #    ))

sentiment_analysis_example(client)

print("All done")
