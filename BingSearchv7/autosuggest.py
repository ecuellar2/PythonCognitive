# python -m pip install azure-cognitiveservices-search-autosuggest
import os
from azure.cognitiveservices.search.autosuggest import AutoSuggestClient
from azure.cognitiveservices.search.autosuggest.models import (
    Suggestions,
    SuggestionsSuggestionGroup,
    SearchAction,
    ErrorResponseException
)
from msrest.authentication import CognitiveServicesCredentials

print("starting ")
subscription_key =  ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?"

client = AutoSuggestClient(endpoint=endpoint_string,credentials=CognitiveServicesCredentials(subscription_key))
suggestions = client.auto_suggest(query="Satya Nadella") 
if suggestions.suggestion_groups:
    print("Searched for \"Satya Nadella\" and found suggestions:")
    suggestion_group = suggestions.suggestion_groups[0] 
    for suggestion in suggestion_group.search_suggestions:  
        print("....................................")
        print(suggestion.query)
        print(suggestion.display_text)
        print(suggestion.url)
        print(suggestion.search_kind)
