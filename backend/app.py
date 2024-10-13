from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from utils.url_analysis import analyze_url
import json
import os

app = Flask(__name__)
CORS(app)

# Load the model
model_path = r'C:\Users\piyus\Downloads\projects\Phishing-detection\backend\model\phishing_model.pkl'
model = joblib.load(model_path)

# Route for testing if the server is running
@app.route('/')
def home():
    return "Flask is working!"

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    url_to_analyze = data.get('url')

    if not url_to_analyze:
        return jsonify({'error': 'No URL provided'}), 400

    features = analyze_url(url_to_analyze)
    try:
        prediction = model.predict([features])
        return jsonify({'prediction': int(prediction[0])})  # Ensure prediction is returned correctly
    except Exception as e:
        print(f"Error during prediction: {e}")  # Log the error
        return jsonify({'error': str(e)}), 500  # Return a server error if something goes wrong

FEEDBACK_FILE = r'C:\Users\piyus\Downloads\projects\Phishing-detection\backend\feedback\feedback.json'

def save_feedback(data):
    # Load existing feedback if the file exists
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, 'r') as f:
            feedback = json.load(f)
    else:
        feedback = []

    # Append new feedback
    feedback.append(data)

    # Save back to the file
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump(feedback, f)

@app.route('/api/feedback', methods=['POST'])
def collect_feedback():
    data = request.json
    if not data:
        return jsonify({'error': 'No feedback provided'}), 400
    
    try:
        save_feedback(data)  # Save feedback
        return jsonify({'message': 'Feedback received'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return a server error if something goes wrong

if __name__ == '__main__':
    app.run(debug=True)
