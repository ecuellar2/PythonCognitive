# python -m pip install azure-cognitiveservices-knowledge-qnamaker
# https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/quickstarts/quickstart-sdk?pivots=programming-language-python
# https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-knowledge-qnamaker/azure.cognitiveservices.knowledge.qnamaker?view=azure-python
# https://www.qnamaker.ai/

import os
import time

#0.2.0 (2020-03-17)  The QnAMakerClient client moved from knowledge.qnamaker to knowledge.qnamaker.authoring
from azure.cognitiveservices.knowledge.qnamaker.authoring import QnAMakerClient
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import MetadataDTO, QnADTO, QnADTOContext, PromptDTOQna, PromptDTO, ContextDTO
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import QueryDTOContext, QueryDTO, QueryContextDTO, QnASearchResultContext, QnASearchResult
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import QnASearchResultList, FeedbackRecordDTO, FeedbackRecordsDTO
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import OperationStateType
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import CreateKbDTO
from msrest.authentication import CognitiveServicesCredentials

print("starting ")

key = ""
#endpoint_string = "https://xxx.cognitiveservices.azure.com/qnamaker/v4.0" #  westus
#endpoint_string = https://westus.api.cognitive.microsoft.com
endpoint_string = "https://xxx.cognitiveservices.azure.com"

client = QnAMakerClient(endpoint=endpoint_string, credentials=CognitiveServicesCredentials(key))

qna = QnADTO(answer="You can use our REST APIs to manage your knowledge base.",
             questions=["How do I manage my knowledgebase?"],
             metadata=[MetadataDTO(name="Category", value="api")]
            )

urls = ["https://docs.microsoft.com/en-in/azure/cognitive-services/qnamaker/faqs"]

create_kb_dto = CreateKbDTO(name="QnA Maker FAQ from quickstart", qna_list=[qna],urls=urls)
create_op = client.knowledgebase.create(create_kb_payload=create_kb_dto)  

print(create_op.operation_state)
print(create_op.operation_id)
print (create_op.resource_location)
'''
for i in range(20):
    if create_op.operation_state in [OperationStateType.not_started, OperationStateType.running]:
        print("Waiting for operation: {} to complete.".format(create_op.operation_id))
        time.sleep(5)
        operation = client.operations.get_details(operation_id=create_op.operation_id)
    else:
        break
if operation.operation_state != OperationStateType.succeeded:
    raise Exception("Operation {} failed to complete.".format(create_op.operation_id))
'''

print("Done ")
