# python -m pip install azure-cognitiveservices-speech
# https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/setup-platform?tabs=dotnet%2Cwindows%2Cjre%2Cbrowser&pivots=programming-language-python

import azure.cognitiveservices.speech as speechsdk

print("starting ")

speech_key = "x"
service_region = "southcentralus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

audio_filename = "C:/code/audio/audio2.wav"

audio_input = speechsdk.audio.AudioConfig(filename=audio_filename)
# audio_config parameter used to reference file name
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

print("Recognizing first result...")

# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task returns the recognition text as result. 
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query. 
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
result = speech_recognizer.recognize_once()

# Checks result.
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))


print("done ")
