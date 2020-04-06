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
if hasattr(web_data.web_pages, 'value'):

    print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

    first_web_page = web_data.web_pages.value[0]
    print("First web page name: {} ".format(first_web_page.name))
    print("First web page URL: {} ".format(first_web_page.url))

else:
    print("Didn't find any web pages...")

print("done")
