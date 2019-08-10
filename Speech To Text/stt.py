#! /usr/bin/env python
import requests
import json
import os
from ibm_watson import SpeechToTextV1

def searchFiles():
    supported_formats = [".wav", ".flac", ".mp3", ".ogg"]
   
    curr_path = os.path.dirname(os.path.abspath(__file__))
    # Not sure if it looks good, but I'll keep it for now.    
    return [file for i in range(len(supported_formats)) for file in os.listdir(curr_path) if file.endswith(supported_formats[i])]

def printTranscript():
    audio_path = os.path.dirname(os.path.abspath(__file__)) + '/audio-file.flac'

    with open(audio_path, 'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/flac',
        ).get_result()

    transcript = speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
    print("Transcript: ", transcript)

# Don't worry the key has been deleted :)
speech_to_text = SpeechToTextV1(
    iam_apikey='34mk2TEXUBRWjma7q7bdkTVS9jZaJLsB8vDIDcdKE2zu',
    url='https://stream.watsonplatform.net/speech-to-text/api'
)

files = searchFiles()

for i in range(len(files)):
    printTranscript()