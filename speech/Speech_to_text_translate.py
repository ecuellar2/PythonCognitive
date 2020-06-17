# python -m pip install azure-cognitiveservices-speech
# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/setup-platform?tabs=dotnet%2Cwindows%2Cjre%2Cbrowser&pivots=programming-language-python

import azure.cognitiveservices.speech as speechsdk

print("starting ")

speech_key = ""
service_region = ""

translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key, region=service_region)
fromLanguage = 'en-US'
toLanguage = 'de'
translation_config.speech_recognition_language = fromLanguage
translation_config.add_target_language(toLanguage)
recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config)
print("Say something...")
result = recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.TranslatedSpeech:
    print("RECOGNIZED '{}': {}".format(fromLanguage, result.text))
    print("TRANSLATED into {}: {}".format(toLanguage, result.translations['de']))
elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("RECOGNIZED: {} (text could not be translated)".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("NOMATCH: Speech could not be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    print("CANCELED: Reason={}".format(result.cancellation_details.reason))
    if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("CANCELED: ErrorDetails={}".format(result.cancellation_details.error_details))


print("done ")
