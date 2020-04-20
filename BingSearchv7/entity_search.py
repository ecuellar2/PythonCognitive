#python -m pip install azure-cognitiveservices-search-entitysearch
#https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/tree/master/samples/search
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services
import os

from azure.cognitiveservices.search.entitysearch import EntitySearchClient
from azure.cognitiveservices.search.entitysearch.models import Place, ErrorResponseException
from msrest.authentication import CognitiveServicesCredentials

print("starting ")
subscription_key =  ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?"
client = EntitySearchClient(endpoint=endpoint_string, credentials=CognitiveServicesCredentials(subscription_key) )
query_string = "William Gates"
#query_string = "George Washington"
entity_data = client.entities.search(query=query_string)
if entity_data.entities.value:
    # find the entity that represents the dominant one
    main_entities = [entity for entity in entity_data.entities.value if entity.entity_presentation_info.entity_scenario == "DominantEntity"]
    disambig_entities = [entity for entity in entity_data.entities.value if entity.entity_presentation_info.entity_scenario == "DisambiguationItem"]
    if main_entities:
        print( "Searched for " + query_string + " and found a dominant entity with this description:")
        print(main_entities[0].description)
    
    if disambig_entities:
        print("\nThis query is pretty ambiguous and can be referring to multiple things. Did you mean one of these:")
        suggestions = []
        for disambig_entity in disambig_entities:
            suggestions.append("{} the {}".format(disambig_entity.name, disambig_entity.entity_presentation_info.entity_type_display_hint))
        print(", or ".join(suggestions))

restaurant_name = "john howie bellevue"
restaurant_data = client.entities.search(query=restaurant_name )
if restaurant_data.places.value:
    restaurant = restaurant_data.places.value[0]
    try:
        telephone = restaurant.telephone
        print("Searched for " + restaurant_name + " and found a restaurant with this phone number: " + restaurant.telephone) 
    except AttributeError:
        print("Could not find phone number ! ")

# different approach using isinstance to get phone number
    if isinstance(restaurant, Place):
        print("Searched for " + restaurant_name + " and found a restaurant with this phone number: " + restaurant.telephone )
    else:
        print("Could not find a place! ")

restaurants = client.entities.search(query="Austin restaurants")
if restaurants.places.value:
    # get all the list items that relate to this query
    list_items = [entity for entity in restaurants.places.value if entity.entity_presentation_info.entity_scenario == "ListItem"]
    if list_items:
        suggestions = []
        for place in list_items:
            try: suggestions.append("{} ({})".format(place.name, place.telephone))
            except AttributeError:print("Unexpectedly found something that isn\'t a place named '{}'", place.name)
        print("We found these places: ")
        print(", ".join(suggestions))
