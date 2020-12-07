#  C:\python\python -m pip install azure-ai-metricsadvisor --upgrade                  use upgrade instead of --pre
#  https://azuresdkdocs.blob.core.windows.net/$web/python/azure-ai-metricsadvisor/latest/azure.ai.metricsadvisor.html
#  https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-metricsadvisor_1.0.0b2/sdk/metricsadvisor/azure-ai-metricsadvisor

#import datetime, json, os, time
import datetime
from azure.ai.metricsadvisor import (MetricsAdvisorKeyCredential,MetricsAdvisorAdministrationClient, MetricsAdvisorClient)
from azure.ai.metricsadvisor.models import DetectionAnomalyFilterCondition
from azure.ai.metricsadvisor.models import DimensionGroupIdentity
from config import DefaultConfig

endpoint_string = "https://xx.cognitiveservices.azure.com/"
CONFIG = DefaultConfig()
key = CONFIG.KEY
api_key = CONFIG.API_KEY
config_id = "x"

#client = MetricsAdvisorAdministrationClient (endpoint_string,MetricsAdvisorKeyCredential(key, api_key))
client = MetricsAdvisorClient(endpoint_string,MetricsAdvisorKeyCredential(key, api_key))
dim_filter = DetectionAnomalyFilterCondition( dimension_filter =[
    {
        "dimension": 
        {
            "namefield1": "valuehere"
        }
    },
    {
        "dimension": 
        {
            "namefield1 or another field": "valuehere_treated_as_OR"
        }
    }

]  )


#  startTime should be less than endTime parameters for API to work
#  Single day incidents:
#  start_time filter must be <=incident start time
#  end_time   filter must be > incident end time
#  Multiple day incidents:
#  start_time filter must be <=incident start time
#  end_time   filter must be >= incident end time (but should use ">" so that result.last_time picks up correct end time  )


results = client.list_incidents(detection_configuration_id=config_id,start_time=datetime.datetime(2020, 11, 15),
    end_time=datetime.datetime(2020, 11, 18),filter = dim_filter)

for result in results:
    print("======================================================")
    print("Incident ID: {}".format(result.id)) # AnomalyIncident object
    #print("Severity: {}".format(result.severity))
    #print("Status: {}".format(result.status))
    print("Start Time: {}".format(result.start_time))
    print("Last Time: {}".format(result.last_time))
    print("DimensionKey: {}".format(result.dimension_key))        

print("----------------------------------------------------------------------")
'''
results = client.list_incident_root_causes(
    detection_configuration_id=config_id,
    incident_id="xxx",
)
for result in results:
    print("Score: {}".format(result.score))
    print("Description: {}".format(result.description))
'''
print("Done ")
