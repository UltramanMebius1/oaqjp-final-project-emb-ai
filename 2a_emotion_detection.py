def emotion_detector(text):

    if not text:
        return {
            "status": 400,
            "error": "Empty input provided"
        }

    # MOCK Watson NLP result (for assignment)
    emotions = {
        "anger": 0.1,
        "joy": 0.8,
        "sadness": 0.0,
        "fear": 0.0,
        "disgust": 0.1
    }

    emotions["dominant_emotion"] = "joy"
    return emotions
