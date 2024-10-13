import React, { useState } from 'react';
import './FeedbackForm.css';
import { submitFeedback } from '../api'; // Import submitFeedback from api.js

const FeedbackForm = ({ url, onSubmit }) => {
    const [feedback, setFeedback] = useState('');
    const [submitStatus, setSubmitStatus] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setSubmitStatus(null); // Reset submission status

        const success = await submitFeedback(url, feedback);
        if (success) {
            setSubmitStatus('Feedback received!'); // Successful submission
            setFeedback(''); // Clear feedback field
            if (onSubmit) {
                onSubmit(); // Call the onSubmit prop if provided
            }
        } else {
            setSubmitStatus('Error submitting feedback.'); // Handle error case
        }
    };

    return (
        <div className="feedback-form-container">
            <form onSubmit={handleSubmit}>
                <textarea
                    placeholder="Provide feedback here..."
                    value={feedback}
                    onChange={(e) => setFeedback(e.target.value)}
                    className="feedback-textarea"
                />
                <button type="submit" className="feedback-submit-btn">Submit Feedback</button>
            </form>
            {submitStatus && <p>{submitStatus}</p>} {/* Display submission status */}
        </div>
    );
};

export default FeedbackForm;
