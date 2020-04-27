#python -m pip install azure-cognitiveservices-search-newssearch
#https://docs.microsoft.com/en-us/azure/cognitive-services/bing-web-search/quickstarts/client-libraries?pivots=programming-language-python
#https://github.com/Azure/azure-sdk-for-python/tree/master/sdk

import os
from azure.cognitiveservices.search.newssearch import NewsSearchClient
from msrest.authentication import CognitiveServicesCredentials

print("starting ")

key = ""
endpoint = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?"

client = NewsSearchClient(endpoint=endpoint,credentials=CognitiveServicesCredentials(key))
search_string = "Artificial Intelligence"  #"Quantum Computing"
print("Search news for query " + search_string  + " with market and count")
# news search with market and count 
'''
news_result = client.news.search(query=search_string, market="en-us", count=10)
if news_result.value:
    print("Total estimated matches value: {}".format(news_result.total_estimated_matches))
    print("News result count: {}".format(len(news_result.value)))
    first_news_result = news_result.value[0]
    print("First news name: {}".format(first_news_result.name))
    print("First news url: {}".format(first_news_result.url))
    print("First news description: {}".format(first_news_result.description))
    print("First published time: {}".format(first_news_result.date_published))
    print("First news provider: {}".format(first_news_result.provider[0].name))
'''
# news search with freshness and sort
#news_result = client.news.search(query=search_string,market="en-us",freshness="Week",sort_by="Date")

#search category news for movie and TV entertainment, safe search, notice that query search string not in use 
'''
news_result = client.news.category(category="Entertainment_MovieAndTV", market="en-us", safe_search="strict")
print("Searching for category  " )
if news_result.value:
    print("News result count: {}".format(len(news_result.value)))
    first_news_result = news_result.value[0]
    print("First news category: {}".format(first_news_result.category))
    print("First news name: {}".format(first_news_result.name))
    print("First news url: {}".format(first_news_result.url))
    print("First news description: {}".format(first_news_result.description))
    print("First published time: {}".format(first_news_result.date_published))
    print("First news provider: {}".format(first_news_result.provider[0].name))
'''
#search trending,  notice that query search string not in use 
trending_topics = client.news.trending(market="en-us")
print("Searching for trending " )
if trending_topics.value:
    print("News result count: {}".format(len(trending_topics.value)))
    first_topic = trending_topics.value[0]
    print("First topic name: {}".format(first_topic.name))
    print("First topic query: {}".format(first_topic.query.text))
    print("First topic image url: {}".format(first_topic.image.url))
    print("First topic webSearchUrl: {}".format(first_topic.web_search_url))
    print("First topic newsSearchUrl: {}".format(first_topic.news_search_url))

print("done")

