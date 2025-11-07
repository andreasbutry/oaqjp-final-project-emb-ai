"""
Flask web application for emotion detection using Watson NLP.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Analyze the emotion of the provided text.
    
    Returns:
        str: Formatted response with emotion scores and dominant emotion,
             or error message for invalid input.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (indicating invalid input)
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    # Format the response as requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )
    return response_text

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
