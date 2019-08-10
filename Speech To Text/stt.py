#! /usr/bin/env python
import requests
import json
import os
from ibm_watson import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    # Add apikey here
    iam_apikey='',
    url='https://stream.watsonplatform.net/speech-to-text/api'
)


def searchFiles():
    supported_formats = [".wav", ".flac", ".mp3", ".ogg"]
    curr_directory = os.path.dirname(os.path.abspath(__file__))  
    return [file for i in range(len(supported_formats)) for file in os.listdir(curr_directory) if file.endswith(supported_formats[i])]

def printTranscript(file):
    audio_path = os.path.dirname(os.path.abspath(__file__)) + '/' + file

    with open(audio_path, 'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/flac',
        ).get_result()

    transcript = speech_recognition_results["results"][0]["alternatives"][0]["transcript"]
    confidence = speech_recognition_results["results"][0]["alternatives"][0]["confidence"] * 100
    print("\n++++++++++++++++++++++++++++++++++++++", file, "transcript++++++++++++++++++++++++++++++++++++++", end='\n')
    print("Watson says with", str(confidence) + "%", "confidence that this was said:")
    print(transcript, end='\n\n')

def main():
    files = searchFiles()

    for i in range(len(files)):
        printTranscript(files[i])

if __name__ == "__main__":
    main()