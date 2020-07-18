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

# Train a model without labels, had issues with BLOB reference, need to research later !!!!!!!!!
trainingDataUrl ="https://xx.blob.core.windows.net/Train/Invoice_1.pdf?SAStoken"
poller = form_training_client.begin_training(trainingDataUrl, use_training_labels=False)
model = poller.result()

# Custom model information
print("Model ID: {}".format(model.model_id))
print("Status: {}".format(model.status))
print("Created on: {}".format(model.requested_on))
print("Last modified: {}".format(model.completed_on))
print("Recognized fields:")
# Looping through the submodels, which contains the fields they were trained on
for submodel in model.submodels:
    print("...The submodel has form type '{}'".format(submodel.form_type))
    for name, field in submodel.fields.items():
        print("...The model found field '{}' to have label '{}'".format(
            name, field.label
        ))

# You can also train custom models by manually labeling the training documents.
# Training with labels leads to better performance in some scenarios.
'''
To train with labels, you need to have special label information files (<filename>.pdf.labels.json) in your blob storage
 container alongside the training documents. The Form Recognizer sample labeling tool provides a UI to help you create these
  label files. Once you have them, you can call the begin_training function with the use_training_labels parameter set to true.
'''
poller = form_training_client.begin_training(trainingDataUrl, use_training_labels=True)
model = poller.result()
print("Recognized fields:")
# Custom model information
print("Model ID: {}".format(model.model_id))
print("Status: {}".format(model.status))
print("Created on: {}".format(model.created_on))
print("Last modified: {}".format(model.last_modified))

# looping through the submodels, which contains the fields they were trained on
# The labels are based on the ones you gave the training document.
for submodel in model.submodels:
for submodel in model.submodels:
    print("...The submodel with form type {} has accuracy '{}'".format(submodel.form_type, submodel.accuracy))
    for name, field in submodel.fields.items():
        print("...The model found field '{}' to have name '{}' with an accuracy of {}".format(
            name, field.name, field.accuracy
        ))

print("done")
