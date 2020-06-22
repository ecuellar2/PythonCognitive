# python -m pip install azure-cognitiveservices-anomalydetector
# python -m pip install pandas
# https://docs.microsoft.com/en-us/azure/cognitive-services/anomaly-detector/quickstarts/client-libraries?tabs=windows&pivots=programming-language-python
# https://github.com/Azure-Samples/AnomalyDetector/blob/master/quickstarts/sdk/python-sdk-sample.py

from azure.cognitiveservices.anomalydetector import AnomalyDetectorClient
from azure.cognitiveservices.anomalydetector.models import Request, Point, Granularity, \
    APIErrorException
from msrest.authentication import CognitiveServicesCredentials
import pandas as pd
import os

print("starting ")

endpoint = "https://xx.cognitiveservices.azure.com"
subscription_key = "xx"
data_location = "C:/code/anomaly/request-data.csv"

client = AnomalyDetectorClient(endpoint, CognitiveServicesCredentials(subscription_key))
series = []
# Load your data file with the Pandas library's read_csv() method
data_file = pd.read_csv(data_location, header=None, encoding='utf-8', parse_dates=[0])
for index, row in data_file.iterrows():
    series.append(Point(timestamp=row[0], value=row[1]))

request = Request(series=series, granularity=Granularity.daily)

'''
print('Detecting anomalies in the entire time series.')
response = client.entire_detect(request)
if True in response.is_anomaly:
    print('An anomaly was detected at index:')
    for i in range(len(response.is_anomaly)):
        if response.is_anomaly[i]:
            print(i)
else:
    print('No anomalies were detected in the time series.')
'''

print('Detecting the anomaly status of the latest data point.')
response = client.last_detect(request)

if response.is_anomaly:
    print('The latest point is detected as anomaly.')
else:
    print('The latest point is not detected as anomaly.')

print("done")

