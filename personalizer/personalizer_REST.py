# https://docs.microsoft.com/en-us/azure/cognitive-services/personalizer/tutorial-use-azure-notebook-generate-loop-data

import json
import matplotlib.pyplot as plt
import random
import requests
import time
import datetime
import uuid

print("starting ")
resource_key = "xxx"
personalization_base_url= 'https://xx.cognitiveservices.azure.com/'
modelLastModified = ""
# build URLs
personalization_rank_url = personalization_base_url + "personalizer/v1.0/rank"
personalization_reward_url = personalization_base_url + "personalizer/v1.0/events/" #add "{eventId}/reward"
personalization_model_properties_url = personalization_base_url + "personalizer/v1.0/model/properties"
personalization_model_policy_url = personalization_base_url + "personalizer/v1.0/configurations/policy"
personalization_service_configuration_url = personalization_base_url + "personalizer/v1.0/configurations/service"
headers = {'Ocp-Apim-Subscription-Key' : resource_key, 'Content-Type': 'application/json'}
# context features of users --  features of your users, their context or their environment when using your app
users = "C:/code/personalizer/users.json"
# action features  -  content items with features specific to each item
coffee = "C:/code/personalizer/coffee.json"
# empty JSON for Rank request
requestpath = "C:/code/personalizer/example-rankrequest.json"

#########################################################################################################3
def add_event_id(rankjsonobj):
    eventid = uuid.uuid4().hex
    rankjsonobj["eventId"] = eventid
    return eventid
#########################################################################################################3
def currentDateTime():
    currentDT = datetime.datetime.now()
    print (str(currentDT))
#########################################################################################################3
# prints out the last modified date and time that the model was updated.
def get_last_updated(currentModifiedDate):
    print('-----checking model')
    # get model properties
    response = requests.get(personalization_model_properties_url, headers = headers, params = None)
    print(response)
    print(response.json())
    # get lastModifiedTime
    lastModifiedTime = json.dumps(response.json()["lastModifiedTime"])
    if (currentModifiedDate != lastModifiedTime):
        currentModifiedDate = lastModifiedTime
        print(f'-----model updated: {lastModifiedTime}')
#########################################################################################################3
def get_service_settings():
    print('-----checking service settings')
    # get learning policy
    response = requests.get(personalization_model_policy_url, headers = headers, params = None)
    print(response)
    print(response.json())
    # get service settings
    response = requests.get(personalization_service_configuration_url, headers = headers, params = None)
    print(response)
    print(response.json())
#########################################################################################################3
random.seed(time.time())
userpref = None
rankactionsjsonobj = None
actionfeaturesobj = None

with open(users) as handle:
    userpref = json.loads(handle.read())

with open(coffee) as handle:
    actionfeaturesobj = json.loads(handle.read())

with open(requestpath) as handle:
    rankactionsjsonobj = json.loads(handle.read())

get_last_updated(modelLastModified)
get_service_settings()
print ("=========================")
#print(f'User count {len(userpref)}')
#print(f'Coffee count {len(actionfeaturesobj)}')
#########################################################################################################3
def add_random_user_and_contextfeatures(namesoption, weatheropt, timeofdayopt, rankjsonobj):
    name = namesoption[random.randint(0,3)]
    weather = weatheropt[random.randint(0,2)]
    timeofday = timeofdayopt[random.randint(0,2)]
    rankjsonobj['contextFeatures'] = [{'timeofday': timeofday, 'weather': weather, 'name': name}]
    return [name, weather, timeofday]
#########################################################################################################3
def add_action_features(rankjsonobj):  # adds list of coffee (action features)
    rankjsonobj["actions"] = actionfeaturesobj
#########################################################################################################3
#called after Rank API is called, for each iteration, compares user's preference for coffee, based on weather and time of day, 
# with the Personalizer's suggestion
def get_reward_from_simulated_data(name, weather, timeofday, prediction):
    if(userpref[name][weather][timeofday] == str(prediction)):
        return 1
    return 0
#########################################################################################################3
def iterations(n, modelCheck, jsonFormat):
    i = 1
    # default reward value - assumes failed prediction
    reward = 0
    # Print out dateTime
    currentDateTime()
    # collect results to aggregate in graph
    total = 0
    rewards = []
    count = []
    # default list of user, weather, time of day
    namesopt = ['Alice', 'Bob', 'Cathy', 'Dave']
    weatheropt = ['Sunny', 'Rainy', 'Snowy']
    timeofdayopt = ['Morning', 'Afternoon', 'Evening']
    while(i <= n):    ## starting loop 
        # create unique id to associate with an event
        eventid = add_event_id(jsonFormat)
        # generate a random sample
        [name, weather, timeofday] = add_random_user_and_contextfeatures(namesopt, weatheropt, timeofdayopt, jsonFormat)
        # add action features to rank (coffee list)
        add_action_features(jsonFormat)
        
        # show JSON to send to Rank
        print('To: ', jsonFormat)
        # choose an action - get prediction from Personalizer, calling rank 
        response = requests.post(personalization_rank_url, headers = headers, params = None, json = jsonFormat)
        
        # show Rank prediction
        print ('From rank URL: ',response.json())
        
        # compare personalization service recommendation with the simulated data to generate a reward value
        prediction = json.dumps(response.json()["rewardActionId"]).replace('"','')

        # compares user's preference for coffee  with the Personalizer's suggestion
        reward = get_reward_from_simulated_data(name, weather, timeofday, prediction)
        
        # show result for iteration
        print(f'   {i} {currentDateTime()} {name} {weather} {timeofday} {prediction} {reward}')
        
        # send the reward to the service for the specific event_id
        response = requests.post(personalization_reward_url + eventid + "/reward", headers = headers, params= None, json = { "value" : reward })
        
        # for every N rank requests, compute total correct  total
        total =  total + reward
        
        # every N iteration, get last updated model date and time
        if(i % modelCheck == 0):
            print("**** 10% of loop found")
            get_last_updated(modelLastModified)

        # aggregate so chart is easier to read
        if(i % 10 == 0):
            rewards.append( total)
            count.append(i)
            total = 0

        i = i + 1

    # Print out dateTime
    currentDateTime()
    return [count, rewards]

# max iterations
num_requests = 10
# check last mod date N% of time - currently 10%
lastModCheck = int(num_requests * .10)
jsonTemplate = rankactionsjsonobj
# main iterations
[count, rewards] = iterations(num_requests, lastModCheck, jsonTemplate)


print("done")

