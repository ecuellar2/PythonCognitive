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

receiptUrl = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"
poller = form_recognizer_client.begin_recognize_receipts_from_url(receiptUrl)
receipts = poller.result()

'''
begin_recognize_content is another option besides recognize_receipts
Extract text and content/layout information from a given document. 
The input document must be of one of the supported content types - 'application/pdf', 'image/jpeg', 'image/png' or 'image/tiff'.
''


for idx, receipt in enumerate(receipts):
    print("--------Recognizing receipt #{}--------".format(idx))
    receipt_type = receipt.fields.get("ReceiptType")
    if receipt_type:
        print("Receipt Type: {} has confidence: {}".format(receipt_type.value, receipt_type.confidence))
    merchant_name = receipt.fields.get("MerchantName")
    if merchant_name:
        print("Merchant Name: {} has confidence: {}".format(merchant_name.value, merchant_name.confidence))
    transaction_date = receipt.fields.get("TransactionDate")
    if transaction_date:
        print("Transaction Date: {} has confidence: {}".format(transaction_date.value, transaction_date.confidence))


print("Receipt items:")
for idx, item in enumerate(receipt.fields.get("Items").value):
    print("...Item #{}".format(idx))
    item_name = item.value.get("Name")
    if item_name:
        print("......Item Name: {} has confidence: {}".format(item_name.value, item_name.confidence))
    item_quantity = item.value.get("Quantity")
    if item_quantity:
        print("......Item Quantity: {} has confidence: {}".format(item_quantity.value, item_quantity.confidence))
    item_price = item.value.get("Price")
    if item_price:
        print("......Individual Item Price: {} has confidence: {}".format(item_price.value, item_price.confidence))
    item_total_price = item.value.get("TotalPrice")
    if item_total_price:
        print("......Total Item Price: {} has confidence: {}".format(item_total_price.value, item_total_price.confidence))


subtotal = receipt.fields.get("Subtotal")
if subtotal:
    print("Subtotal: {} has confidence: {}".format(subtotal.value, subtotal.confidence))
tax = receipt.fields.get("Tax")
if tax:
    print("Tax: {} has confidence: {}".format(tax.value, tax.confidence))
tip = receipt.fields.get("Tip")
if tip:
    print("Tip: {} has confidence: {}".format(tip.value, tip.confidence))
total = receipt.fields.get("Total")
if total:
    print("Total: {} has confidence: {}".format(total.value, total.confidence))
print("--------------------------------------")

print("done")
