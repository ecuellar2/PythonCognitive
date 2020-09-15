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
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import CreateKbDTO, UpdateKbOperationDTO, UpdateKbOperationDTOAdd
from msrest.authentication import CognitiveServicesCredentials

print("starting ")

key = "grab key from Keys and Endpoint tab in portal resource"
endpoint_string = "https://qna_resource_name.cognitiveservices.azure.com" 

client = QnAMakerClient(endpoint=endpoint_string, credentials=CognitiveServicesCredentials(key))
#create_op = client.knowledgebase.create(create_kb_payload=create_kb_dto)  
#operation = client.operations.get_details(operation_id=operation_id)
kb_id = "grab from qnamaker.ai, KB, settings, "

update_kb_operation_dto = UpdateKbOperationDTO(add=UpdateKbOperationDTOAdd(
    qna_list=[
                QnADTO(questions=["What is xxx?"], 
                answer="The answer is xxx.",
                metadata=[MetadataDTO(name="Location", value="Austin")]
                )
            ]
        )
    )


#update_op = client.knowledgebase.update(kb_id=kb_id, update_kb=update_kb_operation_dto)
#print (update_op.operation_id)


#client.knowledgebase.publish(kb_id=kb_id)
#kb_data = client.knowledgebase.download(kb_id=kb_id, environment="Prod")
#print("KB Downloaded. It has {} QnAs.".format(len(kb_data.qna_documents)))
#client.knowledgebase.delete(kb_id=kb_id)



print("Done ")
