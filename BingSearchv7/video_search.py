#python -m pip install azure-cognitiveservices-search-videosearch
#https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/tree/master/samples/search
#https://github.com/MicrosoftDocs/azure-docs/tree/master/articles/cognitive-services

import os
from azure.cognitiveservices.search.videosearch import VideoSearchClient
from azure.cognitiveservices.search.videosearch.models import VideoPricing, VideoLength, VideoResolution, VideoInsightModule
from msrest.authentication import CognitiveServicesCredentials

print("starting ")

key = ""
endpoint = "https://southcentralus.api.cognitive.microsoft.com/bing/v7.0/search?"
client = VideoSearchClient(endpoint, CognitiveServicesCredentials(key))
query_string = "SwiftKey"
'''
video_result = client.videos.search(query=query_string)
print ("Searching " + query_string )
if video_result.value:
    print("Video result count: {}".format(len(video_result.value)))
    first_video_result = video_result.value[0]
    print("First video id: {}".format(first_video_result.video_id))
    print("First video name: {}".format(first_video_result.name))
    print("First video url: {}".format(first_video_result.content_url))
'''
query_string2 = "Bellevue Trailer"
# Can also  use str "free" and  str "hd1080p"  str "short"
'''
video_result = client.videos.search(query=query_string2,pricing=VideoPricing.free, length=VideoLength.short, resolution=VideoResolution.hd1080p )
print("Search videos  that are free, short and 1080p resolution")
if video_result.value:
    print("Video result count: {}".format(len(video_result.value)))
    first_video_result = video_result.value[0]
    print("First video id: {}".format(first_video_result.video_id))
    print("First video name: {}".format(first_video_result.name))
    print("First video url: {}".format(first_video_result.content_url))
'''
trending_result = client.videos.trending()
#print("Search trending video")
#A tile is an interactive logo or image displayed next to a search result that helps people easily identify a trusted site
'''
if trending_result.banner_tiles:
    print("Banner tile count: {}".format(len(trending_result.banner_tiles)))
    first_banner_tile = trending_result.banner_tiles[0]
    print("First banner tile text: {}".format(first_banner_tile.query.text))
    print("First banner tile url: {}".format(first_banner_tile.query.web_search_url))
'''
'''
if trending_result.categories:
    print("Category count: {}".format(len(trending_result.categories)))
    first_category = trending_result.categories[0]
    print("First category title: {}".format(first_category.title))
    if first_category.subcategories:
        first_subcategory = first_category.subcategories[0]
        print("Subcategory count: {}".format(len(first_category.subcategories)))
        print("First subcategory title: {}".format(first_subcategory.title))
        if first_subcategory.tiles:
            first_tile = first_subcategory.tiles[0]
            print("Subcategory tile count: {}".format(len(first_subcategory.tiles)))
            print("First tile text: {}".format(first_tile.query.text))
            print("First tile url: {}".format(first_tile.query.web_search_url))

'''

#search videos and then search for detail information of the first video
print("new search ")
video_result = client.videos.search(query=query_string2 )
first_video_result = video_result.value[0]
# Can use ["all"] too
video_details = client.videos.details(query=query_string2,id=first_video_result.video_id,modules=[VideoInsightModule.all] )

if video_details.video_result:
    print("Expected Video id: {}".format(video_details.video_result.video_id))
    print("Expected Video name: {}".format(video_details.video_result.name))
    print("Expected Video url: {}".format(video_details.video_result.content_url))

if video_details.related_videos.value:
    print("Related video count: {}".format(len(video_details.related_videos.value)))
    first_related_video = video_details.related_videos.value[0]
    print("First related video id: {}".format(first_related_video.video_id))
    print("First related video name: {}".format(first_related_video.name))
    print("First related video content url: {}".format(first_related_video.content_url))

print("done")

