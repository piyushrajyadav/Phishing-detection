import json
import os

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

# Example usage in the app
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

