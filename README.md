# Final Project: Emotion Detector

## About
An AI-based web application that detects emotions in text using the Watson NLP library. Built with Python and Flask.

## Features
- Emotion detection using Watson NLP EmotionPredict API
- Detects five emotions: anger, disgust, fear, joy, sadness
- Identifies the dominant emotion
- Web interface for easy interaction
- Error handling for blank/invalid input

## Project Structure
```
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
└── README.md
```

## How to Run
1. Install dependencies: `pip install flask requests`
2. Run the server: `python3 server.py`
3. Open browser at `http://localhost:5000`

## Running Tests
```bash
python3 -m unittest test_emotion_detection.py
```

## Static Code Analysis
```bash
pylint server.py
```
