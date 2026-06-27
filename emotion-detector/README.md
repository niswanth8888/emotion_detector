# Emotion Detector

Emotion Detector is an AI-based Flask web application that analyzes user text and identifies emotion scores for anger, disgust, fear, joy, and sadness. It also returns the dominant emotion.

## Project Tasks

- Clone the project repository
- Create an emotion detection application using the Watson NLP library
- Format the output of the application
- Package the application
- Run unit tests
- Deploy the application using Flask
- Incorporate error handling
- Run static code analysis

## Project Structure

```text
emotion-detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── tests/
│   └── test_emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   ├── mywebscript.js
│   └── style.css
├── server.py
├── requirements.txt
└── README.md
```

## Run the application

```bash
python3 server.py
```

Open the application in the browser and test the emotion detector.

## Run unit tests

```bash
python3 -m unittest tests/test_emotion_detection.py
```

## Run static code analysis

```bash
pylint server.py
```
