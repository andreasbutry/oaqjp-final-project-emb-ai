import requests
import json

def emotion_detector(text_to_analyze):
     # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the sentiment analysis service
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, headers=headers, json=myobj)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    #  Make sure, that all keys are available
    anger = emotions.get('anger', 0)
    disgust = emotions.get('disgust', 0)
    fear = emotions.get('fear', 0)
    joy = emotions.get('joy', 0)
    sadness = emotions.get('sadness', 0)
    
    emotions_dict = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    # Find dominant emotion by max score
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    
    # Add dominant emotion
    emotions_dict['dominant_emotion'] = dominant_emotion

    return emotions_dict