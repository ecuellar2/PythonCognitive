# python -m pip install azure-cognitiveservices-knowledge-qnamaker
import os
import time

from azure.cognitiveservices.knowledge.qnamaker.authoring import QnAMakerClient
from azure.cognitiveservices.knowledge.qnamaker.runtime import QnAMakerRuntimeClient
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import QueryDTO
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import MetadataDTO
from msrest.authentication import CognitiveServicesCredentials

from config import DefaultConfig
CONFIG = DefaultConfig()
key = CONFIG.QNA_KEY       # grab key from Keys and Endpoint tab in portal resource
kb_id = CONFIG.QNA_KB_ID   # grab from qnamaker.ai, KB, settings

# from portal resource blade overview section
endpoint_string  = "https://qna_resource_name.cognitiveservices.azure.com"

client = QnAMakerClient(endpoint=endpoint_string, credentials=CognitiveServicesCredentials(key))

print("Getting runtime endpoint keys...")
keys = client.endpoint_keys.get_keys()
print("Primary runtime endpoint key: {}.".format(keys.primary_endpoint_key))

runtime_endpoint_string = "https://qna_resource_name.azurewebsites.net"

runtimeClient = QnAMakerRuntimeClient(runtime_endpoint=runtime_endpoint_string, credentials=CognitiveServicesCredentials(key))
AuthHeaderValue = "EndpointKey " + keys.primary_endpoint_key

metadata_filter = [MetadataDTO(name="key1", value="value1"), MetadataDTO(name="key2", value="value2") ]

question_payload = QueryDTO(question = "xxxx", strict_filters=metadata_filter,score_threshold=1, is_test="false",top=5)

listSearchResults = runtimeClient.runtime.generate_answer(kb_id=kb_id, generate_answer_payload=question_payload, 
custom_headers=dict(Authorization=AuthHeaderValue ))


for i in listSearchResults.answers:
    print(f"Answer ID: {i.id}.")
    print(f"Answer: {i.answer}.")
    print(f"Answer score: {i.score}.")


print ("done")

