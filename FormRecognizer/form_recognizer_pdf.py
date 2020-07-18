# python -m pip install azure-ai-formrecognizer
# https://docs.microsoft.com/en-us/azure/cognitive-services/form-recognizer/quickstarts/client-library?tabs=windows&pivots=programming-language-python#recognize-form-content

print("starting ")
import os
import azure.ai.formrecognizer
from azure.ai.formrecognizer import FormRecognizerClient
from azure.ai.formrecognizer import FormTrainingClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceNotFoundError

key = "xx"
endpoint_string = "https://xx.cognitiveservices.azure.com/"

form_recognizer_client = FormRecognizerClient(endpoint=endpoint_string, credential=AzureKeyCredential(key))
form_training_client = FormTrainingClient(endpoint_string, AzureKeyCredential(key))

formUrl = "https://xx.blob.core.windows.net/formrecog/Train/Invoice_1.pdf?st="

poller = form_recognizer_client.begin_recognize_content_from_url(formUrl)
contents = poller.result()

def format_bounding_box(bounding_box):
    if not bounding_box:
        return "N/A"
    return ", ".join(["[{}, {}]".format(p.x, p.y) for p in bounding_box])

for idx, content in enumerate(contents):
    print("----Recognizing content from page #{}----".format(idx))
    print("Has width: {} and height: {}, measured with unit: {}".format(
        content.width,
        content.height,
        content.unit
    ))
    for table_idx, table in enumerate(content.tables):
        print("Table # {} has {} rows and {} columns".format(table_idx, table.row_count, table.column_count))
        for cell in table.cells:
            print("...Cell[{}][{}] has text '{}' within bounding box '{}'".format(
                cell.row_index,
                cell.column_index,
                cell.text,
                format_bounding_box(cell.bounding_box)
            ))
    for line_idx, line in enumerate(content.lines):
        print("Line # {} has word count '{}' and text '{}' within bounding box '{}'".format(
            line_idx,
            len(line.words),
            line.text,
            format_bounding_box(line.bounding_box)
        ))
    print("----------------------------------------")

print("done")
