
# https://docs.microsoft.com/en-us/azure/cognitive-services/anomaly-detector/quickstarts/detect-data-anomalies-python?tabs=windows
# https://github.com/Azure-Samples/AnomalyDetector/blob/master/quickstarts/python-detect-anomalies.py

import os
import requests
import json

print("starting ")

endpoint = "https://xx.cognitiveservices.azure.com"
subscription_key = "xx"
batch_detection_url = "/anomalydetector/v1.0/timeseries/entire/detect"
latest_point_detection_url = "/anomalydetector/v1.0/timeseries/last/detect"
data_location = "C:/code/anomaly/request-data.json"
file_handler = open(data_location)
json_data = json.load(file_handler) # can also use csv 

'''
By default, the upper and lower boundaries for anomaly detection are calculated using expectedValue, upperMargin, and lowerMargin.
If you require different boundaries, we recommend applying a marginScale to upperMargin or lowerMargin.
is negative anomaly
IsNegativeAnomaly contains anomaly status in negative direction for each input point. 
True means a negative anomaly has been detected. A negative anomaly means the point is detected as an anomaly and its real
 value is smaller than the expected one.

is positive anomaly
IsPositiveAnomaly contain anomaly status in positive direction for each input point. True means a positive anomaly has been detected. 
A positive anomaly means the point is detected as an anomaly and its real value is larger than the expected one. 

'''

def send_request(endpoint, url, subscription_key, request_data):
    headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': subscription_key}
    response = requests.post(endpoint+url, data=json.dumps(request_data), headers=headers)
    return json.loads(response.content.decode("utf-8"))


def detect_batch(request_data):
    print("Detecting anomalies as a batch")
    # Send the request, and print the JSON result
    result = send_request(endpoint, batch_detection_url, subscription_key, request_data)
    print(json.dumps(result, indent=4))

    if result.get('code') is not None:
        print("Detection failed. ErrorCode:{}, ErrorMessage:{}".format(result['code'], result['message']))
    else:
        # Find and display the positions of anomalies in the data set
        anomalies = result["isAnomaly"]
        print("Anomalies detected in the following data positions:")

        for x in range(len(anomalies)):
            if anomalies[x]:
                print (x, request_data['series'][x]['value'])
#to determine if the latest data point in your time series is an anomaly
def detect_latest(request_data):
    print("Determining if latest data point is an anomaly")
    # send the request, and print the JSON result
    result = send_request(endpoint, latest_point_detection_url, subscription_key, request_data)
    print(json.dumps(result, indent=4))

#detect_batch(json_data)
detect_latest(json_data)

print("done")

