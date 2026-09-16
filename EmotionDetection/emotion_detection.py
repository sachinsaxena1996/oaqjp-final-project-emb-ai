import json
from flask import Flask, request, jsonify
import requests


app = Flask('Final Project')

URL = (
    "https://sn-watson-emotion.labs.skills.network"
    "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def emotion_detector(text_to_analyze):
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=payload, headers=HEADERS)
    # Returns the raw text attribute of the HTTP response
    json_dict =  json.loads(response.text)
    emotions = json_dict['emotionPredictions'][0]['emotion']
    final_output = {
                'anger': emotions['anger'],
                'disgust': emotions['disgust'],
                'fear': emotions['fear'],
                'joy': emotions['joy'],
                'sadness': emotions['sadness'],
                'dominant_emotion': max(emotions, key=emotions.get)
            }

    return final_output