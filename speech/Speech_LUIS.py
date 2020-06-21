# python -m pip install azure-cognitiveservices-speech
# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/setup-platform?tabs=dotnet%2Cwindows%2Cjre%2Cbrowser&pivots=programming-language-python
# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/regions

import azure.cognitiveservices.speech as speechsdk
    
print("starting ")


luis_key = ""
luis_region = "southcentralus"
luis_app = "xx"
intent_config = speechsdk.SpeechConfig(subscription=luis_key, region=luis_region)
intent_recognizer = speechsdk.intent.IntentRecognizer(speech_config=intent_config)
# Set up the config for the intent recognizer (remember that this uses the Language Understanding key, not the Speech Services key)!

model = speechsdk.intent.LanguageUnderstandingModel(app_id=luis_app)

intents = [
    (model, "FindFlights")
]

#You need to associate a LanguageUnderstandingModel with the intent recognizer and add the intents you want recognized. 
#intent_recognizer.add_intents(intents)
intent_recognizer.add_all_intents(model)

# Starts intent recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
print("Say something ")
intent_result = intent_recognizer.recognize_once()

if intent_result.reason == speechsdk.ResultReason.RecognizedIntent:
    print("Recognized: {}".format(intent_result.text))
elif intent_result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(intent_result.no_match_details))
elif intent_result.reason == speechsdk.ResultReason.Canceled:
    print("Intent recognition canceled: {}".format(intent_result.cancellation_details.reason))
    if intent_result.cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(intent_result.cancellation_details.error_details))

print("done ")
