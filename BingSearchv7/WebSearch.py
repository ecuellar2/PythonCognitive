#python -m pip install azure-cognitiveservices-search-websearch
#C:\Users\xxx\AppData\Local\Programs\Python\Python38-32\python.exe -m venv mytestenv
#mytestenv\Scripts\activate.bat
#https://docs.microsoft.com/en-us/azure/cognitive-services/bing-web-search/quickstarts/client-libraries?pivots=programming-language-python
#https://github.com/Azure/azure-sdk-for-python/tree/master/sdk


from azure.cognitiveservices.search.websearch import WebSearchClient
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

print("starting ")

key = "xx"
endpoint = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?"

#curl -X GET "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?q=metallica" -H "Ocp-Apim-Subscription-Key: xxx" -H "Content-Type: application/json"

client = WebSearchClient(endpoint, CognitiveServicesCredentials(key))
web_data = client.web.search(query="Yosemite")


print("sent search query ")
'''
Web pages
If the search response contains web pages, the first result's name and url
are printed.
'''

if hasattr(web_data.web_pages, 'value'):

    print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

    first_web_page = web_data.web_pages.value[0]
    print("First web page name: {} ".format(first_web_page.name))
    print("First web page URL: {} ".format(first_web_page.url))

else:
    print("Didn't find any web pages...")


'''
Images
If the search response contains images, the first result's name and url
are printed.
'''
if hasattr(web_data.images, 'value'):

    print("\r\nImage Results#{}".format(len(web_data.images.value)))

    first_image = web_data.images.value[0]
    print("First Image name: {} ".format(first_image.name))
    print("First Image URL: {} ".format(first_image.url))

else:
    print("Didn't find any images...")

'''
News
If the search response contains news, the first result's name and url
are printed.
'''
if hasattr(web_data.news, 'value'):

    print("\r\nNews Results#{}".format(len(web_data.news.value)))

    first_news = web_data.news.value[0]
    print("First News name: {} ".format(first_news.name))
    print("First News URL: {} ".format(first_news.url))

else:
    print("Didn't find any news...")

'''
If the search response contains videos, the first result's name and url
are printed.
'''
if hasattr(web_data.videos, 'value'):

    print("\r\nVideos Results#{}".format(len(web_data.videos.value)))

    first_video = web_data.videos.value[0]
    print("First Videos name: {} ".format(first_video.name))
    print("First Videos URL: {} ".format(first_video.url))

else:
    print("Didn't find any videos...")

print("done")
