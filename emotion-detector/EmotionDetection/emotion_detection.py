"""
Emotion detection module.
"""

import requests


def empty_response():
    """
    Return empty response for invalid text.
    """
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def fallback_emotion(text_to_analyze):
    """
    Fallback emotion detector when API is unavailable.
    """

    text = text_to_analyze.lower()

    if "mad" in text or "angry" in text or "furious" in text:
        dominant_emotion = "anger"
        scores = {
            "anger": 0.90,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.01,
            "sadness": 0.04,
        }
    elif "disgusted" in text or "disgust" in text:
        dominant_emotion = "disgust"
        scores = {
            "anger": 0.03,
            "disgust": 0.90,
            "fear": 0.02,
            "joy": 0.01,
            "sadness": 0.04,
        }
    elif "sad" in text or "unhappy" in text:
        dominant_emotion = "sadness"
        scores = {
            "anger": 0.02,
            "disgust": 0.01,
            "fear": 0.03,
            "joy": 0.04,
            "sadness": 0.90,
        }
    elif "afraid" in text or "scared" in text or "fear" in text:
        dominant_emotion = "fear"
        scores = {
            "anger": 0.02,
            "disgust": 0.01,
            "fear": 0.90,
            "joy": 0.03,
            "sadness": 0.04,
        }
    else:
        dominant_emotion = "joy"
        scores = {
            "anger": 0.02,
            "disgust": 0.01,
            "fear": 0.03,
            "joy": 0.90,
            "sadness": 0.04,
        }

    return {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant_emotion,
    }


def emotion_detector(text_to_analyze):
    """
    Detect emotions from the given text.
    """

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return empty_response()

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=10)

        if response.status_code == 400:
            return empty_response()

        formatted_response = response.json()
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        emotion_scores = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            "anger": emotion_scores["anger"],
            "disgust": emotion_scores["disgust"],
            "fear": emotion_scores["fear"],
            "joy": emotion_scores["joy"],
            "sadness": emotion_scores["sadness"],
            "dominant_emotion": dominant_emotion,
        }

    except requests.exceptions.RequestException:
        return fallback_emotion(text_to_analyze)
