#  https://docs.microsoft.com/en-us/azure/search/cognitive-search-tutorial-blob-python

import json
import requests
from pprint import pprint

print("starting ")

# Define the names for the data source, skillset, index and indexer


index_name = "cogsrch-py-index"   # hotels-sample-index
indexer_name = "cogsrch-py-indexer"  # hotels-sample-indexer
storage_string = "DefaultEndpointsProtocol=https;AccountName=cogecstorage;AccountKey=MCObIPz9qWbU+MHFpXyw66+6UZT6ulhn8HYD8vghdJ41BuLEsb+iNsIvXi1NVH3k0LDvaY0kI9i1ou1SFBUVyg==;EndpointSuffix=core.windows.net"

endpoint = "https://xx.search.windows.net/"
headers = {'Content-Type': 'application/json',
        'api-key': "xx" }
params = {
    'api-version': '2020-06-30'
}

# Create a data source
datasource_name = "cogsrch-py-datasource"  
datasourceConnectionString = storage_string
datasource_payload = {
    "name": datasource_name,
    "description": "Demo files to demonstrate cognitive search capabilities.",
    "type": "azureblob",
    "credentials": {
        "connectionString": datasourceConnectionString
    },
    "container": {
        "name": "cog-search-demo"
    }
}
#r = requests.put(endpoint + "/datasources/" + datasource_name,data=json.dumps(datasource_payload), headers=headers, params=params)
#print(r.status_code)   #201 success
#############################################################################################################
#Each enrichment step is a skill, and the set of enrichment steps a skillset. 
skillset_name = "cogsrch-py-skillset" 

# Create a skillset with 4 built in skills EntityRecognitionSkill, LanguageDetectionSkill, SplitSkill, KeyPhraseExtractionSkill
skillset_payload = {
    "name": skillset_name,
    "description":
    "Extract entities, detect language and extract key-phrases",
    "skills":
    [
        {
            "@odata.type": "#Microsoft.Skills.Text.EntityRecognitionSkill",
            "categories": ["Organization"],
            "defaultLanguageCode": "en",
            "inputs": [
                {
                    "name": "text", 
                    "source": "/document/content"
                }
            ],
            "outputs": [
                {
                    "name": "organizations", 
                    "targetName": "organizations"
                }
            ]
        },
        {
            "@odata.type": "#Microsoft.Skills.Text.LanguageDetectionSkill",
            "inputs": [
                {
                    "name": "text", 
                    "source": "/document/content"
                }
            ],
            "outputs": [
                {
                    "name": "languageCode",
                    "targetName": "languageCode"
                }
            ]
        },
        {
            "@odata.type": "#Microsoft.Skills.Text.SplitSkill",
            "textSplitMode": "pages",
            "maximumPageLength": 4000,
            "inputs": [
                {
                    "name": "text",
                    "source": "/document/content"
                },
                {
                    "name": "languageCode",
                    "source": "/document/languageCode"
                }
            ],
            "outputs": [
                {
                    "name": "textItems",
                    "targetName": "pages"
                }
            ]
        },
        {
            "@odata.type": "#Microsoft.Skills.Text.KeyPhraseExtractionSkill",
            "context": "/document/pages/*",
            "inputs": [
                {
                    "name": "text", 
                    "source": "/document/pages/*"
                },
                {
                    "name": "languageCode", 
                    "source": "/document/languageCode"
                }
            ],
            "outputs": [
                {
                    "name": "keyPhrases",
                    "targetName": "keyPhrases"
                }
            ]
        }
    ]
}
# KeyPhraseExtraction skill is applied for each page
# document/pages/* means run enricher for each member of the document/pages array (for each page in the document).
# the other skills reference source as /document/content, text found in source file is placed in content field, one for each document
#r = requests.put(endpoint + "/skillsets/" + skillset_name,data=json.dumps(skillset_payload), headers=headers, params=params)
#print(r.status_code)

# Create an index
index_payload = {
    "name": index_name,
    "fields": [
        {
            "name": "id",
            "type": "Edm.String",
            "key": "true",
            "searchable": "true",
            "filterable": "false",
            "facetable": "false",
            "sortable": "true"
        },
        {
            "name": "content",
            "type": "Edm.String",
            "sortable": "false",
            "searchable": "true",
            "filterable": "false",
            "facetable": "false"
        },
        {
            "name": "languageCode",
            "type": "Edm.String",
            "searchable": "true",
            "filterable": "false",
            "facetable": "false"
        },
        {
            "name": "keyPhrases",
            "type": "Collection(Edm.String)",
            "searchable": "true",
            "filterable": "false",
            "facetable": "false"
        },
        {
            "name": "organizations",
            "type": "Collection(Edm.String)",
            "searchable": "true",
            "sortable": "false",
            "filterable": "false",
            "facetable": "false"
        }
    ]
}

#r = requests.put(endpoint + "/indexes/" + index_name, data=json.dumps(index_payload), headers=headers, params=params)
#print(r.status_code)


'''
The "fieldMappings" are processed before the skillset, mapping source fields from the data source to target fields in an index. 
If field names and types are the same at both ends, no mapping is required.

The "outputFieldMappings" are processed after the skillset, referencing "sourceFieldNames" that don't exist until document cracking or 
enrichment creates them. The "targetFieldName" is a field in an index.
'''

# Create an indexer
indexer_payload = {
    "name": indexer_name,
    "dataSourceName": datasource_name,
    "targetIndexName": index_name,
    "skillsetName": skillset_name,
    "fieldMappings": [
        {
            "sourceFieldName": "metadata_storage_path",
            "targetFieldName": "id",
            "mappingFunction":
            {"name": "base64Encode"}
        },
        {
            "sourceFieldName": "content",
            "targetFieldName": "content"
        }
    ],
    "outputFieldMappings":
    [
        {
            "sourceFieldName": "/document/organizations",
            "targetFieldName": "organizations"
        },
        {
            "sourceFieldName": "/document/pages/*/keyPhrases/*",
            "targetFieldName": "keyPhrases"
        },
        {
            "sourceFieldName": "/document/languageCode",
            "targetFieldName": "languageCode"
        }
    ],
    "parameters":
    {
        "maxFailedItems": -1,
        "maxFailedItemsPerBatch": -1,
        "configuration":
        {
            "dataToExtract": "contentAndMetadata",
            "imageAction": "generateNormalizedImages"
        }
    }
}
'''
maxFailedItems  -1   instructs the indexing engine to ignore errors during data import because there are so few documents
"dataToExtract":"contentAndMetadata"  tells the indexer to extract the content from different file formats and the metadata related to each file.

"imageAction":"generateNormalizedImages" configuration, combined with the OCR Skill and Text Merge Skill,
 tells the indexer to extract text from the images (for example, the word "stop" from a traffic Stop sign), and 
 embed it as part of the content field. This behavior applies to both the images embedded in the documents 
 (think of an image inside a PDF) and images found in the data source, for instance a JPG file.

'''

#r = requests.put(endpoint + "/indexers/" + indexer_name,data=json.dumps(indexer_payload), headers=headers, params=params)
#print(r.status_code)
#r = requests.get(endpoint + "/indexers/" + indexer_name + "/status", headers=headers, params=params)
#pprint(json.dumps(r.json(), indent=1))

#Submit a second query for "*" to return all contents of a single field organizations
r = requests.get(endpoint + "/indexes/" + index_name + "/docs?&search=*&$top=2&$select=organizations", headers=headers, params=params)
pprint(json.dumps(r.json(), indent=1))

print("done")

