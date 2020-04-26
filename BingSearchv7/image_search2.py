# python -m pip install azure-cognitiveservices-search-imagesearch
#https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/tree/master/samples/search
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services

import os
from azure.cognitiveservices.search.imagesearch import ImageSearchClient
from azure.cognitiveservices.search.imagesearch.models import ImageType, ImageAspect, ImageInsightModule
from msrest.authentication import CognitiveServicesCredentials

print("starting *******")
subscription_key =  ""
endpoint_string = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?"
search_term = "canadian rockies"

"""
Will search images on the web with the Bing Image Search API 
param count: The number of images to return in the response. The
 actual number delivered may be less than requested. The default is 35.  
 The maximum value is 150. You use this parameter along with the offset  
 parameter to page results.For example, if your user interface displays  
 20 images per page, set count to 20 and offset to 0 to get the first  
 page of results.For each subsequent page, increment offset by 20 (for  
 example, 0, 20, 40). Use this parameter only with the Image Search  
 API.Do not specify this parameter when calling the Insights, Trending  
 Images, or Web Search APIs. 
"""
client = ImageSearchClient(endpoint_string, CognitiveServicesCredentials(subscription_key))
image_results = client.images.search(query=search_term, count=14)  

#print("Searching the web for images of: {}".format(search_term))

if image_results.value: 
    first_image_result = image_results.value[0]
    print("Image result count: {}".format(len(image_results.value)))  # image_results.value  this is number returned out of the total estimated matches
    #print("First image insights token: {}".format(first_image_result.image_insights_token))
    #print("First image thumbnail url: {}".format(first_image_result.thumbnail_url))
   # print("First image content url: {}".format(first_image_result.content_url))
'''
Bing returns a subset of the total number of results that may be relevant to the query. 
To get the estimated total number of available results, access the answer object's totalEstimatedMatches field.
https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#totalestimatedmatches
'''
print("Image result total estimated matches: {}".format(image_results.total_estimated_matches)) # image_results.total_estimated_matches
#print("Image result next offset: {}".format(image_results.next_offset))
'''
If you want to display 15 results per page, you would set count to 15 and offset to 0 to get the first page of results. 
For each subsequent API call, you would increment offset by 15.

Pivot suggestions can be displayed as optional search terms to the user. 
For example, if the original query was Microsoft Surface, Bing might segment the query into Microsoft and Surface and provide suggested pivots for each
'''
'''
if image_results.pivot_suggestions:
    first_pivot = image_results.pivot_suggestions[0]
    #print("Pivot suggestion count: {}".format(len(image_results.pivot_suggestions)))
    #print("First pivot: {}".format(first_pivot.pivot))
    if first_pivot.suggestions:
        first_suggestion = first_pivot.suggestions[0]
        print("Pivot suggestion count: {}".format( len(first_pivot.suggestions)))
        print("Pivot first suggestion text: {}".format(first_suggestion.text))
        print("pivot first suggestion web search url: {}".format(first_suggestion.web_search_url))
'''
'''
If Bing can expand the query to narrow the original search, the Images object contains the queryExpansions 
This is different than pivot.
'''
'''
if image_results.query_expansions:
    first_query_expansion = image_results.query_expansions[0]
    print("Query expansion count: {}".format(len(image_results.query_expansions)))
    print("First query expansion text: {}".format(first_query_expansion.text))
    print("First query expansion search link: {}".format(first_query_expansion.search_link))
'''

# example below is using image type filter,  could also have used str "AnimatedGif" and str "Wide"
'''
search_term2 = "studio ghibli"
image_results2 = client.images.search(query=search_term2, image_type=ImageType.animated_gif,  aspect=ImageAspect.wide, count=32 )
print("Search images for "+ search_term2 +  " results that are animated gifs and wide aspect")
if image_results2.value:
    first_image_result2 = image_results2.value[0]
    print("Image result count: {}".format(len(image_results2.value)))
    print("First image insights token: {}".format(first_image_result2.image_insights_token))
    print("First image thumbnail url: {}".format(first_image_result2.thumbnail_url))
    print("First image web search url: {}".format(first_image_result2.web_search_url))
'''

# search trending images 
# tile is a list of images that are trending in the category. Each tile contains an image and a URL that returns more images of the subject. 
# For example, if the category is Popular People Searches, the image is of a popular person and the URL would return more images of that person.

'''
trending_result = client.images.trending()
print("Search trending images")
# Categorires
if trending_result.categories:
    first_category = trending_result.categories[0]
    print("Category count: {}".format(len(trending_result.categories)))
    print("First category title: {}".format(first_category.title))
    if first_category.tiles:
        first_tile = first_category.tiles[0]
        print("Subcategory tile count: {}".format(len(first_category.tiles)))
        print("First tile text: {}".format(first_tile.query.text))
        print("First tile url: {}".format(first_tile.query.web_search_url))
'''
search_term3 = "degas"
print("Search images for " + search_term3)
image_results3 = client.images.search(query=search_term3, count=24 )
first_image = image_results3.value[0]
 # modules paramter could be the str "all", search images and then search for image details of the first image.
image_detail = client.images.details(query=search_term3, insights_token=first_image.image_insights_token,
modules=[ImageInsightModule.all ],)

#print("Search detail for image insights token: {}".format(first_image.image_insights_token))
#print("Expected image insights token: {}".format(image_detail.image_insights_token))

# Image tags used to associate images with tags, like type of clouds in an image
if image_detail.image_tags.value:
    print("Image tags count: {}".format(len(image_detail.image_tags.value)))
    first_image_tag = image_detail.image_tags.value[0]
    print("First tag name: {}".format(first_image_tag.name))


#Gets the query term that best represents the image. 
'''
if image_detail.best_representative_query:
    print("Best representative query text: {}".format(image_detail.best_representative_query.text))
    print("Best representative query web search url: {}".format(image_detail.best_representative_query.web_search_url))
'''
'''
if image_detail.image_caption:
    print("Image caption: {}".format(image_detail.image_caption.caption))
    print("Image caption data source url: {}".format(image_detail.image_caption.data_source_url))
'''
#pagesIncluding - Web pages that include the image
'''
if image_detail.pages_including.value:
    first_page = image_detail.pages_including.value[0]
    print("Pages including count: {}".format(len(image_detail.pages_including.value)))
    print("First page content url: {}".format(first_page.content_url))
    print("First page name: {}".format(first_page.name))
    print("First page date published: {}".format(first_page.date_published))
'''
#relatedSearches - searches based on details in the image.
'''
if image_detail.related_searches.value:
    first_related_search = image_detail.related_searches.value[0]
    print("Related searches count: {}".format(len(image_detail.related_searches.value)))
    print("First related search text: {}".format(first_related_search.text))
    print("First related search web search url: {}".format(first_related_search.web_search_url))
'''
'''
if image_detail.visually_similar_images.value:
    first_visually_similar_images = image_detail.visually_similar_images.value[0]
    print("Visually similar images count: {}".format(len(image_detail.visually_similar_images.value)))
    print("First visually similar image name: {}".format(first_visually_similar_images.name))
    print("First visually similar image content url: {}".format(first_visually_similar_images.content_url))
    print("First visually similar image content size: {}".format(first_visually_similar_images.content_size))
'''

print("done  ")



